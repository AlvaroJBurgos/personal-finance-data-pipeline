from etl.transformation import transform_data
# from tests.conftest import raw_dataframe

def test_transformation_invalid_categories(raw_dataframe):
    result = transform_data(raw_dataframe)
    invalid_categories = [
            'Income',
            'Expenses',
            'Total Income',
            'Total Expenses',
            'Montly Savings',
            'Total'
        ]
    assert not result.isin[invalid_categories].any()