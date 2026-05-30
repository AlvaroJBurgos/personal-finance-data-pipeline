import os

MONTH_MAPPING = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12,
}

def create_star_schema(df):
    
    df = df.copy()
    
    # Creating dim_category based on df with only Category and Transaction Type, droping duplicates, and resetting Index
    dim_category = df[['Category', 'Transaction Type']].drop_duplicates().reset_index(drop=True)

    #Creating the auto-augmented ID for the dimCategory
    dim_category.insert(0, 'CategoryID', range(1, 1 + len(dim_category)))

    # Merging dim_category and df to add the CategoryID to what will be the fact table
    df = df.merge(dim_category, on=['Category', 'Transaction Type'])
  

    # Now we delete the double columns of Category and Transaction Type as we have it in our dim_category
    df = df.drop(['Category', 'Transaction Type'], axis=1)

    # Reorder
    df = df[['CategoryID', 'Week', 'Month', 'Year', 'Amount']]

    # Create dim_date based on the df
    dim_date = df[['Week', 'Month', 'Year']].drop_duplicates().reset_index(drop=True)

    # Map the months to the Dictionary from above
    dim_date['MonthNum'] = dim_date['Month'].map(MONTH_MAPPING)

    # Validation check
    if dim_date['MonthNum'].isna().any():
        raise ValueError(
            'Some month values could not be mapped.'
        )

    # Sort dim_date by Year, MonthNum and Week
    dim_date = dim_date.sort_values(by=['Year', 'MonthNum', 'Week']).reset_index(drop=True)

    # We create DateID in dim_date
    dim_date.insert(0, 'DateID', range(1, 1 + len(dim_date)))

    # Ordering by preference
    dim_date = dim_date[['DateID', 'Year', 'MonthNum', 'Month', 'Week']]

    # Merge dim_date with the df
    df = df.merge(dim_date, on=['Week', 'Month', 'Year'])

    # Drop the time columns and keep DateID
    df = df.drop(['Week', 'MonthNum', 'Month', 'Year'], axis=1)

    #Reorder base on preference and create fact_transactions
    fact_transactions = df[['CategoryID', 'DateID', 'Amount']]


    # Export tables to .csv for Power BI import to /data/processed folder
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    processed_path  = os.path.join(base_dir, 'data', 'processed')

    os.makedirs(processed_path , exist_ok=True)
    
    fact_transactions.to_csv(os.path.join(processed_path , 'fact_transactions.csv'), index=False, encoding='utf-8', decimal=',', sep=';')
    dim_category.to_csv(os.path.join(processed_path , 'dim_category.csv'), index=False, encoding='utf-8', decimal=',', sep=';')
    dim_date.to_csv(os.path.join(processed_path , 'dim_date.csv'), index=False, encoding='utf-8', decimal=',', sep=';')
    # print(f'Processed files exported to: {processed_path}')
    
    return fact_transactions, dim_category, dim_date