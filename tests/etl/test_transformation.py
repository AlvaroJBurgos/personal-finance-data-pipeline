import pandas as pd

from etl.transformation import transform_data


def test_transformation_invalid_categories(transformed_dataframe):
    invalid_categories = [
            'Income',
            'Expenses',
            'Total Income',
            'Total Expenses',
            'Montly Savings',
            'Total'
        ]
    assert not transformed_dataframe["Category"].isin(invalid_categories).any()

def test_transformation_amount_is_not_null(transformed_dataframe):
    assert transformed_dataframe["Amount"].notna().all()
    assert pd.api.types.is_numeric_dtype(transformed_dataframe["Amount"])

def test_transformation_output_has_expected_columns(transformed_dataframe):
    valid_columns = [
        'Category',
        'Transaction Type',
        'Amount',
        'Week',
        'Month',
        'Year'
    ]
    assert transformed_dataframe.columns.isin(valid_columns).all()

def test_transformation_output_has_expected_week(transformed_dataframe):
    valid_weeks = [1, 2, 3, 4, 5]
    assert transformed_dataframe['Week'].isin(valid_weeks).all()

def test_transformation_output_has_expected_months(transformed_dataframe): 
    valid_months = [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
    ]
    assert transformed_dataframe["Month"].isin(valid_months).all()
    


    