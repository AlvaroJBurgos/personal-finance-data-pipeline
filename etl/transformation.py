import pandas as pd
import os
import re


def transform_data(raw_data: pd.DataFrame) -> pd.DataFrame:
    
    # Create a copy to avoid modifying the original dataframe
    df = raw_data.copy()

    # Rename columns first
    df = df.rename(columns={
        'Unnamed: 1': 'Category',
        'Unnamed: 2': 'Week 1',
        'Unnamed: 3': 'Week 2',
        'Unnamed: 4': 'Week 3',
        'Unnamed: 5': 'Week 4',
        'Unnamed: 6': 'Week 5',
        'Unnamed: 7': 'Total'
    })
    
    # Remove the totals column from the excel
    df = df.drop(['Total'], axis='columns')

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
        'Montly Savings',
        'Total'
    ]

    # Remove unwanted rows
    df = df[
        ~df['Category'].isin(invalid_categories)
        & df['Category'].notna()
    ]
    
    # Check colums that exist for the melt
    week_cols = [col for col in ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5']
                 if col in df.columns]

    # Unpivot weeks into rows
    df = df.melt(
        id_vars=[
            'Category',
            'Transaction Type',
            'Month',
            'Year'
        ],
        value_vars=week_cols,
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