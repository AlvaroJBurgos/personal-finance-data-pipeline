from fastapi import APIRouter
from api.services.data_service import get_transactions_sumary

router = APIRouter()

@router.get("/")
def summary():
    df_summary = get_transactions_sumary()
    dict_summary = df_summary.to_dict("records")
    return dict_summary