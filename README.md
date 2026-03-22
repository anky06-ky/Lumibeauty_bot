# 🌸 Lumi Beauty Chatbot

Telegram Chatbot tư vấn mỹ phẩm thông minh, triển khai hoàn toàn trên **Microsoft Azure**.

> Đồ án môn "Nền tảng phát triển phần mềm" – Đại học Văn Lang (VLU)

---

## ✨ Tính năng

| Lệnh | Chức năng |
|------|-----------|
| `/start` | Chào mừng & giới thiệu bot |
| `/skintype` | Xác định loại da (nút chọn trực quan) |
| `/recommend` | Gợi ý sản phẩm theo loại da |
| `/products` | Xem toàn bộ danh sách sản phẩm |
| `/search <từ khóa>` | Tìm kiếm sản phẩm |
| `/order` | Đặt hàng (chọn → số lượng → địa chỉ → xác nhận) |
| `/myorder` | Xem lịch sử đơn hàng |

---

## 🏗️ Kiến trúc hệ thống (Azure)

```
User (Telegram App)
       ↓
Telegram Bot API
       ↓
Python Telegram Bot Server
       ↓
Azure App Service (PaaS – Cloud hosting)
       ↓
Azure Cosmos DB (NoSQL Database)
```

---

## ☁️ Azure Services sử dụng

| Service | Vai trò |
|---------|---------|
| **Azure App Service** | Hosting bot Python trên cloud |
| **Azure Cosmos DB (NoSQL)** | Lưu trữ users, products, orders |
| **GitHub Actions** | CI/CD tự động deploy lên Azure |

---

## 📁 Cấu trúc project

```
cosmetic-telegram-bot/
├── app.py                    # Entry point
├── bot/
│   ├── handlers.py           # Xử lý tất cả lệnh
│   ├── keyboards.py          # InlineKeyboard
│   └── messages.py           # Message templates
├── database/
│   ├── cosmos.py             # Kết nối Azure Cosmos DB
│   ├── users.py              # CRUD users
│   ├── products.py           # CRUD products
│   └── orders.py             # CRUD orders
├── data/
│   └── seed_products.py      # Tạo 15 sản phẩm mẫu
├── .env.example              # Mẫu cấu hình
├── requirements.txt
└── README.md
```

---

## ⚙️ Cài đặt và chạy local

### 1. Clone repository
```bash
git clone https://github.com/anky06-ky/Lumibeauty_bot.git
cd Lumibeauty_bot
```

### 2. Tạo môi trường ảo
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Tạo Azure Cosmos DB
1. Vào [portal.azure.com](https://portal.azure.com)
2. Tạo **Azure Cosmos DB for NoSQL** → chọn **Serverless**
3. Lấy **URI** và **Primary Key** trong mục **Keys**

### 4. Cấu hình .env
```bash
copy .env.example .env
```
Điền thông tin vào `.env`:
```
TELEGRAM_TOKEN=your_bot_token
COSMOS_ENDPOINT=https://your-account.documents.azure.com:443/
COSMOS_KEY=your_primary_key
COSMOS_DATABASE=lumibeauty
```

### 5. Tạo dữ liệu mẫu
```bash
python data/seed_products.py
```

### 6. Chạy bot
```bash
python app.py
```

---

## ☁️ Triển khai lên Azure App Service

1. Tạo **App Service** (Python 3.11, Linux, Free F1 tier)
2. **Configuration → Application Settings** → thêm các biến trong `.env`
3. **Deployment Center** → kết nối GitHub → bật CI/CD tự động
4. Bot sẽ tự deploy mỗi khi push code lên GitHub ✅

---

## 🗄️ Azure Cosmos DB – Database Design

| Container | Partition Key | Fields |
|-----------|--------------|--------|
| `users` | `/telegram_id` | telegram_id, username, skintype |
| `products` | `/id` | id, name, price, skintype[], description |
| `orders` | `/user_id` | id, user_id, product_name, quantity, address, status, created_at |

---

## 🛠️ Tech Stack

| Thành phần | Công nghệ |
|-----------|-----------|
| Ngôn ngữ | Python 3.11 |
| Bot Framework | python-telegram-bot v20+ |
| Database | Azure Cosmos DB for NoSQL |
| Cloud Hosting | Azure App Service |
| CI/CD | GitHub → Azure Deployment Center |
| Version Control | GitHub |
