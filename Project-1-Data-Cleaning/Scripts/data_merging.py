import os
import pandas as pd

def clean_and_merge(file1, file2, output_path):
    """
    Cleans and merges two CSV files based on the 'url' column.
    Outputs the merged dataset to a specified file.
    """
    try:
        # Read the first CSV
        print(f"Reading {file1}...")
        df1 = pd.read_csv(file1, dtype=str)
        print(f"First dataset loaded with shape: {df1.shape}")

        # Read the second CSV
        print(f"Reading {file2}...")
        df2 = pd.read_csv(file2, dtype=str)
        print(f"Second dataset loaded with shape: {df2.shape}")

        # Inspecting the datasets
        print("\nCleaning and inspecting the datasets...")

        # Drop rows with missing 'url' (essential for the join)
        df1 = df1.dropna(subset=['url'])
        df2 = df2.dropna(subset=['url'])

        # Drop duplicate 'url' entries if any
        df1 = df1.drop_duplicates(subset=['url'])
        df2 = df2.drop_duplicates(subset=['url'])

        # Merge the datasets on 'url'
        print("\nMerging datasets on 'url'...")
        merged_df = pd.merge(df1, df2, on="url", how="inner")
        print(f"Merged dataset shape: {merged_df.shape}")

        # Additional Cleaning: Handle missing values in merged data
        print("\nHandling missing values...")
        merged_df = merged_df.fillna("Unknown")  # Replace missing values with "Unknown" or any strategy

        # Save the merged dataset to a CSV file
        merged_df.to_csv(output_path, index=False)
        print(f"\nMerged dataset saved to {output_path}")

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    # Get the folder where the script is located
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Path to the 'files' folder
    files_directory = os.path.join(script_directory, "files")

    # Specify the paths to the two CSV files
    file1 = os.path.join(files_directory, "steam_data.csv")
    file2 = os.path.join(files_directory, "text_content.csv")
    output_file = os.path.join(files_directory, "merged_steam_data.csv")

    # Clean and merge the files
    clean_and_merge(file1, file2, output_file)
