from pymongo import MongoClient

# Connect to MongoDB
client= MongoClient('mongodb://localhost:27017/')
db = client['finance_db']

# Collections
users_collection = db["users"]
transactions_collection = db["transactions"]