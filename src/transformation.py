import pandas as pd

def transform_data(raw_data):

    # Create a copy to avoid modifying the original dataframe
    df = raw_data.copy()

    # Rename columns first
    df = df.rename(columns={
        'Unnamed: 1': 'Category',
        'Unnamed: 2': 'Week 1',
        'Unnamed: 3': 'Week 2',
        'Unnamed: 4': 'Week 3',
        'Unnamed: 5': 'Week 4',
        'Unnamed: 6': 'Week 5'
    })

    # Drop completely empty columns
    df = df.dropna(axis=1, how='all')

    # Add Transaction Type column
    df['Transaction Type'] = None

    # Detect Income / Expense sections
    df.loc[df['Category'] == 'Income', 'Transaction Type'] = 'Income'
    df.loc[df['Category'] == 'Expenses', 'Transaction Type'] = 'Expense'

    # Forward fill Transaction Type
    df['Transaction Type'] = df['Transaction Type'].ffill()

    # Categories/rows we don't want
    invalid_categories = [
        'Income',
        'Expenses',
        'Total Income',
        'Total Expenses',
        'Montly Savings'
    ]

    # Remove unwanted rows
    df = df[
        ~df['Category'].isin(invalid_categories)
        & df['Category'].notna()
    ]

    # Unpivot weeks into rows
    df = df.melt(
        id_vars=[
            'Category',
            'Transaction Type',
            'Month',
            'Year'
        ],
        value_vars=[
            'Week 1',
            'Week 2',
            'Week 3',
            'Week 4',
            'Week 5'
        ],
        var_name='Week',
        value_name='Amount'
    )

    # Convert Week column from "Week 1" -> 1
    df['Week'] = (
        df['Week']
        .str.replace('Week', '', regex=False)
        .str.strip()
        .astype(int)
    )
    
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
    df = df[df['Amount'].notna()]

    return df