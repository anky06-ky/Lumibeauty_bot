import uuid
from database.mongo import get_collection


def _c():
    return get_collection("users")


def get_user(telegram_id: int) -> dict | None:
    return _c().find_one({"telegram_id": str(telegram_id)}, {"_id": 0})


def save_user(telegram_id: int, username: str):
    user = get_user(telegram_id)
    if not user:
        _c().insert_one({
            "id": str(telegram_id),
            "telegram_id": str(telegram_id),
            "username": username or "Khách hàng",
            "skintype": None
        })
    elif user.get("username") in (None, "unknown", "Khách hàng") and username:
        _c().update_one(
            {"telegram_id": str(telegram_id)},
            {"$set": {"username": username}}
        )


def update_skintype(telegram_id: int, skintype: str):
    _c().update_one(
        {"telegram_id": str(telegram_id)},
        {"$set": {"skintype": skintype}}
    )


def get_skintype(telegram_id: int) -> str | None:
    user = get_user(telegram_id)
    return user.get("skintype") if user else None


def get_all_users() -> list:
    return list(_c().find({}, {"_id": 0}))


def delete_user(telegram_id: int):
    result = _c().delete_one({"telegram_id": str(telegram_id)})
    return result.deleted_count > 0
