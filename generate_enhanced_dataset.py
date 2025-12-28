"""
Generate Enhanced E-commerce Customer Dataset
Author: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
"""

import csv
import random

random.seed(42)

# Define feature values
payment_methods = ['Credit Card', 'Debit Card', 'PayPal', 'Digital Wallet', 'Bank Transfer', 'Cash on Delivery']
referral_sources = ['Google Search', 'Social Media', 'Email Campaign', 'Direct', 'Referral', 'Advertisement', 'Influencer']
geographic_regions = ['North', 'South', 'East', 'West', 'Central']
shipping_methods = ['Standard', 'Express', 'Overnight', 'Same Day']
loyalty_tiers = ['Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond']
product_categories = ['Electronics', 'Clothing', 'Home & Garden', 'Sports', 'Books', 'Beauty']
device_types = ['Mobile', 'Desktop', 'Tablet']
genders = ['Male', 'Female']
segments = ['High Value', 'Medium Value', 'Low Value']

# Generate enhanced dataset
data = []
for i in range(1, 101):
    customer_id = i
    age = random.randint(18, 70)
    gender = random.choice(genders)
    annual_income = random.randint(15000, 50000)
    
    # Segment-based logic
    if i <= 40:
        segment = 'High Value'
        spending_score = random.randint(70, 100)
        purchase_frequency = random.randint(12, 20)
        avg_order_value = random.uniform(85, 115)
        total_purchases = purchase_frequency
        browsing_time = random.randint(140, 240)
        last_purchase_days = random.randint(1, 7)
        return_rate = random.uniform(0.02, 0.08)
        cart_abandonment = random.uniform(0.15, 0.30)
        discount_usage = random.uniform(0.20, 0.40)
        customer_satisfaction = random.uniform(4.2, 5.0)
        repeat_purchase_rate = random.uniform(0.75, 0.95)
        loyalty_tier = random.choice(['Gold', 'Platinum', 'Diamond'])
        customer_since = random.randint(18, 36)
    elif i <= 70:
        segment = 'Medium Value'
        spending_score = random.randint(30, 50)
        purchase_frequency = random.randint(6, 11)
        avg_order_value = random.uniform(125, 200)
        total_purchases = purchase_frequency
        browsing_time = random.randint(50, 100)
        last_purchase_days = random.randint(10, 30)
        return_rate = random.uniform(0.05, 0.12)
        cart_abandonment = random.uniform(0.30, 0.50)
        discount_usage = random.uniform(0.40, 0.60)
        customer_satisfaction = random.uniform(3.5, 4.5)
        repeat_purchase_rate = random.uniform(0.50, 0.75)
        loyalty_tier = random.choice(['Silver', 'Gold'])
        customer_since = random.randint(6, 18)
    else:
        segment = 'Low Value'
        spending_score = random.randint(3, 20)
        purchase_frequency = random.randint(1, 5)
        avg_order_value = random.uniform(200, 450)
        total_purchases = purchase_frequency
        browsing_time = random.randint(5, 50)
        last_purchase_days = random.randint(35, 85)
        return_rate = random.uniform(0.10, 0.25)
        cart_abandonment = random.uniform(0.50, 0.75)
        discount_usage = random.uniform(0.60, 0.85)
        customer_satisfaction = random.uniform(2.5, 3.8)
        repeat_purchase_rate = random.uniform(0.20, 0.50)
        loyalty_tier = random.choice(['Bronze', 'Silver'])
        customer_since = random.randint(1, 12)
    
    # Common features
    product_category = random.choice(product_categories)
    device_type = random.choice(device_types)
    
    # Calculate CLV
    clv = round(avg_order_value * purchase_frequency * (customer_since / 12), 2)
    
    # Additional unique features
    payment_method = random.choice(payment_methods)
    newsletter_subscribed = random.choice(['Yes', 'No'])
    social_media_engagement = random.randint(10, 100) if newsletter_subscribed == 'Yes' else random.randint(0, 30)
    avg_review_rating = round(random.uniform(2.5, 5.0), 1)
    referral_source = random.choice(referral_sources)
    preferred_shopping_hour = random.randint(8, 22)
    mobile_app_user = 'Yes' if device_type == 'Mobile' and random.random() > 0.3 else 'No'
    wishlist_items = random.randint(0, 25) if segment == 'High Value' else random.randint(0, 10)
    email_open_rate = round(random.uniform(0.15, 0.65), 2) if newsletter_subscribed == 'Yes' else round(random.uniform(0.0, 0.20), 2)
    click_through_rate = round(email_open_rate * random.uniform(0.2, 0.5), 2)
    cross_category_purchases = random.randint(1, 4) if segment == 'High Value' else random.randint(0, 2)
    avg_session_duration = random.randint(180, 1200)  # seconds
    pages_per_session = random.randint(3, 15)
    geographic_region = random.choice(geographic_regions)
    preferred_shipping = random.choice(shipping_methods)
    support_interactions = random.randint(0, 5) if segment == 'Low Value' else random.randint(0, 2)
    product_reviews_count = random.randint(0, 15) if segment == 'High Value' else random.randint(0, 5)
    social_shares = random.randint(0, 20) if social_media_engagement > 50 else random.randint(0, 5)
    coupon_redemptions = random.randint(0, 8) if discount_usage > 0.5 else random.randint(0, 3)
    
    row = [
        customer_id, age, gender, annual_income, spending_score,
        purchase_frequency, round(avg_order_value, 2), total_purchases,
        browsing_time, product_category, device_type, last_purchase_days, segment,
        clv, round(return_rate, 3), payment_method, newsletter_subscribed,
        social_media_engagement, avg_review_rating, round(cart_abandonment, 3),
        round(discount_usage, 3), referral_source, round(customer_satisfaction, 1),
        preferred_shopping_hour, mobile_app_user, wishlist_items,
        customer_since, loyalty_tier, round(email_open_rate, 2),
        round(click_through_rate, 2), cross_category_purchases,
        round(repeat_purchase_rate, 2), avg_session_duration, pages_per_session,
        geographic_region, preferred_shipping, support_interactions,
        product_reviews_count, social_shares, coupon_redemptions
    ]
    data.append(row)

# Write to CSV
headers = [
    'customer_id', 'age', 'gender', 'annual_income', 'spending_score',
    'purchase_frequency', 'avg_order_value', 'total_purchases',
    'browsing_time_minutes', 'product_category_preference', 'device_type',
    'last_purchase_days', 'segment', 'customer_lifetime_value', 'return_rate',
    'payment_method', 'newsletter_subscribed', 'social_media_engagement',
    'avg_review_rating', 'cart_abandonment_rate', 'discount_usage_pct',
    'referral_source', 'customer_satisfaction_score', 'preferred_shopping_hour',
    'mobile_app_user', 'wishlist_items', 'customer_since_months', 'loyalty_tier',
    'email_open_rate', 'click_through_rate', 'cross_category_purchases',
    'repeat_purchase_rate', 'avg_session_duration', 'pages_per_session',
    'geographic_region', 'preferred_shipping', 'support_interactions',
    'product_reviews_count', 'social_shares', 'coupon_redemptions'
]

with open('ecommerce_customers.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(data)

print(f"Enhanced dataset generated with {len(headers)} features and {len(data)} customers")

