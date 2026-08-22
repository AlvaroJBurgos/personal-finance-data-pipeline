import pytest
import pandas as pd
from etl.transformation import transform_data
from etl.modeling import create_star_schema

@pytest.fixture
def raw_dataframe():
    return pd.DataFrame(data=[
        [None, "Total Income", 1500, 1200, "Monthly Sanvings", -100, None, 1500, "March", 2026],
        [None, "Total Income", 1500, 1200, "Monthly Sanvings", -44.7, None, None, "March", 2026],
        [None, "Income", 1500, 1200, None, 50, None, None, "March", 2026],
        [None, "Total Expenses", 1500, 1200, "Monthly Sanvings", -44.7, None, 2200, "March", 2026],
        [None, "Expenses", 1500, 1200, "Total Income", -20.7, None, None, "March", 2026],
        [None, "Rent", None, None, None, -0, None, None, "March", 2025],
        [None, "Food", None, None, None, -0, None, None, "March", 2025],
        [None, "Restaurant Card", 100.0, None, None, -0, None, None, "March", 2025],
        ],
        columns=["Unnamed: 0" , "Unnamed: 1" , "Unnamed: 2" , "Unnamed: 3" , "Unnamed: 4" , "Unnamed: 5" , "Unnamed: 6" , "Unnamed: 7" , "Month" , "Year"])
    # return pd.DataFrame(raw_dataframe, columns=["Unnamed: 0" , "Unnamed: 1" , "Unnamed: 2" , "Unnamed: 3" , "Unnamed: 4" , "Unnamed: 5" , "Unnamed: 6" , "Unnamed: 7" , "Month" , "Year"])

@pytest.fixture
def transformed_dataframe(raw_dataframe):
    return transform_data(raw_dataframe)

@pytest.fixture
def modeled_dataframe(transformed_dataframe):
    return create_star_schema(transformed_dataframe)

    