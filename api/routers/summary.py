from fastapi import APIRouter
from api.services.data_service import get_monthly_sumary
from api.models import MonthlySummary

router = APIRouter()

@router.get("/", response_model=list[MonthlySummary])
def summary():
    df_summary = get_monthly_sumary()
    dict_summary = df_summary.to_dict("records")
    return dict_summary