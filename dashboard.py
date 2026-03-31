"""
Lumi Beauty – Admin Dashboard
Flask web server phục vụ giao diện quản trị và REST API.
Chạy: python dashboard.py  →  http://localhost:5050
"""

import os
import requests as http_req
from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv

load_dotenv()

from database import users, orders, products


# ── Telegram Notification ─────────────────────────────────
def _notify_telegram(user_id: str, order_id: str, product_name: str, new_status: str):
    """Gửi tin nhắn Telegram cho khách khi admin cập nhật trạng thái đơn hàng."""
    token = os.getenv("TELEGRAM_TOKEN")
    if not token or not user_id:
        return

    short_id = (order_id or "")[:8]
    STATUS_MESSAGES = {
        "Đang xử lý": (
            f"🕐 *Cập nhật đơn hàng của bạn*\n\n"
            f"Đơn hàng *{product_name}* đang được xử lý.\n"
            f"Chúng tôi sẽ liên hệ khi hàng sẵn sàng giao nhé! 📦\n"
            f"_Mã đơn: {short_id}..._"
        ),
        "Đã giao": (
            f"🎉 *Đơn hàng đã giao thành công!*\n\n"
            f"Sản phẩm *{product_name}* đã được giao đến bạn rồi nhé!\n"
            f"Cảm ơn bạn đã mua hàng tại *Lumi Beauty* 🌸\n"
            f"_Mã đơn: {short_id}..._"
        ),
        "Đã hủy": (
            f"❌ *Đơn hàng đã bị hủy*\n\n"
            f"Đơn hàng *{product_name}* của bạn đã bị hủy.\n"
            f"Nếu có thắc mắc, vui lòng nhắn tin cho shop nhé! 🌸\n"
            f"_Mã đơn: {short_id}..._"
        ),
    }
    text = STATUS_MESSAGES.get(
        new_status,
        f"📦 Đơn hàng *{product_name}* vừa được cập nhật: *{new_status}*"
    )
    try:
        http_req.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            json={"chat_id": user_id, "text": text, "parse_mode": "Markdown"},
            timeout=6
        )
        print(f"[Dashboard] Đã gửi notify cho user {user_id}: {new_status}")
    except Exception as e:
        print(f"[Dashboard] Lỗi gửi Telegram notify: {e}")

app = Flask(__name__)


# ── Trang chính ──────────────────────────────────────────
@app.route("/")
def index():
    return render_template("dashboard.html")


# ── API: Thống kê ────────────────────────────────────────
@app.route("/api/stats")
def api_stats():
    all_users = users.get_all_users()
    all_orders = orders.get_all_orders()
    all_products = products.get_all_products()

    total_revenue = 0
    for o in all_orders:
        if o.get("status") != "Đã hủy":
            # Tìm giá sản phẩm
            prod = products.get_product_by_name(o.get("product_name", ""))
            price = prod["price"] if prod else 0
            total_revenue += price * o.get("quantity", 1)

    return jsonify({
        "users": len(all_users),
        "orders": len(all_orders),
        "products": len(all_products),
        "revenue": total_revenue,
    })


# ── API: Users ───────────────────────────────────────────
@app.route("/api/users")
def api_users():
    all_users = users.get_all_users()
    search = request.args.get("search", "").lower()
    if search:
        all_users = [
            u for u in all_users
            if search in (u.get("username") or "").lower()
            or search in (u.get("full_name") or "").lower()
            or search in (u.get("telegram_id") or "").lower()
        ]
    clean = []
    for u in all_users:
        username = u.get("username") or ""
        full_name = u.get("full_name") or ""
        # Hiển thị tên: ưu tiên full_name, fallback @username
        display = full_name if full_name and full_name != "unknown" else (f"@{username}" if username else "unknown")
        clean.append({
            "id": u.get("id"),
            "telegram_id": u.get("telegram_id"),
            "username": username,
            "full_name": full_name,
            "display_name": display,
            "skintype": u.get("skintype"),
        })
    return jsonify(clean)


@app.route("/api/users/<telegram_id>", methods=["DELETE"])
def api_delete_user(telegram_id):
    ok = users.delete_user(int(telegram_id))
    return jsonify({"success": ok})


# ── API: Orders ──────────────────────────────────────────
@app.route("/api/orders")
def api_orders():
    all_orders = orders.get_all_orders()
    status_filter = request.args.get("status", "")
    if status_filter:
        all_orders = [o for o in all_orders if o.get("status") == status_filter]

    clean = []
    for o in all_orders:
        clean.append({
            "id": o.get("id"),
            "user_id": o.get("user_id"),
            "customer_name": o.get("customer_name"),
            "product_name": o.get("product_name"),
            "quantity": o.get("quantity"),
            "address": o.get("address"),
            "status": o.get("status"),
            "created_at": o.get("created_at"),
        })
    return jsonify(clean)


@app.route("/api/orders/<order_id>", methods=["PATCH"])
def api_update_order(order_id):
    data = request.get_json()
    new_status = data.get("status")
    user_id = data.get("user_id")
    product_name = data.get("product_name", "sản phẩm")
    if not new_status or not user_id:
        return jsonify({"success": False, "error": "Missing status or user_id"}), 400
    ok = orders.update_order_status(order_id, user_id, new_status)
    if ok:
        _notify_telegram(user_id, order_id, product_name, new_status)
    return jsonify({"success": ok})


# ── API: Products ────────────────────────────────────────
@app.route("/api/products")
def api_products():
    all_products = products.get_all_products()
    search = request.args.get("search", "").lower()
    if search:
        all_products = [
            p for p in all_products
            if search in (p.get("name") or "").lower()
            or search in (p.get("description") or "").lower()
        ]

    clean = []
    for p in all_products:
        clean.append({
            "id": p.get("id"),
            "name": p.get("name"),
            "price": p.get("price"),
            "description": p.get("description"),
            "skintype": p.get("skintype", []),
            "image": p.get("image"),
        })
    return jsonify(clean)


# ── Main ─────────────────────────────────────────────────
if __name__ == "__main__":
    print("[Lumi Beauty] Admin Dashboard -> http://localhost:5050")
    app.run(host="0.0.0.0", port=5050, debug=True)
