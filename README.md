# 🌸 Lumi Beauty – Cosmetic Chatbot & Admin Dashboard

> **Đồ án môn Điện toán đám mây** — Telegram Chatbot tư vấn mỹ phẩm tích hợp AI (Gemini), quản lý đơn hàng và Admin Dashboard trực quan.

---

## 📋 Tính năng chính

### 🤖 Telegram Bot
| Lệnh | Mô tả |
|---|---|
| `/start` | Chào mừng & hướng dẫn sử dụng |
| `/skintype` | Xác định loại da (chọn nút bấm) |
| `/recommend` | Gợi ý sản phẩm phù hợp với loại da |
| `/products` | Duyệt sản phẩm theo danh mục |
| `/search <từ khóa>` | Tìm kiếm sản phẩm |
| `/xem <tên SP>` | Xem ảnh sản phẩm |
| `/order` | Đặt hàng (hội thoại nhiều bước) |
| `/myorder` | Xem lịch sử đơn hàng |
| `/ask <câu hỏi>` | Tư vấn da bằng Gemini AI |
| _(chat tự do)_ | AI tư vấn tự nhiên không cần lệnh |

### 🖥️ Admin Dashboard
- **Thống kê tổng quan**: Tổng users, đơn hàng, sản phẩm, doanh thu
- **Biểu đồ trực quan**: Bar chart & pie chart theo trạng thái đơn hàng
- **Quản lý Users**: Xem, tìm kiếm, xóa người dùng
- **Quản lý Orders**: Lọc theo trạng thái, cập nhật trạng thái real-time
- **Quản lý Products**: Xem toàn bộ catalog sản phẩm
- **Dark mode** + Glassmorphism UI

---

## 🏗️ Kiến trúc hệ thống

```
cosmetic-telegram-bot/
├── app.py              # Entry point — Telegram Bot (Polling / Webhook)
├── dashboard.py        # Admin Dashboard — Flask REST API server
│
├── bot/                # Logic bot Telegram
│   ├── handlers.py     # Xử lý tất cả lệnh (/start, /order, ...)
│   ├── ai.py           # Tích hợp Gemini AI + caching sản phẩm
│   ├── keyboards.py    # Inline keyboard buttons
│   └── messages.py     # Văn bản tin nhắn chuẩn
│
├── database/           # Lớp truy cập dữ liệu (Azure Cosmos DB)
│   ├── cosmos.py       # Kết nối & singleton client
│   ├── users.py        # CRUD người dùng
│   ├── orders.py       # CRUD đơn hàng
│   └── products.py     # Query sản phẩm
│
├── templates/
│   └── dashboard.html  # Giao diện Admin Dashboard (Glassmorphism)
│
├── data/
│   ├── seed_products.py    # Script import 60+ sản phẩm vào Cosmos DB
│   └── img_folder_map.json # Map tên sản phẩm → file ảnh
│
├── img/                # Ảnh sản phẩm (32 ảnh)
├── Dockerfile          # Container cho deploy Cloud Run / Render
└── requirements.txt    # Python dependencies
```

---

## ☁️ Tech Stack

| Layer | Technology |
|---|---|
| **AI** | Google Gemini 2.0 Flash (`google-generativeai`) |
| **Bot Framework** | python-telegram-bot ≥ 20.0 (async) |
| **Database** | Azure Cosmos DB (NoSQL) |
| **Web Dashboard** | Flask + Vanilla HTML/CSS/JS |
| **Deploy** | Docker → Google Cloud Run / Render.com |
| **Config** | python-dotenv |

---

## ⚙️ Cài đặt & Chạy

### 1. Clone & cài dependencies

```bash
git clone https://github.com/<your-org>/cosmetic-telegram-bot.git
cd cosmetic-telegram-bot

python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux/Mac

pip install -r requirements.txt
```

### 2. Cấu hình biến môi trường

```bash
cp .env.example .env
```

Chỉnh sửa file `.env`:

```env
TELEGRAM_TOKEN=your_telegram_bot_token_here
COSMOS_ENDPOINT=https://your-account.documents.azure.com:443/
COSMOS_KEY=your_cosmos_primary_key_here
COSMOS_DATABASE=lumibeauty
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-2.0-flash
```

### 3. Seed dữ liệu sản phẩm (chạy 1 lần)

```bash
python data/seed_products.py
```

### 4. Chạy Bot (Dev - Long Polling)

```bash
python app.py
```

### 5. Chạy Admin Dashboard

```bash
python dashboard.py
# Mở http://localhost:5050
```

---

## 🐳 Deploy với Docker

```bash
# Build image
docker build -t lumi-beauty-bot .

# Chạy với env file
docker run --env-file .env -p 8443:8443 lumi-beauty-bot
```

Để deploy lên **Google Cloud Run**, đặt biến môi trường:
```env
ENVIRONMENT=production
WEBHOOK_URL=https://your-service-url.run.app
PORT=8080
```

---

## 🔑 Lấy API Keys

| Key | Nơi lấy |
|---|---|
| `TELEGRAM_TOKEN` | [@BotFather](https://t.me/BotFather) trên Telegram |
| `GEMINI_API_KEY` | [Google AI Studio](https://aistudio.google.com/apikey) |
| `COSMOS_ENDPOINT` & `COSMOS_KEY` | Azure Portal → Cosmos DB → Keys |

---

## 📊 Dashboard Architecture

```
Browser (dashboard.html)
    │
    │  fetch('/api/stats')
    │  fetch('/api/users')
    │  fetch('/api/orders')
    │  fetch('/api/products')
    ▼
Flask (dashboard.py :5050)
    │
    │  import database.users / orders / products
    ▼
Database Layer (database/)
    │
    │  azure-cosmos SDK
    ▼
Azure Cosmos DB (cloud)
  ├── Container: users     (partition: /telegram_id)
  ├── Container: orders    (partition: /user_id)
  └── Container: products  (partition: /id)
```

---

## 📄 License

MIT License — Đồ án học tập, không sử dụng cho mục đích thương mại.
