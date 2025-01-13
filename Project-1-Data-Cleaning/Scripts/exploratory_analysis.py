import os
import pandas as pd

def read_and_clean_data(file_path):
    """
    Reads a .dat file and performs initial cleaning.
    Adjust this function as needed to match the structure of your .dat files.
    """
    try:
        # Read the file into a DataFrame
        df = pd.read_csv(file_path, delimiter="\t", dtype=str)  # Adjust delimiter if needed
        # Clean column names (example: stripping whitespace)
        df.columns = df.columns.str.strip()
        return df
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def process_directory_common_columns(directory_path):
    """
    Process all .dat files in a directory, joining only on common columns.
    """
    common_columns = None
    all_data = []

    # First pass: Identify common columns
    for filename in os.listdir(directory_path):
        if filename.endswith('.dat'):
            file_path = os.path.join(directory_path, filename)
            print(f"Inspecting columns in {file_path}...")
            df = read_and_clean_data(file_path)
            if df is not None and not df.empty:
                if common_columns is None:
                    common_columns = set(df.columns)  # Initialize with columns from the first file
                else:
                    common_columns.intersection_update(df.columns)  # Keep only common columns
            else:
                print(f"{filename} was skipped due to empty or invalid data.")

    if not common_columns:
        print("\nNo common columns found across all files.")
        return None

    print(f"\nIdentified {len(common_columns)} common columns.")

    # Convert to a sorted list for consistent ordering
    common_columns = sorted(common_columns)

    # Second pass: Load data with only common columns
    for filename in os.listdir(directory_path):
        if filename.endswith('.dat'):
            file_path = os.path.join(directory_path, filename)
            print(f"Processing {file_path}...")

            df = read_and_clean_data(file_path)
            if df is not None and not df.empty:
                # Keep only the common columns
                df = df[common_columns]
                all_data.append(df)
                print(f"{filename} loaded with shape: {df.shape}")
            else:
                print(f"{filename} was skipped due to empty or invalid data.")

    # Combine all DataFrames into one
    if all_data:
        combined_data = pd.concat(all_data, ignore_index=True)
        print(f"\nAll files combined successfully. Combined DataFrame shape: {combined_data.shape}")
        return combined_data
    else:
        print("\nNo valid data to combine.")
        return None

import pandas as pd

def analyze_csv(file_path):
    """
    Analyzes the structure and content of a CSV file.
    """
    try:
        print(f"\nAnalyzing {file_path}...")
        df = pd.read_csv(file_path, dtype=str)

        # Overview of the dataset
        print(f"Shape of the dataset: {df.shape}")
        print(f"First few rows:\n{df.head()}\n")

        # Column-level information
        print(f"Columns and their types:")
        print(df.dtypes)
        print("\nColumn-wise null values:")
        print(df.isnull().sum())

        # Basic stats for numerical and categorical columns
        print("\nSample stats for numerical columns:")
        print(df.describe(include=[float, int]).transpose())
        print("\nSample stats for categorical columns:")
        print(df.describe(include=[object]).transpose())

        return df
    except Exception as e:
        print(f"Error analyzing {file_path}: {e}")
        return None

def compare_csvs(file1, file2):
    """
    Compares the structure and content of two CSV files.
    """
    df1 = analyze_csv(file1)
    df2 = analyze_csv(file2)

    if df1 is not None and df2 is not None:
        # Comparing column names
        common_columns = set(df1.columns).intersection(set(df2.columns))
        print(f"\nCommon columns ({len(common_columns)}): {common_columns}")

        unique_to_file1 = set(df1.columns) - set(df2.columns)
        unique_to_file2 = set(df2.columns) - set(df1.columns)
        print(f"\nColumns unique to {file1}: {unique_to_file1}")
        print(f"Columns unique to {file2}: {unique_to_file2}")

        # Checking for similar column names with potential typos
        # (This can be extended with fuzzy matching)
        print("\nHint: Check for similar column names in case of typos.")

        # Summary of data overlap
        if not common_columns:
            print("\nNo common columns to join on.")
        else:
            # Sampling data for overlaps
            print("\nChecking overlap in data for common columns:")
            for col in common_columns:
                overlap = len(pd.merge(df1[[col]], df2[[col]], how='inner'))
                print(f"{col}: {overlap} overlapping values.")

        return df1, df2
    else:
        print("\nOne or both files could not be analyzed.")
        return None, None

# Main execution
if __name__ == "__main__":
    # Get the folder where the script is located
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Path to the 'dat_files' folder
    files_directory = os.path.join(script_directory, "files")

    # Specify the paths to the two CSV files
    file1 = os.path.join(files_directory, "steam_data.csv")  # Replace with the actual file name
    file2 = os.path.join(files_directory, "text_content.csv") # Replace with the actual file name

    # Analyze and compare the files
    df1, df2 = compare_csvs(file1, file2)

    if df1 is not None and df2 is not None:
        # Perform further data cleaning and joining based on analysis
        print("\nYou can now clean and join the data based on the analysis above.")

