"""
Customer Segmentation using Clustering Models
=============================================
This script performs advanced customer segmentation using various clustering algorithms
including K-Means, DBSCAN, and Hierarchical Clustering.

Author: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import silhouette_score
import warnings
warnings.filterwarnings('ignore')

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 8)

def load_and_prepare_data(file_path='ecommerce_customers.csv'):
    """
    Load and prepare data for clustering
    """
    df = pd.read_csv(file_path)
    
    # Encode categorical variables
    le_gender = LabelEncoder()
    le_category = LabelEncoder()
    le_device = LabelEncoder()
    
    df['gender_encoded'] = le_gender.fit_transform(df['gender'])
    df['category_encoded'] = le_category.fit_transform(df['product_category_preference'])
    df['device_encoded'] = le_device.fit_transform(df['device_type'])
    
    return df, le_gender, le_category, le_device

def find_optimal_clusters(X, max_clusters=10):
    """
    Find optimal number of clusters using Elbow Method and Silhouette Score
    """
    inertias = []
    silhouette_scores = []
    K_range = range(2, max_clusters + 1)
    
    for k in K_range:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(X)
        inertias.append(kmeans.inertia_)
        silhouette_scores.append(silhouette_score(X, kmeans.labels_))
    
    # Find optimal k (highest silhouette score)
    optimal_k = K_range[np.argmax(silhouette_scores)]
    
    return optimal_k, inertias, silhouette_scores, K_range

def kmeans_segmentation(df, n_clusters=4):
    """
    Perform K-Means clustering
    """
    print("\n" + "="*60)
    print("K-MEANS CLUSTERING")
    print("="*60)
    
    # Select features
    features = ['annual_income', 'spending_score', 'purchase_frequency', 
                'avg_order_value', 'browsing_time_minutes']
    X = df[features].values
    
    # Standardize
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Find optimal clusters
    optimal_k, inertias, sil_scores, K_range = find_optimal_clusters(X_scaled)
    print(f"\nOptimal number of clusters: {optimal_k}")
    print(f"Best Silhouette Score: {sil_scores[optimal_k-2]:.3f}")
    
    # Perform clustering with optimal k
    kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
    df['kmeans_cluster'] = kmeans.fit_predict(X_scaled)
    
    # Analyze clusters
    print("\nCluster Characteristics:")
    cluster_analysis = df.groupby('kmeans_cluster').agg({
        'annual_income': 'mean',
        'spending_score': 'mean',
        'purchase_frequency': 'mean',
        'avg_order_value': 'mean',
        'browsing_time_minutes': 'mean',
        'customer_id': 'count'
    }).round(2)
    cluster_analysis.columns = ['Avg Income', 'Avg Spending', 'Avg Freq', 
                                'Avg Order Value', 'Avg Browsing Time', 'Count']
    print(cluster_analysis)
    
    return df, kmeans, scaler

def dbscan_segmentation(df):
    """
    Perform DBSCAN clustering
    """
    print("\n" + "="*60)
    print("DBSCAN CLUSTERING")
    print("="*60)
    
    # Select features
    features = ['annual_income', 'spending_score', 'purchase_frequency', 
                'avg_order_value', 'browsing_time_minutes']
    X = df[features].values
    
    # Standardize
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Perform DBSCAN
    dbscan = DBSCAN(eps=0.5, min_samples=5)
    df['dbscan_cluster'] = dbscan.fit_predict(X_scaled)
    
    # Analyze clusters
    n_clusters = len(set(df['dbscan_cluster'])) - (1 if -1 in df['dbscan_cluster'] else 0)
    n_noise = list(df['dbscan_cluster']).count(-1)
    
    print(f"\nNumber of clusters found: {n_clusters}")
    print(f"Number of noise points: {n_noise}")
    
    if n_clusters > 0:
        print("\nCluster Characteristics:")
        cluster_analysis = df[df['dbscan_cluster'] != -1].groupby('dbscan_cluster').agg({
            'annual_income': 'mean',
            'spending_score': 'mean',
            'purchase_frequency': 'mean',
            'avg_order_value': 'mean',
            'customer_id': 'count'
        }).round(2)
        print(cluster_analysis)
    
    return df, dbscan

def hierarchical_segmentation(df, n_clusters=4):
    """
    Perform Hierarchical Clustering
    """
    print("\n" + "="*60)
    print("HIERARCHICAL CLUSTERING")
    print("="*60)
    
    # Select features
    features = ['annual_income', 'spending_score', 'purchase_frequency', 
                'avg_order_value', 'browsing_time_minutes']
    X = df[features].values
    
    # Standardize
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Perform Agglomerative Clustering
    hierarchical = AgglomerativeClustering(n_clusters=n_clusters, linkage='ward')
    df['hierarchical_cluster'] = hierarchical.fit_predict(X_scaled)
    
    # Analyze clusters
    print("\nCluster Characteristics:")
    cluster_analysis = df.groupby('hierarchical_cluster').agg({
        'annual_income': 'mean',
        'spending_score': 'mean',
        'purchase_frequency': 'mean',
        'avg_order_value': 'mean',
        'customer_id': 'count'
    }).round(2)
    cluster_analysis.columns = ['Avg Income', 'Avg Spending', 'Avg Freq', 
                                'Avg Order Value', 'Count']
    print(cluster_analysis)
    
    return df, hierarchical

def compare_segments(df):
    """
    Compare different segmentation methods
    """
    print("\n" + "="*60)
    print("SEGMENTATION COMPARISON")
    print("="*60)
    
    print("\nOriginal Segment Distribution:")
    print(df['segment'].value_counts())
    
    if 'kmeans_cluster' in df.columns:
        print("\nK-Means Cluster Distribution:")
        print(df['kmeans_cluster'].value_counts().sort_index())
    
    if 'dbscan_cluster' in df.columns:
        print("\nDBSCAN Cluster Distribution:")
        print(df['dbscan_cluster'].value_counts().sort_index())
    
    if 'hierarchical_cluster' in df.columns:
        print("\nHierarchical Cluster Distribution:")
        print(df['hierarchical_cluster'].value_counts().sort_index())

def generate_segment_profiles(df):
    """
    Generate detailed profiles for each segment
    """
    print("\n" + "="*60)
    print("SEGMENT PROFILES")
    print("="*60)
    
    if 'kmeans_cluster' in df.columns:
        print("\nK-Means Segment Profiles:")
        for cluster in sorted(df['kmeans_cluster'].unique()):
            cluster_data = df[df['kmeans_cluster'] == cluster]
            print(f"\n  Cluster {cluster} ({len(cluster_data)} customers):")
            print(f"    - Avg Income: ${cluster_data['annual_income'].mean():,.0f}")
            print(f"    - Avg Spending Score: {cluster_data['spending_score'].mean():.1f}")
            print(f"    - Avg Purchase Frequency: {cluster_data['purchase_frequency'].mean():.1f}")
            print(f"    - Top Category: {cluster_data['product_category_preference'].mode()[0]}")
            print(f"    - Top Device: {cluster_data['device_type'].mode()[0]}")

def main():
    """
    Main segmentation function
    """
    print("="*60)
    print("CUSTOMER SEGMENTATION ANALYSIS")
    print("RSK World - https://rskworld.in")
    print("="*60)
    
    # Load and prepare data
    df, le_gender, le_category, le_device = load_and_prepare_data()
    print(f"\nDataset loaded: {len(df)} customers")
    
    # Perform different clustering methods
    df, kmeans, scaler = kmeans_segmentation(df)
    df, dbscan = dbscan_segmentation(df)
    df, hierarchical = hierarchical_segmentation(df)
    
    # Compare and analyze
    compare_segments(df)
    generate_segment_profiles(df)
    
    # Save results
    output_file = 'customer_segmentation_results.csv'
    df.to_csv(output_file, index=False)
    print(f"\nSegmentation results saved to '{output_file}'")
    
    print("\n" + "="*60)
    print("SEGMENTATION COMPLETE")
    print("="*60)

if __name__ == "__main__":
    main()

