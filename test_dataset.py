"""
Test script to verify dataset quality
Author: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
"""

import pandas as pd
import sys

def test_dataset():
    """Test dataset for quality issues"""
    print("="*60)
    print("DATASET QUALITY CHECK")
    print("="*60)
    
    try:
        df = pd.read_csv('ecommerce_customers.csv')
        
        # Basic checks
        print(f"\n1. Basic Information:")
        print(f"   Total rows: {len(df)}")
        print(f"   Total columns: {len(df.columns)}")
        print(f"   Expected rows: 100")
        print(f"   Expected columns: 40")
        
        # Missing values
        print(f"\n2. Missing Values:")
        missing = df.isnull().sum()
        if missing.sum() == 0:
            print("   No missing values found")
        else:
            print("   Missing values found:")
            for col, count in missing[missing > 0].items():
                print(f"     {col}: {count}")
        
        # Duplicate check
        print(f"\n3. Duplicate Check:")
        duplicates = df['customer_id'].duplicated().sum()
        if duplicates == 0:
            print("   No duplicate customer IDs")
        else:
            print(f"   Found {duplicates} duplicate customer IDs")
        
        # Data type check
        print(f"\n4. Data Types:")
        print(f"   Integer columns: {(df.dtypes == 'int64').sum()}")
        print(f"   Float columns: {(df.dtypes == 'float64').sum()}")
        print(f"   Object columns: {(df.dtypes == 'object').sum()}")
        
        # Range checks
        print(f"\n5. Data Ranges:")
        print(f"   Age: {df['age'].min()}-{df['age'].max()}")
        print(f"   Spending Score: {df['spending_score'].min()}-{df['spending_score'].max()}")
        print(f"   Annual Income: ${df['annual_income'].min():,.0f}-${df['annual_income'].max():,.0f}")
        
        # Negative values check
        print(f"\n6. Negative Values Check:")
        numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
        neg_cols = []
        for col in numeric_cols:
            if (df[col] < 0).any():
                neg_cols.append(col)
        if not neg_cols:
            print("   No negative values found (all good)")
        else:
            print(f"   Columns with negative values: {neg_cols}")
        
        # Required columns check
        print(f"\n7. Required Columns Check:")
        required_cols = [
            'customer_id', 'age', 'gender', 'annual_income', 'spending_score',
            'purchase_frequency', 'avg_order_value', 'total_purchases',
            'browsing_time_minutes', 'product_category_preference', 'device_type',
            'last_purchase_days', 'segment', 'customer_lifetime_value',
            'return_rate', 'payment_method', 'newsletter_subscribed',
            'social_media_engagement', 'avg_review_rating', 'cart_abandonment_rate',
            'discount_usage_pct', 'referral_source', 'customer_satisfaction_score',
            'preferred_shopping_hour', 'mobile_app_user', 'wishlist_items',
            'customer_since_months', 'loyalty_tier', 'email_open_rate',
            'click_through_rate', 'cross_category_purchases', 'repeat_purchase_rate',
            'avg_session_duration', 'pages_per_session', 'geographic_region',
            'preferred_shipping', 'support_interactions', 'product_reviews_count',
            'social_shares', 'coupon_redemptions'
        ]
        missing_cols = [col for col in required_cols if col not in df.columns]
        if not missing_cols:
            print("   All required columns present")
        else:
            print(f"   Missing columns: {missing_cols}")
        
        print("\n" + "="*60)
        print("DATASET QUALITY CHECK COMPLETE")
        print("="*60)
        
        return True
        
    except Exception as e:
        print(f"\nError: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_dataset()
    sys.exit(0 if success else 1)

