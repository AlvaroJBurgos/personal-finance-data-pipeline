

def test_modeling_creates_fact_transactions_columns(modeled_dataframe):
    valid_columns = ['CategoryID', 'DateID', 'Amount']
    assert set(modeled_dataframe.fact_transactions.columns) == set(valid_columns)

def test_modeling_creates_dim_category_columns(modeled_dataframe):
    valid_columns = ['CategoryID', 'Category', 'Transaction Type']
    assert set(modeled_dataframe.dim_category.columns) == set(valid_columns)

def test_modeling_creates_dim_date_colums(modeled_dataframe):
    valid_columns = ['DateID', 'Year', 'MonthNum', 'Month', 'Week']

    assert set(modeled_dataframe.dim_date.columns) == set(valid_columns)

def test_modeling_valid_dim_dates(modeled_dataframe):
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
    valid_month_num = [1,2,3,4,5,6,7,8,9,10,11,12]
    valid_week_num = [1,2,3,4,5]
    assert modeled_dataframe.dim_date["Month"].isin(valid_months).all()
    assert modeled_dataframe.dim_date["MonthNum"].isin(valid_month_num).all()
    assert modeled_dataframe.dim_date["Week"].isin(valid_week_num).all()
    