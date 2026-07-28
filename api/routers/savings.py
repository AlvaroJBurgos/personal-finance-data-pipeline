from fastapi import APIRouter
from api.models import MonthlySavings
from api.services.data_service import get_savings_summary

router = APIRouter()

@router.get("/", response_model=list[MonthlySavings])
def savings():
    df_summary = get_savings_summary()
    dict_summary = df_summary.to_dict("records")
    return dict_summary


