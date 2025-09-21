import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Generate synthetic sales data
def generate_sales_data(n_records=5000):
    # Date range: Last 2 years
    start_date = datetime.now() - timedelta(days=730)
    end_date = datetime.now()
    
    # Product categories and names
    categories = ['Electronics', 'Clothing', 'Home & Garden', 'Sports', 'Books', 'Beauty']
    products = {
        'Electronics': ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Camera', 'TV'],
        'Clothing': ['T-Shirt', 'Jeans', 'Dress', 'Jacket', 'Shoes', 'Hat'],
        'Home & Garden': ['Sofa', 'Table', 'Lamp', 'Plant', 'Cookware', 'Bedding'],
        'Sports': ['Running Shoes', 'Yoga Mat', 'Dumbbells', 'Tennis Racket', 'Basketball', 'Bicycle'],
        'Books': ['Fiction Novel', 'Cookbook', 'Biography', 'Self-Help', 'Textbook', 'Children Book'],
        'Beauty': ['Lipstick', 'Foundation', 'Shampoo', 'Perfume', 'Moisturizer', 'Nail Polish']
    }
    
    # Regions and cities
    regions = ['North', 'South', 'East', 'West', 'Central']
    cities = {
        'North': ['New York', 'Boston', 'Chicago'],
        'South': ['Miami', 'Atlanta', 'Houston'],
        'East': ['Philadelphia', 'Washington DC', 'Baltimore'],
        'West': ['Los Angeles', 'San Francisco', 'Seattle'],
        'Central': ['Denver', 'Kansas City', 'Minneapolis']
    }
    
    # Customer segments
    segments = ['Consumer', 'Corporate', 'Home Office']
    
    # Sales channels
    channels = ['Online', 'Store', 'Phone']
    
    # Generate data
    data = []
    
    for i in range(n_records):
        # Random date
        random_days = random.randint(0, 730)
        order_date = start_date + timedelta(days=random_days)
        
        # Random region and city
        region = random.choice(regions)
        city = random.choice(cities[region])
        
        # Random category and product
        category = random.choice(categories)
        product = random.choice(products[category])
        
        # Random customer info
        customer_id = f"CUST_{random.randint(1000, 9999)}"
        segment = random.choice(segments)
        
        # Random sales info
        channel = random.choice(channels)
        quantity = random.randint(1, 10)
        
        # Price based on category (with some randomness)
        base_prices = {
            'Electronics': 500, 'Clothing': 50, 'Home & Garden': 200,
            'Sports': 100, 'Books': 20, 'Beauty': 30
        }
        base_price = base_prices[category]
        unit_price = base_price * random.uniform(0.5, 2.0)
        
        # Calculate totals
        sales = quantity * unit_price
        profit_margin = random.uniform(0.1, 0.4)  # 10-40% profit margin
        profit = sales * profit_margin
        
        # Discount (sometimes)
        discount = random.uniform(0, 0.3) if random.random() < 0.3 else 0
        sales_after_discount = sales * (1 - discount)
        profit_after_discount = profit * (1 - discount)
        
        data.append({
            'Order_ID': f"ORD_{i+1:05d}",
            'Order_Date': order_date.strftime('%Y-%m-%d'),
            'Customer_ID': customer_id,
            'Customer_Segment': segment,
            'Region': region,
            'City': city,
            'Category': category,
            'Product_Name': product,
            'Sales_Channel': channel,
            'Quantity': quantity,
            'Unit_Price': round(unit_price, 2),
            'Sales': round(sales_after_discount, 2),
            'Profit': round(profit_after_discount, 2),
            'Discount': round(discount, 3),
            'Profit_Margin': round(profit_after_discount / sales_after_discount, 3) if sales_after_discount > 0 else 0
        })
    
    return pd.DataFrame(data)

# Generate and save the dataset
if __name__ == "__main__":
    df = generate_sales_data(5000)
    df.to_csv('sales_data.csv', index=False)
    print(f"Generated sales dataset with {len(df)} records")
    print("\nDataset preview:")
    print(df.head())
    print("\nDataset info:")
    print(df.info())
