from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Transaction(BaseModel):
    user_id: str
    amount: float
    category: str
    description: Optional[str]=None
    date: datetime = datetime.now()

class User(BaseModel):
    username: str 
    email: str
    password: str                           # use hashing in production
