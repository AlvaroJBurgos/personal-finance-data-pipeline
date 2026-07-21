from fastapi import APIRouter
from api.services.data_service import get_categories
from api.models import Category

router = APIRouter()

@router.get("/", response_model=list[Category])
def categories():
    df_cagetories = get_categories()
    dict_categories = df_cagetories.to_dict("records")
    return dict_categories
    
    
    