import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from telegram.request import HTTPXRequest

from bot.handlers import (
    start, skintype, skintype_callback,
    recommend, product_list, search,
    my_orders, get_order_conversation_handler,
    ask_ai, normal_chat, category_callback, view_image
)

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

def main():
    # ── Tạo custom request với timeout cao hơn cho Render ──
    # Render Free plan cold-start chậm → cần timeout dài & retry nhiều
    custom_request = HTTPXRequest(
        connect_timeout=30.0,       # Thời gian tối đa chờ kết nối (giây)
        read_timeout=30.0,          # Thời gian tối đa chờ đọc response
        write_timeout=30.0,         # Thời gian tối đa chờ ghi request
        pool_timeout=30.0,          # Thời gian tối đa chờ lấy connection từ pool
        connection_pool_size=256,   # Số lượng connection tối đa trong pool
    )

    app = (
        ApplicationBuilder()
        .token(TOKEN)
        .request(custom_request)          # Request cho các API call thông thường
        .get_updates_request(custom_request)  # Request cho getUpdates (polling)
        .connect_timeout(30.0)
        .read_timeout(30.0)
        .write_timeout(30.0)
        .pool_timeout(30.0)
        .build()
    )

    # Lệnh ở group=-1 để luôn chạy trước ConversationHandler (vd: đang /order vẫn dùng được /xem)
    app.add_handler(CommandHandler("start", start), group=-1)
    app.add_handler(CommandHandler("skintype", skintype), group=-1)
    app.add_handler(CommandHandler("recommend", recommend), group=-1)
    app.add_handler(CommandHandler("products", product_list), group=-1)
    app.add_handler(CommandHandler("search", search), group=-1)
    app.add_handler(CommandHandler("xem", view_image), group=-1)
    app.add_handler(CommandHandler("myorder", my_orders), group=-1)
    app.add_handler(CommandHandler("ask", ask_ai), group=-1)

    # ConversationHandler cho /order
    app.add_handler(get_order_conversation_handler())

    # Handler cho chat tự nhiên bằng AI
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, normal_chat))

    # Callback xử lý nút chọn danh mục sản phẩm
    app.add_handler(CallbackQueryHandler(category_callback, pattern="^cat_"))

    # Callback xử lý nút chọn loại da
    app.add_handler(CallbackQueryHandler(skintype_callback, pattern="^skin_"))

    ENVIRONMENT = os.getenv("ENVIRONMENT", "local")

    if ENVIRONMENT == "production":
        # Chạy Webhook trên Cloud (Render, Railway, Fly.io, ...)
        PORT = int(os.environ.get('PORT', '10000'))
        WEBHOOK_URL = os.environ.get('WEBHOOK_URL')  # Ví dụ: https://lumi-beauty-bot.onrender.com

        print(f"[Lumi Beauty Bot] is running in Webhook mode on port {PORT}...")
        print(f"[Lumi Beauty Bot] Webhook URL: {WEBHOOK_URL}")
        print(f"[Lumi Beauty Bot] Token present: {bool(TOKEN)}")
        app.run_webhook(
            listen="0.0.0.0",
            port=PORT,
            webhook_url=WEBHOOK_URL,
            bootstrap_retries=-1,     # Retry vô hạn cho đến khi kết nối được Telegram API
            drop_pending_updates=True, # Bỏ qua tin nhắn cũ khi restart
        )
    else:
        # Chạy Long Polling khi DEV ở Local
        print("[Lumi Beauty Bot] is running in Polling mode (Local)...")
        app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()