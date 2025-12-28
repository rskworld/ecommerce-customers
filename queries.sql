-- ============================================================================
-- E-commerce Customer Dataset - SQL Queries
-- ============================================================================
-- Author: RSK World
-- Website: https://rskworld.in
-- Email: help@rskworld.in
-- Phone: +91 93305 39277
-- ============================================================================

-- Create table structure (Enhanced with 40 features)
CREATE TABLE IF NOT EXISTS ecommerce_customers (
    customer_id INT PRIMARY KEY,
    age INT,
    gender VARCHAR(10),
    annual_income DECIMAL(10, 2),
    spending_score INT,
    purchase_frequency INT,
    avg_order_value DECIMAL(10, 2),
    total_purchases INT,
    browsing_time_minutes INT,
    product_category_preference VARCHAR(50),
    device_type VARCHAR(20),
    last_purchase_days INT,
    segment VARCHAR(20),
    customer_lifetime_value DECIMAL(10, 2),
    return_rate DECIMAL(5, 3),
    payment_method VARCHAR(50),
    newsletter_subscribed VARCHAR(3),
    social_media_engagement INT,
    avg_review_rating DECIMAL(3, 1),
    cart_abandonment_rate DECIMAL(5, 3),
    discount_usage_pct DECIMAL(5, 3),
    referral_source VARCHAR(50),
    customer_satisfaction_score DECIMAL(3, 1),
    preferred_shopping_hour INT,
    mobile_app_user VARCHAR(3),
    wishlist_items INT,
    customer_since_months INT,
    loyalty_tier VARCHAR(20),
    email_open_rate DECIMAL(5, 2),
    click_through_rate DECIMAL(5, 2),
    cross_category_purchases INT,
    repeat_purchase_rate DECIMAL(5, 2),
    avg_session_duration INT,
    pages_per_session INT,
    geographic_region VARCHAR(20),
    preferred_shipping VARCHAR(20),
    support_interactions INT,
    product_reviews_count INT,
    social_shares INT,
    coupon_redemptions INT
);

-- ============================================================================
-- BASIC QUERIES
-- ============================================================================

-- 1. Get all customers
SELECT * FROM ecommerce_customers;

-- 2. Count total customers
SELECT COUNT(*) AS total_customers FROM ecommerce_customers;

-- 3. Get customer statistics
SELECT 
    COUNT(*) AS total_customers,
    AVG(age) AS avg_age,
    AVG(annual_income) AS avg_annual_income,
    AVG(spending_score) AS avg_spending_score,
    AVG(purchase_frequency) AS avg_purchase_frequency,
    AVG(avg_order_value) AS avg_order_value,
    SUM(total_purchases) AS total_purchases_all_customers
FROM ecommerce_customers;

-- ============================================================================
-- SEGMENTATION QUERIES
-- ============================================================================

-- 4. Customer segment distribution
SELECT 
    segment,
    COUNT(*) AS customer_count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM ecommerce_customers), 2) AS percentage
FROM ecommerce_customers
GROUP BY segment
ORDER BY customer_count DESC;

-- 5. High value customers
SELECT 
    customer_id,
    age,
    gender,
    annual_income,
    spending_score,
    purchase_frequency,
    avg_order_value,
    product_category_preference
FROM ecommerce_customers
WHERE segment = 'High Value'
ORDER BY spending_score DESC;

-- 6. Segment statistics
SELECT 
    segment,
    COUNT(*) AS count,
    AVG(annual_income) AS avg_income,
    AVG(spending_score) AS avg_spending_score,
    AVG(purchase_frequency) AS avg_purchase_frequency,
    AVG(avg_order_value) AS avg_order_value,
    AVG(browsing_time_minutes) AS avg_browsing_time
FROM ecommerce_customers
GROUP BY segment
ORDER BY avg_spending_score DESC;

-- ============================================================================
-- GENDER ANALYSIS
-- ============================================================================

-- 7. Gender distribution
SELECT 
    gender,
    COUNT(*) AS count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM ecommerce_customers), 2) AS percentage,
    AVG(spending_score) AS avg_spending_score,
    AVG(purchase_frequency) AS avg_purchase_frequency,
    AVG(avg_order_value) AS avg_order_value
FROM ecommerce_customers
GROUP BY gender;

-- 8. Gender by segment
SELECT 
    gender,
    segment,
    COUNT(*) AS count,
    AVG(spending_score) AS avg_spending_score
FROM ecommerce_customers
GROUP BY gender, segment
ORDER BY gender, segment;

-- ============================================================================
-- PRODUCT PREFERENCE ANALYSIS
-- ============================================================================

-- 9. Product category preferences
SELECT 
    product_category_preference,
    COUNT(*) AS customer_count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM ecommerce_customers), 2) AS percentage,
    AVG(spending_score) AS avg_spending_score,
    AVG(purchase_frequency) AS avg_purchase_frequency,
    AVG(avg_order_value) AS avg_order_value
FROM ecommerce_customers
GROUP BY product_category_preference
ORDER BY customer_count DESC;

-- 10. Product category by segment
SELECT 
    product_category_preference,
    segment,
    COUNT(*) AS count,
    AVG(spending_score) AS avg_spending_score
FROM ecommerce_customers
GROUP BY product_category_preference, segment
ORDER BY product_category_preference, segment;

-- ============================================================================
-- DEVICE ANALYSIS
-- ============================================================================

-- 11. Device type distribution
SELECT 
    device_type,
    COUNT(*) AS customer_count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM ecommerce_customers), 2) AS percentage,
    AVG(browsing_time_minutes) AS avg_browsing_time,
    AVG(purchase_frequency) AS avg_purchase_frequency,
    AVG(spending_score) AS avg_spending_score
FROM ecommerce_customers
GROUP BY device_type
ORDER BY customer_count DESC;

-- 12. Device type by product category
SELECT 
    device_type,
    product_category_preference,
    COUNT(*) AS count,
    AVG(spending_score) AS avg_spending_score
FROM ecommerce_customers
GROUP BY device_type, product_category_preference
ORDER BY device_type, product_category_preference;

-- ============================================================================
-- AGE ANALYSIS
-- ============================================================================

-- 13. Age group analysis
SELECT 
    CASE 
        WHEN age < 25 THEN 'Young (0-24)'
        WHEN age < 35 THEN 'Adult (25-34)'
        WHEN age < 50 THEN 'Middle (35-49)'
        ELSE 'Senior (50+)'
    END AS age_group,
    COUNT(*) AS count,
    AVG(spending_score) AS avg_spending_score,
    AVG(purchase_frequency) AS avg_purchase_frequency,
    AVG(avg_order_value) AS avg_order_value
FROM ecommerce_customers
GROUP BY age_group
ORDER BY 
    CASE age_group
        WHEN 'Young (0-24)' THEN 1
        WHEN 'Adult (25-34)' THEN 2
        WHEN 'Middle (35-49)' THEN 3
        ELSE 4
    END;

-- 14. Age and income correlation
SELECT 
    CASE 
        WHEN age < 25 THEN 'Young (0-24)'
        WHEN age < 35 THEN 'Adult (25-34)'
        WHEN age < 50 THEN 'Middle (35-49)'
        ELSE 'Senior (50+)'
    END AS age_group,
    AVG(annual_income) AS avg_income,
    AVG(spending_score) AS avg_spending_score
FROM ecommerce_customers
GROUP BY age_group
ORDER BY avg_income DESC;

-- ============================================================================
-- PURCHASE BEHAVIOR ANALYSIS
-- ============================================================================

-- 15. Top customers by spending score
SELECT 
    customer_id,
    age,
    gender,
    annual_income,
    spending_score,
    purchase_frequency,
    avg_order_value,
    segment
FROM ecommerce_customers
ORDER BY spending_score DESC
LIMIT 10;

-- 16. Customers with high purchase frequency
SELECT 
    customer_id,
    age,
    gender,
    purchase_frequency,
    total_purchases,
    avg_order_value,
    spending_score,
    segment
FROM ecommerce_customers
WHERE purchase_frequency >= 15
ORDER BY purchase_frequency DESC;

-- 17. Recent purchasers (last 7 days)
SELECT 
    customer_id,
    age,
    gender,
    last_purchase_days,
    spending_score,
    purchase_frequency,
    segment
FROM ecommerce_customers
WHERE last_purchase_days <= 7
ORDER BY last_purchase_days ASC;

-- 18. Customers with high average order value
SELECT 
    customer_id,
    age,
    gender,
    avg_order_value,
    purchase_frequency,
    total_purchases,
    annual_income,
    segment
FROM ecommerce_customers
WHERE avg_order_value >= 200
ORDER BY avg_order_value DESC;

-- ============================================================================
-- BROWSING BEHAVIOR ANALYSIS
-- ============================================================================

-- 19. Browsing time analysis
SELECT 
    CASE 
        WHEN browsing_time_minutes < 30 THEN 'Low (< 30 min)'
        WHEN browsing_time_minutes < 100 THEN 'Medium (30-99 min)'
        WHEN browsing_time_minutes < 200 THEN 'High (100-199 min)'
        ELSE 'Very High (200+ min)'
    END AS browsing_category,
    COUNT(*) AS count,
    AVG(spending_score) AS avg_spending_score,
    AVG(purchase_frequency) AS avg_purchase_frequency
FROM ecommerce_customers
GROUP BY browsing_category
ORDER BY 
    CASE browsing_category
        WHEN 'Low (< 30 min)' THEN 1
        WHEN 'Medium (30-99 min)' THEN 2
        WHEN 'High (100-199 min)' THEN 3
        ELSE 4
    END;

-- 20. Browsing time vs purchase frequency correlation
SELECT 
    device_type,
    AVG(browsing_time_minutes) AS avg_browsing_time,
    AVG(purchase_frequency) AS avg_purchase_frequency,
    AVG(spending_score) AS avg_spending_score
FROM ecommerce_customers
GROUP BY device_type
ORDER BY avg_browsing_time DESC;

-- ============================================================================
-- ADVANCED ANALYTICAL QUERIES
-- ============================================================================

-- 21. Customer lifetime value estimation
SELECT 
    segment,
    COUNT(*) AS customer_count,
    AVG(avg_order_value * purchase_frequency) AS estimated_clv,
    SUM(avg_order_value * purchase_frequency) AS total_clv
FROM ecommerce_customers
GROUP BY segment
ORDER BY estimated_clv DESC;

-- 22. Income vs spending analysis
SELECT 
    CASE 
        WHEN annual_income < 20000 THEN 'Low Income (< 20k)'
        WHEN annual_income < 30000 THEN 'Medium Income (20k-29k)'
        WHEN annual_income < 40000 THEN 'High Income (30k-39k)'
        ELSE 'Very High Income (40k+)'
    END AS income_category,
    COUNT(*) AS count,
    AVG(spending_score) AS avg_spending_score,
    AVG(purchase_frequency) AS avg_purchase_frequency,
    AVG(avg_order_value) AS avg_order_value
FROM ecommerce_customers
GROUP BY income_category
ORDER BY 
    CASE income_category
        WHEN 'Low Income (< 20k)' THEN 1
        WHEN 'Medium Income (20k-29k)' THEN 2
        WHEN 'High Income (30k-39k)' THEN 3
        ELSE 4
    END;

-- 23. Comprehensive customer profile
SELECT 
    segment,
    gender,
    product_category_preference,
    device_type,
    COUNT(*) AS count,
    AVG(age) AS avg_age,
    AVG(annual_income) AS avg_income,
    AVG(spending_score) AS avg_spending_score,
    AVG(purchase_frequency) AS avg_purchase_frequency,
    AVG(avg_order_value) AS avg_order_value,
    AVG(browsing_time_minutes) AS avg_browsing_time
FROM ecommerce_customers
GROUP BY segment, gender, product_category_preference, device_type
ORDER BY segment, count DESC;

-- 24. Churn risk analysis (customers with long time since last purchase)
SELECT 
    customer_id,
    age,
    gender,
    last_purchase_days,
    purchase_frequency,
    spending_score,
    segment,
    CASE 
        WHEN last_purchase_days > 45 THEN 'High Risk'
        WHEN last_purchase_days > 30 THEN 'Medium Risk'
        ELSE 'Low Risk'
    END AS churn_risk
FROM ecommerce_customers
ORDER BY last_purchase_days DESC;

-- 25. Product recommendation candidates (high spending, low frequency in category)
SELECT 
    customer_id,
    age,
    gender,
    product_category_preference,
    purchase_frequency,
    spending_score,
    avg_order_value,
    segment
FROM ecommerce_customers
WHERE spending_score > 70 
  AND purchase_frequency < 10
ORDER BY spending_score DESC;

-- ============================================================================
-- ENHANCED FEATURES QUERIES
-- ============================================================================

-- 26. Customer Lifetime Value Analysis
SELECT 
    segment,
    COUNT(*) AS customer_count,
    AVG(customer_lifetime_value) AS avg_clv,
    SUM(customer_lifetime_value) AS total_clv,
    MAX(customer_lifetime_value) AS max_clv,
    MIN(customer_lifetime_value) AS min_clv
FROM ecommerce_customers
GROUP BY segment
ORDER BY avg_clv DESC;

-- 27. Payment Method Preferences
SELECT 
    payment_method,
    COUNT(*) AS customer_count,
    AVG(avg_order_value) AS avg_order_value,
    AVG(spending_score) AS avg_spending_score,
    AVG(customer_lifetime_value) AS avg_clv
FROM ecommerce_customers
GROUP BY payment_method
ORDER BY customer_count DESC;

-- 28. Loyalty Tier Analysis
SELECT 
    loyalty_tier,
    COUNT(*) AS customer_count,
    AVG(customer_lifetime_value) AS avg_clv,
    AVG(repeat_purchase_rate) AS avg_repeat_rate,
    AVG(spending_score) AS avg_spending_score,
    AVG(customer_since_months) AS avg_tenure_months
FROM ecommerce_customers
GROUP BY loyalty_tier
ORDER BY 
    CASE loyalty_tier
        WHEN 'Diamond' THEN 1
        WHEN 'Platinum' THEN 2
        WHEN 'Gold' THEN 3
        WHEN 'Silver' THEN 4
        WHEN 'Bronze' THEN 5
    END;

-- 29. Newsletter Subscription Impact
SELECT 
    newsletter_subscribed,
    COUNT(*) AS customer_count,
    AVG(email_open_rate) AS avg_open_rate,
    AVG(click_through_rate) AS avg_ctr,
    AVG(spending_score) AS avg_spending_score,
    AVG(purchase_frequency) AS avg_purchase_frequency,
    AVG(customer_lifetime_value) AS avg_clv
FROM ecommerce_customers
GROUP BY newsletter_subscribed;

-- 30. Social Media Engagement Analysis
SELECT 
    segment,
    AVG(social_media_engagement) AS avg_engagement,
    AVG(social_shares) AS avg_shares,
    AVG(spending_score) AS avg_spending_score,
    COUNT(*) AS customer_count
FROM ecommerce_customers
GROUP BY segment
ORDER BY avg_engagement DESC;

-- 31. Customer Satisfaction by Segment
SELECT 
    segment,
    AVG(customer_satisfaction_score) AS avg_satisfaction,
    AVG(avg_review_rating) AS avg_review_rating,
    AVG(product_reviews_count) AS avg_reviews_count,
    COUNT(*) AS customer_count
FROM ecommerce_customers
GROUP BY segment
ORDER BY avg_satisfaction DESC;

-- 32. Geographic Region Analysis
SELECT 
    geographic_region,
    COUNT(*) AS customer_count,
    AVG(spending_score) AS avg_spending_score,
    AVG(customer_lifetime_value) AS avg_clv,
    AVG(purchase_frequency) AS avg_purchase_frequency,
    AVG(annual_income) AS avg_income
FROM ecommerce_customers
GROUP BY geographic_region
ORDER BY avg_clv DESC;

-- 33. Referral Source Performance
SELECT 
    referral_source,
    COUNT(*) AS customer_count,
    AVG(spending_score) AS avg_spending_score,
    AVG(customer_lifetime_value) AS avg_clv,
    AVG(customer_satisfaction_score) AS avg_satisfaction,
    AVG(repeat_purchase_rate) AS avg_repeat_rate
FROM ecommerce_customers
GROUP BY referral_source
ORDER BY avg_clv DESC;

-- 34. Mobile App Users Analysis
SELECT 
    mobile_app_user,
    COUNT(*) AS customer_count,
    AVG(spending_score) AS avg_spending_score,
    AVG(purchase_frequency) AS avg_purchase_frequency,
    AVG(browsing_time_minutes) AS avg_browsing_time,
    AVG(customer_lifetime_value) AS avg_clv
FROM ecommerce_customers
GROUP BY mobile_app_user;

-- 35. Cart Abandonment Analysis
SELECT 
    segment,
    AVG(cart_abandonment_rate) AS avg_abandonment_rate,
    AVG(spending_score) AS avg_spending_score,
    AVG(purchase_frequency) AS avg_purchase_frequency,
    COUNT(*) AS customer_count
FROM ecommerce_customers
GROUP BY segment
ORDER BY avg_abandonment_rate DESC;

-- 36. Discount Usage Patterns
SELECT 
    segment,
    AVG(discount_usage_pct) AS avg_discount_usage,
    AVG(coupon_redemptions) AS avg_coupon_redemptions,
    AVG(spending_score) AS avg_spending_score,
    AVG(avg_order_value) AS avg_order_value
FROM ecommerce_customers
GROUP BY segment
ORDER BY avg_discount_usage DESC;

-- 37. Return Rate Analysis
SELECT 
    segment,
    AVG(return_rate) AS avg_return_rate,
    AVG(customer_satisfaction_score) AS avg_satisfaction,
    AVG(avg_review_rating) AS avg_review_rating,
    COUNT(*) AS customer_count
FROM ecommerce_customers
GROUP BY segment
ORDER BY avg_return_rate DESC;

-- 38. Preferred Shopping Hours
SELECT 
    preferred_shopping_hour,
    COUNT(*) AS customer_count,
    AVG(spending_score) AS avg_spending_score,
    AVG(purchase_frequency) AS avg_purchase_frequency
FROM ecommerce_customers
GROUP BY preferred_shopping_hour
ORDER BY preferred_shopping_hour;

-- 39. Wishlist Analysis
SELECT 
    segment,
    AVG(wishlist_items) AS avg_wishlist_items,
    AVG(spending_score) AS avg_spending_score,
    AVG(purchase_frequency) AS avg_purchase_frequency,
    COUNT(*) AS customer_count
FROM ecommerce_customers
GROUP BY segment
ORDER BY avg_wishlist_items DESC;

-- 40. Cross-Category Purchase Analysis
SELECT 
    cross_category_purchases,
    COUNT(*) AS customer_count,
    AVG(spending_score) AS avg_spending_score,
    AVG(customer_lifetime_value) AS avg_clv,
    AVG(purchase_frequency) AS avg_purchase_frequency
FROM ecommerce_customers
GROUP BY cross_category_purchases
ORDER BY cross_category_purchases DESC;

-- 41. Customer Support Interactions
SELECT 
    segment,
    AVG(support_interactions) AS avg_support_interactions,
    AVG(customer_satisfaction_score) AS avg_satisfaction,
    AVG(return_rate) AS avg_return_rate,
    COUNT(*) AS customer_count
FROM ecommerce_customers
GROUP BY segment
ORDER BY avg_support_interactions DESC;

-- 42. Shipping Preference Analysis
SELECT 
    preferred_shipping,
    COUNT(*) AS customer_count,
    AVG(avg_order_value) AS avg_order_value,
    AVG(spending_score) AS avg_spending_score,
    AVG(customer_lifetime_value) AS avg_clv
FROM ecommerce_customers
GROUP BY preferred_shipping
ORDER BY customer_count DESC;

-- 43. Session Behavior Analysis
SELECT 
    segment,
    AVG(avg_session_duration) AS avg_session_duration_seconds,
    AVG(pages_per_session) AS avg_pages_per_session,
    AVG(browsing_time_minutes) AS avg_browsing_time_minutes,
    AVG(spending_score) AS avg_spending_score
FROM ecommerce_customers
GROUP BY segment
ORDER BY avg_session_duration_seconds DESC;

-- 44. Repeat Purchase Rate Analysis
SELECT 
    segment,
    AVG(repeat_purchase_rate) AS avg_repeat_rate,
    AVG(customer_since_months) AS avg_tenure_months,
    AVG(customer_lifetime_value) AS avg_clv,
    COUNT(*) AS customer_count
FROM ecommerce_customers
GROUP BY segment
ORDER BY avg_repeat_rate DESC;

-- 45. Comprehensive Customer Profile (Enhanced)
SELECT 
    segment,
    loyalty_tier,
    payment_method,
    geographic_region,
    COUNT(*) AS customer_count,
    AVG(age) AS avg_age,
    AVG(annual_income) AS avg_income,
    AVG(spending_score) AS avg_spending_score,
    AVG(customer_lifetime_value) AS avg_clv,
    AVG(customer_satisfaction_score) AS avg_satisfaction,
    AVG(repeat_purchase_rate) AS avg_repeat_rate
FROM ecommerce_customers
GROUP BY segment, loyalty_tier, payment_method, geographic_region
ORDER BY segment, avg_clv DESC;

-- 46. High-Value Customer Characteristics
SELECT 
    customer_id,
    age,
    gender,
    loyalty_tier,
    customer_lifetime_value,
    spending_score,
    repeat_purchase_rate,
    customer_satisfaction_score,
    newsletter_subscribed,
    mobile_app_user,
    cross_category_purchases
FROM ecommerce_customers
WHERE segment = 'High Value'
ORDER BY customer_lifetime_value DESC
LIMIT 20;

-- 47. Email Marketing Effectiveness
SELECT 
    newsletter_subscribed,
    AVG(email_open_rate) AS avg_open_rate,
    AVG(click_through_rate) AS avg_ctr,
    AVG(purchase_frequency) AS avg_purchase_frequency,
    AVG(spending_score) AS avg_spending_score,
    COUNT(*) AS customer_count
FROM ecommerce_customers
WHERE newsletter_subscribed = 'Yes'
GROUP BY newsletter_subscribed;

-- 48. Customer Retention Metrics
SELECT 
    segment,
    AVG(customer_since_months) AS avg_tenure_months,
    AVG(repeat_purchase_rate) AS avg_repeat_rate,
    AVG(last_purchase_days) AS avg_days_since_purchase,
    COUNT(*) AS customer_count
FROM ecommerce_customers
GROUP BY segment
ORDER BY avg_tenure_months DESC;

-- 49. Product Review Engagement
SELECT 
    segment,
    AVG(product_reviews_count) AS avg_reviews_count,
    AVG(avg_review_rating) AS avg_review_rating,
    AVG(customer_satisfaction_score) AS avg_satisfaction,
    COUNT(*) AS customer_count
FROM ecommerce_customers
GROUP BY segment
ORDER BY avg_reviews_count DESC;

-- 50. Top Performers by Multiple Metrics
SELECT 
    customer_id,
    segment,
    customer_lifetime_value,
    spending_score,
    repeat_purchase_rate,
    customer_satisfaction_score,
    social_media_engagement,
    product_reviews_count,
    loyalty_tier
FROM ecommerce_customers
WHERE customer_lifetime_value > (SELECT AVG(customer_lifetime_value) FROM ecommerce_customers)
  AND spending_score > 70
  AND repeat_purchase_rate > 0.7
ORDER BY customer_lifetime_value DESC;

