from fastapi import APIRouter, HTTPException
from api.services.data_service import get_transactions
from api.models import Transaction

router = APIRouter()

@router.get("/", response_model=list[Transaction])
def transactions(year: int | None = None, month: str | None = None):
    df_transactions = get_transactions(year, month)
    if df_transactions.empty:
        raise HTTPException(status_code=404, detail="No transactions found")
    dict_transactions = df_transactions.to_dict("records")
    return dict_transactions
