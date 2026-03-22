import uuid
from database.cosmos import get_container

def _c():
    return get_container("users", "/telegram_id")

def get_user(telegram_id: int) -> dict | None:
    try:
        return _c().read_item(item=str(telegram_id), partition_key=str(telegram_id))
    except Exception:
        return None

def save_user(telegram_id: int, username: str):
    if not get_user(telegram_id):
        _c().create_item(body={
            "id": str(telegram_id),
            "telegram_id": str(telegram_id),
            "username": username or "unknown",
            "skintype": None
        })

def update_skintype(telegram_id: int, skintype: str):
    user = get_user(telegram_id)
    if user:
        user["skintype"] = skintype
        _c().replace_item(item=str(telegram_id), body=user)

def get_skintype(telegram_id: int) -> str | None:
    user = get_user(telegram_id)
    return user.get("skintype") if user else None
