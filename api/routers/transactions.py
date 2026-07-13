from fastapi import APIRouter
from api.services.data_service import get_transactions

router = APIRouter()

@router.get("/")
def transactions(year: int | None = None, month: str | None = None):
    df_transactions = get_transactions(year, month)
    dict_transactions = df_transactions.to_dict("records")
    return dict_transactions
