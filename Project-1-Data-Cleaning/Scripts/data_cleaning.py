# Third Step
import os
import pandas as pd
import re
from urllib.parse import urlparse, urlunparse
from datetime import datetime

# Get the folder where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Path to the 'files' folder
files_directory = os.path.join(script_directory, "files")

# Path to the CSV file
csv_file_path = os.path.join(files_directory, "merged_steam_data.csv")

print(f"Loading dataset from {csv_file_path}...")
# Load the dataset into a pandas DataFrame
data = pd.read_csv(csv_file_path)
print(f"Initial dataset loaded with shape: {data.shape}")
print(data.head())

# 0. Replace all_reviews values with NaN where the value is a valid date
print("\nReplacing valid dates in all_reviews with NaN...")
data['all_reviews'] = data['all_reviews'].apply(lambda x: None if pd.to_datetime(x, errors='coerce') is not pd.NaT else x)
print(f"Data shape after replacing valid dates in all_reviews: {data.shape}")

# 1. Clean URLs (remove tracking parameters)
print("\nCleaning URLs...")
def clean_url(url):
    parsed = urlparse(url)
    return urlunparse(parsed._replace(query=""))

data['url'] = data['url'].apply(clean_url)
data['img_url'] = data['img_url'].apply(clean_url)
print("URLs cleaned.")
print(f"Data shape after cleaning URLs: {data.shape}")

# 2. Split Categories and Tags into separate rows
print("\nSplitting categories and popular tags...")
data['categories'] = data['categories'].str.split(" ")
data['popu_tags'] = data['popu_tags'].str.split(" ")
print("Categories and tags split into lists.")
print(f"Data shape after splitting categories and tags: {data.shape}")

# 3. Parse User Reviews
print("\nParsing user reviews...")
def parse_reviews_vectorized(series):
    sentiment_pattern = r"([A-Za-z\s]+)"  # This captures the sentiment part, e.g., 'Mixed', 'Mostly Positive', etc.
    reviews_pattern = r"\(([\d,]+)\)"  # This captures the review count, e.g., '2,234'
    percentage_pattern = r"(\d+)%"  # This captures the percentage, e.g., '65'

    sentiments = series.str.extract(sentiment_pattern, expand=False)
    reviews = series.str.extract(reviews_pattern, expand=False)
    reviews = reviews.str.replace(",", "").astype(float)  # Remove commas and convert to float
    percentages = series.str.extract(percentage_pattern, expand=False).astype(float)

    return sentiments, reviews, percentages

data["last30_sentiment"], data["last30_reviews"], data["last30_percentage"] = parse_reviews_vectorized(data["user_reviews"])
data["all_sentiment"], data["all_reviews"], data["all_percentage"] = parse_reviews_vectorized(data["all_reviews"])
print("User reviews parsed.")
print(f"Data shape after parsing user reviews: {data.shape}")

# 4. Standardize Date Format
print("\nStandardizing date format...")
data['date'] = pd.to_datetime(data['date'], errors='coerce').dt.strftime('%Y-%m-%d')
print("Dates standardized.")
print(f"Data shape after standardizing date format: {data.shape}")

# 5. Extract Price and Mark Free-to-Play Games
print("\nExtracting price and marking free-to-play games...")
def extract_price(price):
    if pd.isna(price):
        return None
    if 'Free' in price:
        return 0.0
    # Match prices with decimal points, dollar sign, or numbers followed by USD
    match = re.search(r"\$\d{1,3}(?:[.,]\d{3})*(?:[.,]\d+)?|\b\d{1,3}(?:[.,]\d{3})*(?:[.,]\d+)?(?=\s*USD|\s*$)", price)
    if match:
        # Replace '$' and commas with an empty string, ensure '.' is used for decimals
        cleaned_price = match.group().replace('$', '').replace(',', '').replace('.', '.', 1)
        return float(cleaned_price)
    return None

data['price'] = data['price'].apply(extract_price)
print("Prices extracted.")
print(f"Data shape after extracting prices: {data.shape}")

# 6. Consolidate PEGI Ratings
print("\nConsolidating PEGI ratings...")
data['pegi_rating'] = data['pegi'].str.split(",").apply(lambda x: [rating.strip() for rating in x] if isinstance(x, list) else None)
data.drop(columns=['pegi', 'pegi_url'], inplace=True)
print("PEGI ratings consolidated.")
print(f"Data shape after consolidating PEGI ratings: {data.shape}")

# 7. Combine and Clean Descriptions
print("\nCombining and cleaning descriptions...")
data['description'] = data['desc'].combine_first(data['full_desc']).str.strip()
data.drop(columns=['desc', 'full_desc'], inplace=True)
print("Descriptions cleaned and combined.")
print(f"Data shape after combining and cleaning descriptions: {data.shape}")

# 8. Parse System Requirements
print("\nParsing system requirements...")
minimum_pattern = re.compile(r"Minimum:(.+?)(Recommended|$)", re.DOTALL)
recommended_pattern = re.compile(r"Recommended:(.+)", re.DOTALL)

def parse_requirements_optimized(req):
    if pd.isna(req):
        return None, None
    minimum_match = minimum_pattern.search(req)
    recommended_match = recommended_pattern.search(req)
    minimum = minimum_match.group(1).strip() if minimum_match else None
    recommended = recommended_match.group(1).strip() if recommended_match else None
    return minimum, recommended

parsed_requirements = data['requirements'].dropna().map(parse_requirements_optimized)
data['min_requirements'] = parsed_requirements.apply(lambda x: x[0] if x else None)
data['rec_requirements'] = parsed_requirements.apply(lambda x: x[1] if x else None)
data.drop(columns=['requirements'], inplace=True)
print("System requirements parsed.")
print(f"Data shape after parsing system requirements: {data.shape}")

# 9. Handle Missing Values
print("\nHandling missing values...")
data.replace('-', None, inplace=True)
print("Missing values handled.")
print(f"Data shape after handling missing values: {data.shape}")

# 10. Select and Order Columns
print("\nSelecting and ordering columns for final output...")
ordered_columns = ['url', 'img_url', 'name', 'all_sentiment', 'all_reviews', 'all_percentage', 'last30_sentiment', 'last30_reviews',
                   'last30_percentage', 'date', 'price', 'description', 'min_requirements', 'rec_requirements']  # Adjust order as needed
data = data[ordered_columns]
print(f"Data shape after selecting and ordering columns: {data.shape}")

# 10.5 Replace specific values in rows
print("\nReplacing specific values in rows where the reviews are empty...")

# Columns to update
columns_to_update_last30 = ['all_sentiment', 'all_reviews', 'all_percentage', 'last30_sentiment', 'last30_reviews', 'last30_percentage']
columns_to_update_all = ['all_sentiment', 'all_reviews', 'all_percentage']

# Ensure columns are of object (string) type
data[columns_to_update_last30] = data[columns_to_update_last30].astype(str)
data[columns_to_update_all] = data[columns_to_update_all].astype(str)

# Replace values with empty data
data.loc[data['last30_sentiment'].str.contains('user reviews', na=False, case=False), columns_to_update_last30] = "No user reviews"
data.loc[data['all_reviews'].str.contains('nan', na=False, case=False), columns_to_update_all] = "No user reviews"

print("Specific values replaced.")
print(f"Data shape after replacing specific values: {data.shape}")

# 11. Drop rows with NaN values
print("\nDropping rows with NaN values...")
data.dropna(subset=['name'], inplace=True)  # Adding inplace=True
print(data['all_sentiment'].unique())

# Save the cleaned dataset
print("\nSaving file...")
cleaned_file_path = os.path.join(files_directory, "cleaned_steam_data.csv")
data.to_csv(cleaned_file_path, index=False)
print(f"\nData cleaning complete. Saved to '{cleaned_file_path}'.")
