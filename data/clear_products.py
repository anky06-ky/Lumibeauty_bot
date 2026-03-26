import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.cosmos import get_container

def clear_products():
    container = get_container("products", "/id")
    items = list(container.query_items(query="SELECT * FROM c", enable_cross_partition_query=True))
    for item in items:
        container.delete_item(item, partition_key=item["id"])
    print(f"✅ Đã xóa {len(items)} sản phẩm cũ.")

if __name__ == "__main__":
    clear_products()
