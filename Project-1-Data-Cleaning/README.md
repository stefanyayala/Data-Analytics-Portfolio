# Data Cleaning and Merging for Steam Data Project

## Overview

This project demonstrates a full pipeline for cleaning and merging datasets to analyze Steam game data. It follows a structured process to handle multiple data sources, clean the data, perform transformations, and output the results for analysis. The pipeline consists of three key steps:

1. **Exploratory Data Analysis and Merging**
2. **Data Cleaning and Transformation**
3. **Final Data Preparation**

The project is built to handle real-world data challenges, such as missing values, inconsistent formats, and redundant information. The final dataset provides a clean and enriched view of the Steam game data, ready for further analysis and business intelligence insights.

## Project Flow

### Step 1: **Exploratory Analysis and Merging**

The first step involves analyzing two source datasets, `steam_data.csv` and `text_content.csv`, by inspecting their structure, cleaning, and merging them based on common columns. This step identifies key columns, drops unnecessary or redundant data, and prepares both datasets for a more detailed merge based on unique identifiers (e.g., the `url` column).

**Key Tasks:**
- Load the data from two CSV files.
- Perform exploratory analysis, such as checking for missing values and data types.
- Compare common columns between the two datasets.
- Merge datasets based on a shared `url` column, ensuring data consistency and completeness.

### Step 2: **Data Cleaning and Transformation**

In this step, the merged data undergoes several transformations and cleaning operations to ensure it is ready for analysis:

**Key Transformations:**
- **Replace Invalid Dates:** All invalid date entries in the `all_reviews` column are replaced with `NaN`.
- **Clean URLs:** Tracking parameters from URLs are removed.
- **Split Categories and Tags:** Categories and tags are split into separate rows for better analysis.
- **Parse Reviews:** User reviews are parsed into sentiment, review counts, and percentages.
- **Standardize Dates:** The date format is standardized to `YYYY-MM-DD`.
- **Extract Price Information:** Prices are extracted and standardized, including marking free-to-play games as `0.0`.
- **Consolidate PEGI Ratings:** Multiple PEGI ratings are consolidated for each game.
- **Combine and Clean Descriptions:** Descriptions are combined and cleaned to ensure completeness.
- **Parse System Requirements:** Both minimum and recommended system requirements are parsed.
- **Handle Missing Values:** Any missing or invalid data is handled appropriately.
- **Select and Order Columns:** Final columns are selected and ordered for output.

### Step 3: **Final Data Preparation**

After all necessary transformations and clean-up tasks, the final dataset is saved. This cleaned dataset is now ready for any further analysis, reporting, or visualization.

**Key Actions:**
- Replace missing review data with a placeholder value.
- Drop rows with missing essential information (e.g., game names).
- Save the cleaned dataset to a CSV file for further use.

## Files

### 1. `exploratory_analysis.py`
- This script performs initial data analysis and merging between the two CSV files, ensuring data consistency before the cleaning process.

### 2. `data_merging.py`
- This script cleans and merges the data based on the `url` column, handling missing values, duplicates, and preparing the data for further transformations.

### 3. `data_cleaning.py`
- This script performs the bulk of the data transformation and cleaning operations, ensuring the final dataset is standardized, enriched, and ready for business intelligence insights.

## How to Run the Project

To run this project locally, ensure you have the following dependencies installed:
- Python 3.x
- pandas

Then, follow these steps:

1. Place your raw data files (`steam_data.csv`, `text_content.csv`) in the `files` directory.
2. Run the `exploratory_analysis.py` script to analyze and merge the data.
3. Run the `data_merging.py` script to clean and merge the datasets.
4. Run the `data_cleaning.py` script to clean, transform, and save the final dataset.

The final cleaned dataset will be saved as `cleaned_steam_data.csv` in the `files` folder.

## Conclusion

This project demonstrates a robust, efficient, and repeatable data pipeline for cleaning and preparing datasets in the business intelligence context. The cleaned and transformed dataset is now ready for analysis, reporting, and decision-making, providing key insights into Steam game data.
