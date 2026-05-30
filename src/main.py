from ingestion import load_raw_data
from transformation import transform_data
from modeling import create_star_schema

def main():
    
    try:
        
        print('Starting ETL pipeline')

        # Extract
        raw_data = load_raw_data()
        print("Loading raw files...")
        
        # Transform
        transformed_data = transform_data(raw_data)
        print("Transforming data...")
        
        # Model + Export
        fact_transactions, dim_category, dim_date = create_star_schema(transformed_data)
        print("Building star schema...")
        
        print("Export completed successfully.")
    
    except Exception as e:
        print(f"Pipeline failed: {e}")


if __name__ == '__main__':
    main()