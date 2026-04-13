import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI     = os.getenv("MONGO_URI")         # Lấy từ MongoDB Atlas
DATABASE_NAME = os.getenv("MONGO_DATABASE", "lumibeauty")

_client   = None
_database = None
_cols     = {}


def get_client() -> MongoClient:
    global _client
    if _client is None:
        _client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    return _client


def get_database():
    global _database
    if _database is None:
        _database = get_client()[DATABASE_NAME]
    return _database


def get_collection(name: str):
    """Lấy (hoặc tạo tự động) collection MongoDB."""
    if name not in _cols:
        _cols[name] = get_database()[name]
    return _cols[name]
