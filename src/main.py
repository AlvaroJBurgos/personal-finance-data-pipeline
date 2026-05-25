from ingestion import load_raw_data
from transformation import transform_data
from modeling import create_star_schema

def main():
    
    print('Starting ETL pipeline')

    # Extract
    raw_data = load_raw_data()
    
    # Transform
    transformed_data = transform_data(raw_data)
    
    # Model + Export
    fact_transactions, dim_category, dim_date = create_star_schema(transformed_data)

if __name__ == '__main__':
    main()