from fastapi import FastAPI, HTTPException, APIRouter
from api.routers.transactions import router as transactions_router
from api.routers.categories import router as categories_router
from api.routers.summary import router as summary_router



app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

app.include_router(transactions_router, prefix="/transactions")
app.include_router(categories_router, prefix="/categories")
app.include_router(summary_router, prefix="/summary/monthly")