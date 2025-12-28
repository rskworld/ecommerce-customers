# E-commerce Customer Dataset

<!--
Author: RSK World
Website: https://rskworld.in
Email: help@rskworld.in
Phone: +91 93305 39277
-->

## 📊 Dataset Overview

This dataset contains comprehensive e-commerce customer behavior data including purchase history, browsing patterns, product preferences, and customer segmentation labels. Perfect for customer segmentation, recommendation systems, and marketing analytics.

**Dataset Details:**
- **Total Customers:** 100
- **Features:** 40 (Enhanced Dataset)
- **Difficulty Level:** Intermediate
- **Category:** Tabular Data
- **Technologies:** CSV, SQL, Pandas, NumPy

## 🎯 Key Features

### Core Features
- ✅ **Purchase History** - Complete purchase records with frequency, order values, and totals
- ✅ **Browsing Patterns** - Detailed browsing behavior including time spent and device preferences
- ✅ **Product Preferences** - Customer preferences for different product categories (6 categories)
- ✅ **Customer Segments** - Pre-labeled segments (High Value, Medium Value, Low Value)
- ✅ **Ready for Clustering** - Optimized for machine learning and clustering models

### Enhanced Unique Features (27 Additional Features)
- ✅ **Customer Lifetime Value (CLV)** - Calculated CLV for each customer
- ✅ **Return Rate** - Product return rates per customer
- ✅ **Payment Methods** - 6 payment method preferences (Credit Card, Debit Card, PayPal, Digital Wallet, Bank Transfer, Cash on Delivery)
- ✅ **Newsletter Subscription** - Subscription status and email engagement
- ✅ **Social Media Engagement** - Engagement scores and social shares count
- ✅ **Average Review Rating** - Customer review ratings (1-5 scale)
- ✅ **Cart Abandonment Rate** - Shopping cart abandonment percentages
- ✅ **Discount Usage** - Discount usage percentage and coupon redemptions
- ✅ **Referral Sources** - 7 referral sources (Google Search, Social Media, Email Campaign, Direct, Referral, Advertisement, Influencer)
- ✅ **Customer Satisfaction Score** - Satisfaction scores (1-5 scale)
- ✅ **Preferred Shopping Hour** - Hour of day when customers prefer to shop
- ✅ **Mobile App User** - Mobile app usage identification
- ✅ **Wishlist Items** - Number of items in customer wishlists
- ✅ **Customer Since (Months)** - Customer tenure in months
- ✅ **Loyalty Tier** - 5-tier loyalty program (Bronze, Silver, Gold, Platinum, Diamond)
- ✅ **Email Open Rate** - Email marketing open rates
- ✅ **Click-Through Rate** - Email marketing CTR
- ✅ **Cross-Category Purchases** - Number of different categories purchased
- ✅ **Repeat Purchase Rate** - Customer repeat purchase percentage
- ✅ **Average Session Duration** - Time spent per session (seconds)
- ✅ **Pages Per Session** - Average pages viewed per session
- ✅ **Geographic Region** - 5 regions (North, South, East, West, Central)
- ✅ **Preferred Shipping** - Shipping method preferences (Standard, Express, Overnight, Same Day)
- ✅ **Support Interactions** - Number of customer support interactions
- ✅ **Product Reviews Count** - Number of product reviews written
- ✅ **Social Shares** - Number of social media shares
- ✅ **Coupon Redemptions** - Number of coupons redeemed

## 📁 Project Structure

```
ecommerce-customers/
│
├── ecommerce_customers.csv          # Enhanced dataset (40 features)
├── generate_enhanced_dataset.py     # Dataset generation script
├── analyze_customers.py             # Comprehensive data analysis script
├── customer_segmentation.py         # Advanced clustering analysis
├── visualize_data.py                # Data visualization script
├── queries.sql                      # 50 SQL queries for data analysis
├── index.html                       # Interactive demo page
├── requirements.txt                 # Python dependencies
└── README.md                        # This file
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### 2. Load the Dataset

```python
import pandas as pd

# Load the dataset
df = pd.read_csv('ecommerce_customers.csv')

# Display basic information
print(df.head())
print(df.info())
```

### 3. Run Analysis Scripts

**Basic Analysis:**
```bash
python analyze_customers.py
```

**Customer Segmentation:**
```bash
python customer_segmentation.py
```

### 4. SQL Queries

Import the dataset into your SQL database and run the queries from `queries.sql`:

```sql
-- Example: Get customer segment distribution
SELECT 
    segment,
    COUNT(*) AS customer_count,
    AVG(spending_score) AS avg_spending_score
FROM ecommerce_customers
GROUP BY segment;
```

## 📊 Dataset Schema (40 Features)

### Basic Information
| Column | Type | Description |
|--------|------|-------------|
| customer_id | INT | Unique customer identifier |
| age | INT | Customer age |
| gender | STRING | Customer gender (Male/Female) |
| annual_income | DECIMAL | Annual income in USD |
| spending_score | INT | Spending score (0-100) |

### Purchase Behavior
| Column | Type | Description |
|--------|------|-------------|
| purchase_frequency | INT | Number of purchases |
| avg_order_value | DECIMAL | Average order value in USD |
| total_purchases | INT | Total number of purchases |
| customer_lifetime_value | DECIMAL | Calculated CLV |
| repeat_purchase_rate | DECIMAL | Repeat purchase percentage |
| last_purchase_days | INT | Days since last purchase |

### Browsing & Engagement
| Column | Type | Description |
|--------|------|-------------|
| browsing_time_minutes | INT | Total browsing time in minutes |
| avg_session_duration | INT | Average session duration (seconds) |
| pages_per_session | INT | Average pages per session |
| preferred_shopping_hour | INT | Preferred shopping hour (0-23) |

### Product & Preferences
| Column | Type | Description |
|--------|------|-------------|
| product_category_preference | STRING | Preferred product category (6 categories) |
| device_type | STRING | Preferred device (Mobile/Desktop/Tablet) |
| cross_category_purchases | INT | Number of different categories purchased |
| wishlist_items | INT | Number of wishlist items |

### Customer Segmentation
| Column | Type | Description |
|--------|------|-------------|
| segment | STRING | Customer segment (High/Medium/Low Value) |
| loyalty_tier | STRING | Loyalty tier (Bronze/Silver/Gold/Platinum/Diamond) |
| customer_since_months | INT | Customer tenure in months |

### Payment & Transactions
| Column | Type | Description |
|--------|------|-------------|
| payment_method | STRING | Preferred payment method (6 types) |
| return_rate | DECIMAL | Product return rate |
| discount_usage_pct | DECIMAL | Discount usage percentage |
| coupon_redemptions | INT | Number of coupons redeemed |

### Marketing & Communication
| Column | Type | Description |
|--------|------|-------------|
| newsletter_subscribed | STRING | Newsletter subscription (Yes/No) |
| email_open_rate | DECIMAL | Email open rate (0-1) |
| click_through_rate | DECIMAL | Email CTR (0-1) |
| referral_source | STRING | Referral source (7 types) |
| social_media_engagement | INT | Social media engagement score |
| social_shares | INT | Number of social shares |

### Customer Experience
| Column | Type | Description |
|--------|------|-------------|
| customer_satisfaction_score | DECIMAL | Satisfaction score (1-5) |
| avg_review_rating | DECIMAL | Average review rating (1-5) |
| product_reviews_count | INT | Number of reviews written |
| cart_abandonment_rate | DECIMAL | Cart abandonment rate |
| support_interactions | INT | Customer support interactions |

### Geographic & Logistics
| Column | Type | Description |
|--------|------|-------------|
| geographic_region | STRING | Geographic region (5 regions) |
| preferred_shipping | STRING | Preferred shipping method (4 types) |

### Technology
| Column | Type | Description |
|--------|------|-------------|
| mobile_app_user | STRING | Mobile app user (Yes/No) |

## 🔍 Analysis Examples

### Customer Segmentation Analysis

```python
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load data
df = pd.read_csv('ecommerce_customers.csv')

# Prepare features
features = ['annual_income', 'spending_score', 'purchase_frequency']
X = df[features].values

# Standardize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# K-Means clustering
kmeans = KMeans(n_clusters=4, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)

# Analyze clusters
print(df.groupby('cluster')[features].mean())
```

### Purchase Behavior Analysis

```python
# Analyze by segment
segment_stats = df.groupby('segment').agg({
    'spending_score': 'mean',
    'purchase_frequency': 'mean',
    'avg_order_value': 'mean'
})
print(segment_stats)
```

### Product Preference Analysis

```python
# Product category preferences
category_stats = df.groupby('product_category_preference').agg({
    'customer_id': 'count',
    'spending_score': 'mean',
    'avg_order_value': 'mean'
})
print(category_stats)
```

## 📈 Use Cases

1. **Customer Segmentation** - Identify and group customers based on behavior
2. **Marketing Analytics** - Understand customer preferences and spending patterns
3. **Recommendation Systems** - Build product recommendation engines
4. **Churn Prediction** - Identify customers at risk of churning
5. **Customer Lifetime Value** - Calculate CLV for different segments
6. **Targeted Marketing** - Create personalized marketing campaigns

## 🛠️ Technologies Used

- **CSV** - Data storage format
- **SQL** - Database queries and analysis
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computations
- **Matplotlib/Seaborn** - Data visualization
- **Scikit-learn** - Machine learning algorithms

## 📝 SQL Queries Included

The `queries.sql` file contains **50 ready-to-use SQL queries** including:

- Basic queries (counts, statistics)
- Segmentation analysis
- Gender-based analysis
- Product preference analysis
- Device type analysis
- Age group analysis
- Purchase behavior analysis
- Browsing behavior analysis
- **Enhanced Features Queries (25 new queries):**
  - Customer Lifetime Value analysis
  - Payment method preferences
  - Loyalty tier analysis
  - Newsletter subscription impact
  - Social media engagement
  - Customer satisfaction metrics
  - Geographic region analysis
  - Referral source performance
  - Mobile app users analysis
  - Cart abandonment patterns
  - Discount usage analysis
  - Return rate analysis
  - Shopping hour preferences
  - Wishlist analysis
  - Cross-category purchases
  - Support interactions
  - Shipping preferences
  - Session behavior
  - Repeat purchase rates
  - Email marketing effectiveness
  - Customer retention metrics
  - Product review engagement
  - Top performers analysis

## 🎨 Demo Page

Open `index.html` in your browser to view an interactive demo page with:
- Dataset overview and statistics
- Feature descriptions
- Dataset preview
- Analysis script information
- Download links

## 📊 Sample Insights

### Basic Insights
- **High Value Customers:** ~40% of customers with average spending score > 75
- **Most Preferred Category:** Multiple categories (Clothing, Electronics, Home & Garden, etc.)
- **Device Preference:** Mobile devices are most popular
- **Purchase Frequency:** High-value customers average 15+ purchases
- **Browsing Time:** Correlates positively with purchase frequency

### Enhanced Insights
- **Customer Lifetime Value:** High-value customers have significantly higher CLV
- **Loyalty Tiers:** Diamond and Platinum tiers show highest engagement
- **Payment Methods:** Credit cards and digital wallets are most popular
- **Email Marketing:** Subscribers show 3x higher engagement rates
- **Social Media:** High engagement correlates with higher spending
- **Mobile App:** App users have higher purchase frequency
- **Geographic:** Regional variations in spending patterns
- **Satisfaction:** High satisfaction scores correlate with repeat purchases
- **Cart Abandonment:** Lower abandonment rates in high-value segment
- **Referral Sources:** Social media and influencers drive quality customers

## 🔗 Resources

- **Website:** [https://rskworld.in](https://rskworld.in)
- **Email:** help@rskworld.in
- **Phone:** +91 93305 39277

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Copyright (c) 2026 RSK World**

This dataset and associated code are provided for educational and research purposes.
You are free to use, modify, and distribute according to the MIT License terms.

## 🙏 Credits

**Author:** RSK World  
**Website:** https://rskworld.in  
**Email:** help@rskworld.in  
**Phone:** +91 93305 39277

---

**Note:** This dataset is designed for learning and practicing data science, machine learning, and marketing analytics. Feel free to modify and extend the analysis scripts according to your needs.

