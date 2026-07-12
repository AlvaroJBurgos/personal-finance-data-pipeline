import pandas as pd
import os
import logging

def get_transactions(year: int | None = None, month: str | None = None) -> pd.DataFrame:
    abs_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    transactions_path = os.path.join(abs_path, "data", "processed", "fact_transactions.csv")
    date_path = os.path.join(abs_path, "data", "processed", "dim_date.csv")
    fact_transactions = pd.read_csv(transactions_path, decimal=',', sep=';')
    dim_date = pd.read_csv(date_path, decimal=',', sep=';')
    fact_transactions = fact_transactions.merge(dim_date, on=["DateID"])
    if year is not None:
        fact_transactions = fact_transactions[fact_transactions["Year"] == year]
    if month is not None:
        fact_transactions = fact_transactions[fact_transactions["Month"] == month]
    return fact_transactions

def get_categories() -> pd.DataFrame:
    abs_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    categories_path = os.path.join(abs_path, "data", "processed", "dim_category.csv")
    dim_category = pd.read_csv(categories_path, decimal=',', sep=';')
    return dim_category


