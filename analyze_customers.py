"""
E-commerce Customer Dataset Analysis (Enhanced)
===============================================
This script performs comprehensive analysis on e-commerce customer data including:
- Customer segmentation
- Purchase behavior analysis
- Browsing patterns
- Product preferences
- Customer Lifetime Value (CLV)
- Payment methods and preferences
- Social media engagement
- Customer satisfaction
- Loyalty program analysis
- Email marketing metrics
- Geographic analysis
- And 20+ more unique features

Author: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

# Set style for better visualizations
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

def load_data(file_path='ecommerce_customers.csv'):
    """
    Load the e-commerce customer dataset
    
    Returns:
        DataFrame: Customer data
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Dataset loaded successfully: {len(df)} customers")
        return df
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
        return None

def explore_data(df):
    """
    Perform exploratory data analysis
    """
    print("\n" + "="*60)
    print("EXPLORATORY DATA ANALYSIS")
    print("="*60)
    
    # Basic information
    print("\n1. Dataset Overview:")
    print(f"   Total Customers: {len(df)}")
    print(f"   Total Features: {len(df.columns)}")
    
    # Data types and missing values
    print("\n2. Data Quality:")
    print(df.info())
    print(f"\n   Missing Values: {df.isnull().sum().sum()}")
    
    # Statistical summary
    print("\n3. Statistical Summary:")
    print(df.describe())
    
    # Categorical columns
    print("\n4. Categorical Features:")
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        print(f"\n   {col}:")
        print(df[col].value_counts())

def analyze_segments(df):
    """
    Analyze customer segments
    """
    print("\n" + "="*60)
    print("CUSTOMER SEGMENTATION ANALYSIS")
    print("="*60)
    
    segment_stats = df.groupby('segment').agg({
        'annual_income': ['mean', 'median', 'std'],
        'spending_score': ['mean', 'median', 'std'],
        'purchase_frequency': ['mean', 'median'],
        'avg_order_value': ['mean', 'median'],
        'total_purchases': ['mean', 'sum'],
        'browsing_time_minutes': ['mean', 'median']
    }).round(2)
    
    print("\nSegment Statistics:")
    print(segment_stats)
    
    # Segment distribution
    print("\nSegment Distribution:")
    segment_counts = df['segment'].value_counts()
    for segment, count in segment_counts.items():
        percentage = (count / len(df)) * 100
        print(f"   {segment}: {count} customers ({percentage:.1f}%)")

def analyze_purchasing_behavior(df):
    """
    Analyze customer purchasing behavior
    """
    print("\n" + "="*60)
    print("PURCHASING BEHAVIOR ANALYSIS")
    print("="*60)
    
    # Correlation analysis
    numeric_cols = ['age', 'annual_income', 'spending_score', 'purchase_frequency', 
                   'avg_order_value', 'total_purchases', 'browsing_time_minutes']
    correlation_matrix = df[numeric_cols].corr()
    
    print("\n1. Correlation Matrix (Top Correlations):")
    # Get top correlations
    corr_pairs = []
    for i in range(len(correlation_matrix.columns)):
        for j in range(i+1, len(correlation_matrix.columns)):
            corr_pairs.append((
                correlation_matrix.columns[i],
                correlation_matrix.columns[j],
                correlation_matrix.iloc[i, j]
            ))
    
    corr_pairs.sort(key=lambda x: abs(x[2]), reverse=True)
    for col1, col2, corr in corr_pairs[:10]:
        print(f"   {col1} ↔ {col2}: {corr:.3f}")
    
    # Gender analysis
    print("\n2. Gender-based Analysis:")
    gender_stats = df.groupby('gender').agg({
        'spending_score': 'mean',
        'purchase_frequency': 'mean',
        'avg_order_value': 'mean',
        'total_purchases': 'sum'
    }).round(2)
    print(gender_stats)
    
    # Age group analysis
    print("\n3. Age Group Analysis:")
    df['age_group'] = pd.cut(df['age'], bins=[0, 25, 35, 50, 100], 
                             labels=['Young (0-25)', 'Adult (26-35)', 'Middle (36-50)', 'Senior (50+)'])
    age_stats = df.groupby('age_group').agg({
        'spending_score': 'mean',
        'purchase_frequency': 'mean',
        'avg_order_value': 'mean'
    }).round(2)
    print(age_stats)

def analyze_product_preferences(df):
    """
    Analyze product category preferences
    """
    print("\n" + "="*60)
    print("PRODUCT PREFERENCE ANALYSIS")
    print("="*60)
    
    # Product category preferences
    print("\n1. Product Category Preferences:")
    category_stats = df.groupby('product_category_preference').agg({
        'customer_id': 'count',
        'spending_score': 'mean',
        'avg_order_value': 'mean',
        'purchase_frequency': 'mean',
        'customer_lifetime_value': 'mean'
    }).round(2)
    category_stats.columns = ['Customer Count', 'Avg Spending Score', 'Avg Order Value', 
                             'Avg Purchase Frequency', 'Avg CLV']
    print(category_stats)
    
    # Device type analysis
    print("\n2. Device Type Analysis:")
    device_stats = df.groupby('device_type').agg({
        'customer_id': 'count',
        'browsing_time_minutes': 'mean',
        'purchase_frequency': 'mean',
        'spending_score': 'mean',
        'mobile_app_user': lambda x: (x == 'Yes').sum()
    }).round(2)
    device_stats.columns = ['Customer Count', 'Avg Browsing Time', 'Avg Purchase Frequency', 
                           'Avg Spending Score', 'Mobile App Users']
    print(device_stats)
    
    # Cross-category purchases
    if 'cross_category_purchases' in df.columns:
        print("\n3. Cross-Category Purchase Analysis:")
        cross_cat_stats = df.groupby('cross_category_purchases').agg({
            'customer_id': 'count',
            'spending_score': 'mean',
            'customer_lifetime_value': 'mean'
        }).round(2)
        print(cross_cat_stats)

def perform_clustering(df, n_clusters=4):
    """
    Perform K-means clustering on customers
    """
    print("\n" + "="*60)
    print("CUSTOMER CLUSTERING (K-Means)")
    print("="*60)
    
    # Select features for clustering
    features = ['annual_income', 'spending_score', 'purchase_frequency', 'avg_order_value']
    X = df[features].values
    
    # Standardize features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Perform K-means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    df['cluster'] = kmeans.fit_predict(X_scaled)
    
    # Cluster analysis
    print(f"\nClustering with {n_clusters} clusters:")
    cluster_stats = df.groupby('cluster').agg({
        'annual_income': 'mean',
        'spending_score': 'mean',
        'purchase_frequency': 'mean',
        'avg_order_value': 'mean',
        'customer_id': 'count'
    }).round(2)
    cluster_stats.columns = ['Avg Income', 'Avg Spending Score', 'Avg Purchase Freq', 'Avg Order Value', 'Count']
    print(cluster_stats)
    
    return df

def analyze_enhanced_features(df):
    """
    Analyze enhanced features
    """
    print("\n" + "="*60)
    print("ENHANCED FEATURES ANALYSIS")
    print("="*60)
    
    # Customer Lifetime Value
    if 'customer_lifetime_value' in df.columns:
        print("\n1. Customer Lifetime Value Analysis:")
        clv_stats = df.groupby('segment')['customer_lifetime_value'].agg(['mean', 'median', 'sum']).round(2)
        print(clv_stats)
    
    # Payment methods
    if 'payment_method' in df.columns:
        print("\n2. Payment Method Preferences:")
        payment_stats = df.groupby('payment_method').agg({
            'customer_id': 'count',
            'avg_order_value': 'mean',
            'spending_score': 'mean'
        }).round(2)
        print(payment_stats)
    
    # Loyalty program
    if 'loyalty_tier' in df.columns:
        print("\n3. Loyalty Tier Distribution:")
        loyalty_stats = df.groupby('loyalty_tier').agg({
            'customer_id': 'count',
            'customer_lifetime_value': 'mean',
            'repeat_purchase_rate': 'mean'
        }).round(2)
        print(loyalty_stats)
    
    # Email marketing
    if 'email_open_rate' in df.columns:
        print("\n4. Email Marketing Metrics:")
        email_stats = df.groupby('newsletter_subscribed').agg({
            'email_open_rate': 'mean',
            'click_through_rate': 'mean',
            'customer_id': 'count'
        }).round(3)
        print(email_stats)
    
    # Social media engagement
    if 'social_media_engagement' in df.columns:
        print("\n5. Social Media Engagement:")
        social_stats = df.groupby('segment')['social_media_engagement'].agg(['mean', 'median']).round(1)
        print(social_stats)
    
    # Customer satisfaction
    if 'customer_satisfaction_score' in df.columns:
        print("\n6. Customer Satisfaction by Segment:")
        satisfaction_stats = df.groupby('segment')['customer_satisfaction_score'].agg(['mean', 'count']).round(2)
        print(satisfaction_stats)
    
    # Geographic analysis
    if 'geographic_region' in df.columns:
        print("\n7. Geographic Distribution:")
        geo_stats = df.groupby('geographic_region').agg({
            'customer_id': 'count',
            'spending_score': 'mean',
            'customer_lifetime_value': 'mean'
        }).round(2)
        print(geo_stats)
    
    # Referral sources
    if 'referral_source' in df.columns:
        print("\n8. Referral Source Analysis:")
        referral_stats = df.groupby('referral_source').agg({
            'customer_id': 'count',
            'spending_score': 'mean',
            'customer_lifetime_value': 'mean'
        }).round(2)
        print(referral_stats)

def generate_insights(df):
    """
    Generate key insights from the analysis
    """
    print("\n" + "="*60)
    print("KEY INSIGHTS")
    print("="*60)
    
    insights = []
    
    # Insight 1: High value customers
    high_value = df[df['segment'] == 'High Value']
    insights.append(f"High Value Customers: {len(high_value)} ({len(high_value)/len(df)*100:.1f}%) "
                   f"with average spending score of {high_value['spending_score'].mean():.1f}")
    
    # Insight 2: Most preferred category
    top_category = df['product_category_preference'].value_counts().index[0]
    insights.append(f"Most Preferred Category: {top_category} "
                   f"({df['product_category_preference'].value_counts()[top_category]} customers)")
    
    # Insight 3: Device preference
    top_device = df['device_type'].value_counts().index[0]
    insights.append(f"Most Used Device: {top_device} "
                   f"({df['device_type'].value_counts()[top_device]} customers)")
    
    # Insight 4: Average metrics
    insights.append(f"Average Annual Income: ${df['annual_income'].mean():,.0f}")
    insights.append(f"Average Spending Score: {df['spending_score'].mean():.1f}")
    insights.append(f"Average Purchase Frequency: {df['purchase_frequency'].mean():.1f} purchases")
    
    # Enhanced insights
    if 'customer_lifetime_value' in df.columns:
        insights.append(f"Average Customer Lifetime Value: ${df['customer_lifetime_value'].mean():,.2f}")
        insights.append(f"Total CLV: ${df['customer_lifetime_value'].sum():,.2f}")
    
    if 'loyalty_tier' in df.columns:
        top_tier = df['loyalty_tier'].value_counts().index[0]
        insights.append(f"Most Common Loyalty Tier: {top_tier}")
    
    if 'payment_method' in df.columns:
        top_payment = df['payment_method'].value_counts().index[0]
        insights.append(f"Most Preferred Payment Method: {top_payment}")
    
    if 'newsletter_subscribed' in df.columns:
        subscribed = (df['newsletter_subscribed'] == 'Yes').sum()
        insights.append(f"Newsletter Subscribers: {subscribed} ({subscribed/len(df)*100:.1f}%)")
    
    for i, insight in enumerate(insights, 1):
        print(f"\n{i}. {insight}")

def main():
    """
    Main analysis function
    """
    print("="*60)
    print("E-COMMERCE CUSTOMER DATASET ANALYSIS")
    print("RSK World - https://rskworld.in")
    print("="*60)
    
    # Load data
    df = load_data()
    if df is None:
        return
    
    # Perform analyses
    explore_data(df)
    analyze_segments(df)
    analyze_purchasing_behavior(df)
    analyze_product_preferences(df)
    analyze_enhanced_features(df)
    df = perform_clustering(df)
    generate_insights(df)
    
    # Save results
    output_file = 'customer_analysis_results.csv'
    df.to_csv(output_file, index=False)
    print(f"\nAnalysis results saved to '{output_file}'")
    
    print("\n" + "="*60)
    print("ANALYSIS COMPLETE")
    print("="*60)

if __name__ == "__main__":
    main()

