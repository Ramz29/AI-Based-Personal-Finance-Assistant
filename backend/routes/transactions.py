from fastapi import APIRouter, HTTPException
from backend.database import transactions_collection
from backend.models import Transaction

router = APIRouter()
# Add a transaction
@router.post("/transactions")
async def add_transaction(transaction: Transaction):
    transaction_dict = transaction.model_dump()
    transactions_collection.insert_one(transaction_dict)
    return {"message" : "Transaction added succesfully"}

# Get all transactions
@router.get("/transactions")
async def get_transactions(user_id: str):
    transactions=list(transactions_collection.find({"user_id": user_id}, {"_id": 0}))
    if not transactions:
        raise HTTPException(status_code=404, detail="No transactions found")
    return transactions
