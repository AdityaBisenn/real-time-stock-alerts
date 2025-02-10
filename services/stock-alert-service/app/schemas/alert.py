from pydantic import BaseModel

class AlertCreate(BaseModel):
    user_id: int
    stock_symbol: str
    target_price: float
    condition: str
