"""
Data Visualization Script for E-commerce Customer Dataset
==========================================================
This script creates comprehensive visualizations including:
- Customer segment distributions
- Income vs spending analysis
- Product preference charts
- Device usage patterns
- Age group analysis

Author: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 8)
plt.rcParams['font.size'] = 10

def load_data(file_path='ecommerce_customers.csv'):
    """Load the dataset"""
    try:
        df = pd.read_csv(file_path)
        print(f"Dataset loaded: {len(df)} customers")
        return df
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
        return None

def plot_segment_distribution(df):
    """Plot customer segment distribution"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Count plot
    segment_counts = df['segment'].value_counts()
    axes[0].bar(segment_counts.index, segment_counts.values, 
                color=['#28a745', '#ffc107', '#6c757d'])
    axes[0].set_title('Customer Segment Distribution', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('Segment')
    axes[0].set_ylabel('Number of Customers')
    axes[0].grid(axis='y', alpha=0.3)
    
    # Pie chart
    colors = ['#28a745', '#ffc107', '#6c757d']
    axes[1].pie(segment_counts.values, labels=segment_counts.index, autopct='%1.1f%%',
                colors=colors, startangle=90)
    axes[1].set_title('Segment Percentage Distribution', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('segment_distribution.png', dpi=300, bbox_inches='tight')
    print("Saved: segment_distribution.png")
    plt.close()

def plot_income_vs_spending(df):
    """Plot income vs spending score"""
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Scatter plot with segment colors
    segment_colors = {'High Value': '#28a745', 'Medium Value': '#ffc107', 'Low Value': '#6c757d'}
    for segment in df['segment'].unique():
        segment_data = df[df['segment'] == segment]
        ax.scatter(segment_data['annual_income'], segment_data['spending_score'],
                  c=segment_colors[segment], label=segment, alpha=0.6, s=100)
    
    ax.set_xlabel('Annual Income ($)', fontsize=12)
    ax.set_ylabel('Spending Score', fontsize=12)
    ax.set_title('Annual Income vs Spending Score by Segment', fontsize=14, fontweight='bold')
    ax.legend()
    ax.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('income_vs_spending.png', dpi=300, bbox_inches='tight')
    print("Saved: income_vs_spending.png")
    plt.close()

def plot_product_preferences(df):
    """Plot product category preferences"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Category distribution
    category_counts = df['product_category_preference'].value_counts()
    # Use a color palette that works for any number of categories
    colors = plt.cm.Set3(range(len(category_counts)))
    axes[0].bar(category_counts.index, category_counts.values, color=colors)
    axes[0].set_title('Product Category Preferences', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('Category')
    axes[0].set_ylabel('Number of Customers')
    axes[0].grid(axis='y', alpha=0.3)
    
    # Category by segment
    category_segment = pd.crosstab(df['product_category_preference'], df['segment'])
    category_segment.plot(kind='bar', ax=axes[1], color=['#6c757d', '#ffc107', '#28a745'])
    axes[1].set_title('Product Category by Segment', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('Category')
    axes[1].set_ylabel('Number of Customers')
    axes[1].legend(title='Segment')
    axes[1].grid(axis='y', alpha=0.3)
    axes[1].tick_params(axis='x', rotation=45, ha='right')
    
    plt.tight_layout()
    plt.savefig('product_preferences.png', dpi=300, bbox_inches='tight')
    print("Saved: product_preferences.png")
    plt.close()

def plot_device_usage(df):
    """Plot device type usage patterns"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Device distribution
    device_counts = df['device_type'].value_counts()
    axes[0].bar(device_counts.index, device_counts.values, 
                color=['#007bff', '#28a745', '#ffc107'])
    axes[0].set_title('Device Type Distribution', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('Device Type')
    axes[0].set_ylabel('Number of Customers')
    axes[0].grid(axis='y', alpha=0.3)
    
    # Average browsing time by device
    device_browsing = df.groupby('device_type')['browsing_time_minutes'].mean().sort_values(ascending=False)
    axes[1].bar(device_browsing.index, device_browsing.values, color=['#007bff', '#28a745', '#ffc107'])
    axes[1].set_title('Average Browsing Time by Device', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('Device Type')
    axes[1].set_ylabel('Average Browsing Time (minutes)')
    axes[1].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('device_usage.png', dpi=300, bbox_inches='tight')
    print("Saved: device_usage.png")
    plt.close()

def plot_age_analysis(df):
    """Plot age group analysis"""
    # Create age groups
    df['age_group'] = pd.cut(df['age'], bins=[0, 25, 35, 50, 100], 
                             labels=['Young (0-25)', 'Adult (26-35)', 'Middle (36-50)', 'Senior (50+)'])
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    
    # Age distribution
    age_counts = df['age_group'].value_counts().sort_index()
    axes[0, 0].bar(range(len(age_counts)), age_counts.values, color=['#007bff', '#28a745', '#ffc107', '#dc3545'])
    axes[0, 0].set_xticks(range(len(age_counts)))
    axes[0, 0].set_xticklabels(age_counts.index, rotation=15, ha='right')
    axes[0, 0].set_title('Age Group Distribution', fontsize=12, fontweight='bold')
    axes[0, 0].set_ylabel('Number of Customers')
    axes[0, 0].grid(axis='y', alpha=0.3)
    
    # Average spending by age group
    age_spending = df.groupby('age_group')['spending_score'].mean().sort_index()
    axes[0, 1].bar(range(len(age_spending)), age_spending.values, color=['#007bff', '#28a745', '#ffc107', '#dc3545'])
    axes[0, 1].set_xticks(range(len(age_spending)))
    axes[0, 1].set_xticklabels(age_spending.index, rotation=15, ha='right')
    axes[0, 1].set_title('Average Spending Score by Age Group', fontsize=12, fontweight='bold')
    axes[0, 1].set_ylabel('Average Spending Score')
    axes[0, 1].grid(axis='y', alpha=0.3)
    
    # Age vs spending scatter
    axes[1, 0].scatter(df['age'], df['spending_score'], alpha=0.6, c=df['spending_score'], 
                      cmap='viridis', s=100)
    axes[1, 0].set_xlabel('Age')
    axes[1, 0].set_ylabel('Spending Score')
    axes[1, 0].set_title('Age vs Spending Score', fontsize=12, fontweight='bold')
    axes[1, 0].grid(alpha=0.3)
    
    # Age group by segment
    age_segment = pd.crosstab(df['age_group'], df['segment'])
    age_segment.plot(kind='bar', ax=axes[1, 1], color=['#6c757d', '#ffc107', '#28a745'])
    axes[1, 1].set_title('Age Group by Segment', fontsize=12, fontweight='bold')
    axes[1, 1].set_xlabel('Age Group')
    axes[1, 1].set_ylabel('Number of Customers')
    axes[1, 1].legend(title='Segment')
    axes[1, 1].grid(axis='y', alpha=0.3)
    axes[1, 1].tick_params(axis='x', rotation=15)
    
    plt.tight_layout()
    plt.savefig('age_analysis.png', dpi=300, bbox_inches='tight')
    print("Saved: age_analysis.png")
    plt.close()

def plot_correlation_heatmap(df):
    """Plot correlation heatmap"""
    numeric_cols = ['age', 'annual_income', 'spending_score', 'purchase_frequency',
                   'avg_order_value', 'total_purchases', 'browsing_time_minutes']
    correlation_matrix = df[numeric_cols].corr()
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0,
                square=True, linewidths=1, cbar_kws={"shrink": 0.8})
    plt.title('Feature Correlation Heatmap', fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig('correlation_heatmap.png', dpi=300, bbox_inches='tight')
    print("Saved: correlation_heatmap.png")
    plt.close()

def plot_purchase_behavior(df):
    """Plot purchase behavior analysis"""
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    
    # Purchase frequency distribution
    axes[0, 0].hist(df['purchase_frequency'], bins=20, color='#007bff', edgecolor='black', alpha=0.7)
    axes[0, 0].set_title('Purchase Frequency Distribution', fontsize=12, fontweight='bold')
    axes[0, 0].set_xlabel('Purchase Frequency')
    axes[0, 0].set_ylabel('Number of Customers')
    axes[0, 0].grid(axis='y', alpha=0.3)
    
    # Average order value by segment
    segment_aov = df.groupby('segment')['avg_order_value'].mean().sort_values(ascending=False)
    axes[0, 1].bar(segment_aov.index, segment_aov.values, color=['#28a745', '#ffc107', '#6c757d'])
    axes[0, 1].set_title('Average Order Value by Segment', fontsize=12, fontweight='bold')
    axes[0, 1].set_xlabel('Segment')
    axes[0, 1].set_ylabel('Average Order Value ($)')
    axes[0, 1].grid(axis='y', alpha=0.3)
    
    # Purchase frequency vs spending score
    axes[1, 0].scatter(df['purchase_frequency'], df['spending_score'], 
                      alpha=0.6, c=df['spending_score'], cmap='viridis', s=100)
    axes[1, 0].set_xlabel('Purchase Frequency')
    axes[1, 0].set_ylabel('Spending Score')
    axes[1, 0].set_title('Purchase Frequency vs Spending Score', fontsize=12, fontweight='bold')
    axes[1, 0].grid(alpha=0.3)
    
    # Total purchases by segment
    segment_purchases = df.groupby('segment')['total_purchases'].sum()
    axes[1, 1].bar(segment_purchases.index, segment_purchases.values, 
                   color=['#28a745', '#ffc107', '#6c757d'])
    axes[1, 1].set_title('Total Purchases by Segment', fontsize=12, fontweight='bold')
    axes[1, 1].set_xlabel('Segment')
    axes[1, 1].set_ylabel('Total Purchases')
    axes[1, 1].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('purchase_behavior.png', dpi=300, bbox_inches='tight')
    print("Saved: purchase_behavior.png")
    plt.close()

def main():
    """Main visualization function"""
    print("="*60)
    print("E-COMMERCE CUSTOMER DATASET - DATA VISUALIZATION")
    print("RSK World - https://rskworld.in")
    print("="*60)
    
    # Load data
    df = load_data()
    if df is None:
        return
    
    # Generate all visualizations
    print("\nGenerating visualizations...")
    plot_segment_distribution(df)
    plot_income_vs_spending(df)
    plot_product_preferences(df)
    plot_device_usage(df)
    plot_age_analysis(df)
    plot_correlation_heatmap(df)
    plot_purchase_behavior(df)
    
    print("\n" + "="*60)
    print("ALL VISUALIZATIONS GENERATED SUCCESSFULLY!")
    print("="*60)
    print("\nGenerated files:")
    print("  - segment_distribution.png")
    print("  - income_vs_spending.png")
    print("  - product_preferences.png")
    print("  - device_usage.png")
    print("  - age_analysis.png")
    print("  - correlation_heatmap.png")
    print("  - purchase_behavior.png")

if __name__ == "__main__":
    main()

