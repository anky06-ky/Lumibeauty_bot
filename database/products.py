from database.mongo import get_collection


def _c():
    return get_collection("products")


def get_all_products() -> list:
    return list(_c().find({}, {"_id": 0}))


def get_products_by_skintype(skintype: str) -> list:
    return list(_c().find({"skintype": skintype}, {"_id": 0}))


def search_products(keyword: str) -> list:
    kw = keyword.lower()
    results = []
    for p in get_all_products():
        if kw in p.get("name", "").lower() or kw in p.get("description", "").lower():
            results.append(p)
    return results


def get_product_by_name(name: str) -> dict | None:
    return _c().find_one({"name": name}, {"_id": 0})
