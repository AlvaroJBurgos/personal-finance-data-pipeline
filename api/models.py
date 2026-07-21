from pydantic import BaseModel, Field

class MonthlySummary(BaseModel):
    Year: int
    Month: str
    Transaction_Type: str = Field(alias="Transaction Type")
    Amount: float
    
class Transaction(BaseModel):
    CategoryID: int
    DateID: int
    Amount: float
    Year: int
    MonthNum: int
    Month: str
    Week: int
    Category: str
    Transaction_Type: str = Field(alias="Transaction Type")
    
class Category(BaseModel):
    CategoryID: int
    Category: str
    Transaction_Type: str = Field(alias="Transaction Type")

    