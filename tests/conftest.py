import pytest
import pandas as pd

@pytest.fixture
def raw_dataframe():
    return pd.DataFrame(data=[
        [None, "Total Income", 1500, 1200, "Monthly Sanvings", -100, None, 0, "March", 2026],
        [None, "Total Income", 1500, 1200, "Monthly Sanvings", -44.7, None, 0, "March", "2026"],
        [None, "Income", 1500, 1200, None, 50, None, 0, "March", 2026],
        [None, "Total Expenses", 1500, 1200, "Monthly Sanvings", -44.7, None, 0, "March", 2026],
        [None, "Expenses", 1500, 1200, "Total Income", -20.7, None, 0, "March", 2026],
        [None, "Rent", None, None, None, -0, None, 0, "March", 2025],
        ],
        columns=["Unnamed: 0" , "Unnamed: 1" , "Unnamed: 2" , "Unnamed: 3" , "Unnamed: 4" , "Unnamed: 5" , "Unnamed: 6" , "Unnamed: 7" , "Month" , "Year"])
    # return pd.DataFrame(raw_dataframe, columns=["Unnamed: 0" , "Unnamed: 1" , "Unnamed: 2" , "Unnamed: 3" , "Unnamed: 4" , "Unnamed: 5" , "Unnamed: 6" , "Unnamed: 7" , "Month" , "Year"])
    