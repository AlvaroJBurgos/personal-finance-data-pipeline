import pandas as pd
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROCESSED_PATH = os.path.join(BASE_DIR, "data", "processed")
TRANSACTIONS_PATH = os.path.join(PROCESSED_PATH, "fact_transactions.csv")
DATE_PATH = os.path.join(PROCESSED_PATH, "dim_date.csv")
CATEGORIES_PATH = os.path.join(PROCESSED_PATH, "dim_category.csv")


def _load_transactions() -> pd.DataFrame:
    return pd.read_csv(TRANSACTIONS_PATH, decimal=',', sep=';')

def _load_dates() -> pd.DataFrame:
    return pd.read_csv(DATE_PATH, decimal=',', sep=';')

def _load_categories() -> pd.DataFrame:
    return pd.read_csv(CATEGORIES_PATH, decimal=',', sep=';')

def _merge_fact_date_category() -> pd.DataFrame:
    fact_transactions = _load_transactions()
    dim_date = _load_dates()
    dim_category = _load_categories()
    fact_transactions = fact_transactions.merge(dim_date, on=["DateID"])
    fact_transactions = fact_transactions.merge(dim_category, on=["CategoryID"])
    return fact_transactions

def get_transactions(year: int | None = None, month: str | None = None) -> pd.DataFrame:
    fact_transactions = _merge_fact_date_category()
    if year is not None:
        fact_transactions = fact_transactions[fact_transactions["Year"] == year]
    if month is not None:
        fact_transactions = fact_transactions[fact_transactions["Month"] == month]
    return fact_transactions

def get_monthly_sumary() -> pd.DataFrame:
    fact_transactions = _merge_fact_date_category()
    fact_transactions = fact_transactions.groupby(["Year", "Month", "Transaction Type"]).agg({"Amount": "sum"}).reset_index()
    return fact_transactions

def get_categories() -> pd.DataFrame:
    dim_category = _load_categories()
    return dim_category

def get_savings_summary () -> pd.DataFrame:
    fact_transactions = get_monthly_sumary()
    table = pd.pivot(fact_transactions, values="Amount", index=["Year", "Month"], columns=["Transaction Type"])
    table.columns.name = None
    table = table.reset_index()
    table["Savings"] = table["Income"] - table["Expense"]
    return table

