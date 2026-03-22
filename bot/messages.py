WELCOME_MSG = """
🌸 *Chào mừng đến với Lumi Beauty Chatbot!* 🌸

Tôi là trợ lý tư vấn mỹ phẩm của bạn.
Tôi sẽ giúp bạn tìm sản phẩm phù hợp nhất với làn da của mình! ✨

📋 *Các lệnh có thể dùng:*
/skintype – Xác định loại da
/recommend – Gợi ý sản phẩm cho bạn
/products – Xem danh sách sản phẩm
/search – Tìm kiếm sản phẩm
/ask <câu hỏi> – 🤖 TƯ VẤN AI: Chat với Gemini AI để được tư vấn da chuyên sâu 
/order – Đặt hàng
/myorder – Xem đơn hàng của bạn
"""

SKINTYPE_MSG = """
💆 *Hãy cho tôi biết loại da của bạn nhé!*

Chọn loại da bên dưới để tôi gợi ý sản phẩm phù hợp nhất cho bạn:
"""

NO_SKINTYPE_MSG = """
⚠️ Bạn chưa xác định loại da!
Hãy dùng /skintype để chọn loại da trước nhé.
"""

NO_PRODUCTS_MSG = "😔 Không tìm thấy sản phẩm nào phù hợp."

def format_product(product: dict, index: int) -> str:
    skintype_str = ", ".join(product.get("skintype", []))
    return (
        f"*{index}. {product['name']}*\n"
        f"   💰 Giá: {product['price']:,} VNĐ\n"
        f"   🧴 Loại da: {skintype_str}\n"
        f"   📝 {product.get('description', '')}\n"
    )

def format_order(order: dict, index: int) -> str:
    return (
        f"*{index}. {order['product_name']}*\n"
        f"   👤 Người nhận: {order.get('customer_name', 'Không có')}\n"
        f"   📦 Số lượng: {order['quantity']}\n"
        f"   📍 Địa chỉ: {order['address']}\n"
        f"   🔄 Trạng thái: {order['status']}\n"
        f"   🕒 Ngày đặt: {order['created_at'][:10]}\n"
    )
