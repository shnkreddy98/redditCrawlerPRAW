import os
import pandas as pd

def merge_csv_files(folder_path, output_file):
    all_data = pd.DataFrame()

    # Iterate over files in the directory
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        # Check if the file is a CSV file
        if file_name.lower().endswith('.csv'):
            try:
                # Read the CSV file into a DataFrame
                current_data = pd.read_csv(file_path)

                # Append the current DataFrame to the overall DataFrame
                all_data = pd.concat([all_data, current_data], ignore_index=True)
            except Exception as e:
                print(f"Error reading file {file_name}: {e}")

    # Write the concatenated DataFrame to a new CSV file
    all_data.to_csv(output_file, index=False)
    print(f"Concatenated data written to {output_file}")

if __name__ == "__main__":
    # Path to the folder
    csv_folder_path = 'data'

    # Output file name
    output_csv_file = 'data/merged_data.csv'

    merge_csv_files(csv_folder_path, output_csv_file)
