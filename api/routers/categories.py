from fastapi import APIRouter
from api.services.data_service import get_categories

router = APIRouter()

@router.get("/")
def categories():
    df_cagetories = get_categories()
    dict_categories = df_cagetories.to_dict("records")
    return dict_categories
    
    
    