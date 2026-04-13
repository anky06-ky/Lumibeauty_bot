import uuid
from datetime import datetime
from database.mongo import get_collection


def _c():
    return get_collection("orders")


def create_order(user_id: int, product_name: str, quantity: int, customer_name: str, address: str) -> str:
    order_id = str(uuid.uuid4())
    _c().insert_one({
        "id": order_id,
        "user_id": str(user_id),
        "customer_name": customer_name,
        "product_name": product_name,
        "quantity": quantity,
        "address": address,
        "status": "Đang xử lý",
        "created_at": datetime.now().isoformat()
    })
    return order_id


def get_orders_by_user(user_id: int) -> list:
    cursor = _c().find(
        {"user_id": str(user_id)},
        {"_id": 0}
    ).sort("created_at", -1).limit(10)
    return list(cursor)


def get_all_orders() -> list:
    cursor = _c().find({}, {"_id": 0}).sort("created_at", -1)
    return list(cursor)


def update_order_status(order_id: str, user_id: str, new_status: str):
    result = _c().update_one(
        {"id": order_id, "user_id": user_id},
        {"$set": {"status": new_status}}
    )
    return result.modified_count > 0
