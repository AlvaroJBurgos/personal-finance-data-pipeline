import pandas as pd
import os
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROCESSED_PATH = os.path.join(BASE_DIR, "data", "processed")

def get_transactions(year: int | None = None, month: str | None = None) -> pd.DataFrame:
    transactions_path = os.path.join(PROCESSED_PATH, "fact_transactions.csv")
    date_path = os.path.join(PROCESSED_PATH, "dim_date.csv")
    fact_transactions = pd.read_csv(transactions_path, decimal=',', sep=';')
    dim_date = pd.read_csv(date_path, decimal=',', sep=';')
    fact_transactions = fact_transactions.merge(dim_date, on=["DateID"])
    if year is not None:
        fact_transactions = fact_transactions[fact_transactions["Year"] == year]
    if month is not None:
        fact_transactions = fact_transactions[fact_transactions["Month"] == month]
    return fact_transactions

def get_transactions_sumary() -> pd.DataFrame:
    transactions_path = os.path.join(PROCESSED_PATH, "fact_transactions.csv")
    date_path = os.path.join(PROCESSED_PATH, "dim_date.csv")
    fact_transactions = pd.read_csv(transactions_path, decimal=',', sep=';')
    dim_date = pd.read_csv(date_path, decimal=',', sep=';')
    fact_transactions = fact_transactions.merge(dim_date, on=["DateID"])
    fact_transactions = fact_transactions.groupby(["Year", "Month"]).agg({"Amount": "sum"}).reset_index()
    return fact_transactions

def get_categories() -> pd.DataFrame:
    categories_path = os.path.join(PROCESSED_PATH, "dim_category.csv")
    dim_category = pd.read_csv(categories_path, decimal=',', sep=';')
    return dim_category

