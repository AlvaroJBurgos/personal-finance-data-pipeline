from ingestion import load_raw_data
from transformation import transform_data
from modeling import create_star_schema
from config.logging_config import setup_logging
from export import export_to_csv
import logging

def main():
    
    setup_logging()
    logger = logging.getLogger(__name__)
    
    # Extract
    try:
        raw_data = load_raw_data()
        logger.info('Loading raw files')
    except Exception as e:
        logger.exception("Load failed")
        raise
    
    
    # Transform
    try:
        transformed_data = transform_data(raw_data)
        logger.info('Transformation completed')
    except Exception as e:
        logger.exception("Transformation failed")
        raise
    
    # Model
    try:
        fact_transactions, dim_category, dim_date = create_star_schema(transformed_data)
        logger.info("Successfuly created the star schema")
    except Exception as e:
        logger.exception("Model/Export failed")
        raise
    
    # Export
    try:
        export_to_csv(fact_transactions, dim_category, dim_date)
        logger.info("Exported CSV files")
    except Exception as e:
        logger.exception("Failed to export CSV files")
        raise
    
    
    
    logger.info("ETL pipeline completed successfully")
    print('Finished ETL pipeline Succesfully')

if __name__ == '__main__':
    main()