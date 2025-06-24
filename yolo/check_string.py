import pandas as pd
import glob
import os

def search_string_in_csv_files(folder_path, search_string):
    file_pattern = os.path.join(folder_path, '*.csv')
    
    csv_files = glob.glob(file_pattern)
    print(csv_files)
    for file in csv_files:
        try:
            df = pd.read_csv(file)
            if df.apply(lambda row: row.astype(str).str.contains(search_string, case=False, na=False).any(), axis=1).any():
                print(f"'{search_string}' found in file: {file}")
            else:
                print(f"'{search_string}' not found in file: {file}")
        except Exception as e:
            print(f"Error reading {file}: {e}")

# Usage example
folder_path = 'yolo/new_dataset/results' 
search_string = 'inf' #inf or nan

search_string_in_csv_files(folder_path, search_string)
