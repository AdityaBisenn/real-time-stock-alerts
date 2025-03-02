from pydantic import BaseModel

class NotificationCreate(BaseModel):
    user_id: int
    alert_id: int
    stock_symbol: str
    message: str