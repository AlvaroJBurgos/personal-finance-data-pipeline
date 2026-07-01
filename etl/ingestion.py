import os
import re
import pandas as pd

def load_raw_data() -> pd.DataFrame:


    # Get project root directory
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    folder_path = os.path.join(base_dir, 'data', 'raw')

    all_dfs = []

    # Loop through all Excel files in the folder
    for filename in os.listdir(folder_path):
        if filename.startswith('Financials') and filename.endswith('.xlsx'):

            # Extract year from filename
            match = re.search(r'Financials(\d{4})', filename)
            if not match:
                raise ValueError(f"Could not extract year from filename: {filename}")
            year = int(match.group(1))

            # Full file path
            file_path = os.path.join(folder_path, filename)

            # Read all sheets
            sheets = pd.read_excel(file_path, sheet_name=None, decimal=',')

            # Process each sheet
            for sheet_name, df in sheets.items():
                df['Month'] = sheet_name
                df['Year'] = year
                all_dfs.append(df)

    # Combine everything
    if not all_dfs:
        raise ValueError("No valid Excel files found in /data/raw")
    raw_data = pd.concat(all_dfs, ignore_index=True)


    number_of_files = len(raw_data['Year'].unique())
    print(f'Extraction completed for {number_of_files} file(s)')

    return raw_data