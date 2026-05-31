from ingestion import load_raw_data
from transformation import transform_data
from modeling import create_star_schema
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    
    logging.info('Starting ETL pipeline')

    # Extract
    try:
        raw_data = load_raw_data()
        logging.info('Loading raw files')
    except Exception as e:
        logging.error(f'Extaction failed: {e}')
        raise
    
    
    # Transform
    try:
        transformed_data = transform_data(raw_data)
        logging.info('Transformation completed')
    except Exception as e:
        logging.error(f'Transformation failed: {e}')
        raise
    
    # Model + Export
    try:
        fact_transactions, dim_category, dim_date = create_star_schema(transformed_data)
        logging.info("Successfuly created the star schema")
    except Exception as e:
        logging.error(f'Modeling/Export failed: {e}')
        raise
    
    logging.info("ETL pipeline completed successfully")
    print('Finished ETL pipeline Succesfully')

if __name__ == '__main__':
    main()