import os
import pandas as pd

def export_to_csv(fact_transactions: pd.DataFrame,
                  dim_category: pd.DataFrame,
                  dim_date: pd.DataFrame) -> None:
    
     # Export tables to .csv
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # Technical debt, will fix later
    processed_path  = os.path.join(base_dir, 'data', 'processed')

    os.makedirs(processed_path , exist_ok=True)
    
    fact_transactions.to_csv(os.path.join(processed_path , 'fact_transactions.csv'), index=False, encoding='utf-8', decimal=',', sep=';')
    dim_category.to_csv(os.path.join(processed_path , 'dim_category.csv'), index=False, encoding='utf-8', decimal=',', sep=';')
    dim_date.to_csv(os.path.join(processed_path , 'dim_date.csv'), index=False, encoding='utf-8', decimal=',', sep=';')
    print(f'Processed files exported to: {processed_path}') # kept for debuggin purposes