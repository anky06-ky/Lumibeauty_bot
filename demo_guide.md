# Hướng Dẫn Demo & Thuyết Trình Dự Án Chatbot Telegram

Tài liệu này cung cấp kịch bản chi tiết để bạn tự tin demo dự án trước hội đồng, giải thích rõ cách hệ thống hoạt động, thao tác với API và cách chứng minh dữ liệu được cập nhật Real-time trên cơ sở dữ liệu.

---

## 1. Khởi động hệ thống (Local)
Để dự án hoạt động, cần chạy song song 2 thành phần: **Cơ sở dữ liệu (Database)** và **Ứng dụng Bot (Python)**.

### Bước 1.1: Bật Database (Azure Cosmos DB Emulator)
1. Mở Start Menu trên Windows, tìm và chạy ứng dụng **Azure Cosmos DB Emulator**.
2. Chờ ứng dụng chạy xong (sẽ có biểu tượng xuất hiện ở khay hệ thống góc dưới màn hình).

### Bước 1.2: Bật Bot Telegram
1. Mở Terminal (Command Prompt / Powershell / VS Code Terminal).
2. Di chuyển vào thư mục dự án `cosmetic-telegram-bot`:
   ```bash
   cd đường_dẫn_tới_thư_mục_dự_án
   ```
3. Chạy lệnh:
   ```bash
   python app.py
   ```
4. Hệ thống báo: `[Lumi Beauty Bot] is running...` là Bot đã sẵn sàng nhận tin nhắn.

---

## 2. Quản Trị Cơ Sở Dữ Liệu (CRUD trực tiếp trên DB)

Để giáo viên thấy trực quan dữ liệu đang được lưu trữ, hãy dùng **Data Explorer** tích hợp sẵn của Azure Emulator.

1. **Truy cập:** Mở trình duyệt Web và truy cập URL: 
   👉 `https://localhost:8081/_explorer/index.html`
   *(Nếu bị cảnh báo SSL "Connection is not private", hãy bấm Advanced -> Proceed to localhost).*
2. **Xem cấu trúc:** 
   - Mở rộng mục `Explorer` bên trái.
   - Click vào database `lumibeauty`.
   - Trong đó sẽ có 3 Collections (bảng): `users`, `products`, và `orders`.

### Thao tác Thêm/Sửa/Xóa (Demo thao tác bằng tay)
- **Xem dữ liệu (Get):** Click vào bảng `products` -> chọn mục `Items`. Danh sách ID của các mỹ phẩm sẽ hiện ra, bấm vào một `id` để xem chi tiết dưới dạng JSON bên phải.
- **Sửa dữ liệu (Update):** Ở giao diện JSON của 1 sản phẩm, thử sửa giá: từ `"price": 320000` thành `"price": 350000` -> bấm nút **Update** ở thanh menu trên -> Ra Telegram gọi `/products` để cho thấy giá đã thay đổi tức thì.
- **Thêm mới (Create):** Bấm nút **New Item** -> dán một mã JSON sản phẩm mới tinh vào (chú ý đổi `id`) -> Bấm **Save** -> Ra Telegram search món đó.
- **Xóa (Delete):** Chọn 1 item -> Bấm nút **Delete Item** hình thùng rác.

---

## 3. Demo Luồng Dữ Liệu (Push / Get qua API)

*(Giải thích cho Hội đồng: "Vì hệ thống giao tiếp qua Telegram Platform (Webhooks/Polling), nên các thao tác GET/POST/PUT/DELETE trên Database được thực hiện gián tiếp thông qua các Command của người dùng")*

### 3.1 Ghi dữ liệu mới (Push / Post / Create)
*Thao tác:* Trên Telegram, gõ lệnh `/start`.
*Giải thích:* 
- Bot đã lấy thông tin `telegram_id` và `username` từ API của Telegram.
- Sau đó **Push** (Insert) bản ghi này vào bảng `users` trên Cosmos DB.
- *(Demo: Mở Data Explorer -> bảng `users` để thấy user mới).*

### 3.2 Lấy và Truy vấn dữ liệu (Get / Read)
*Thao tác:* Gõ lệnh `/products` và `/search serum`.
*Giải thích:*
- Lệnh `/products`: Thực hiện thao tác **GET** toàn bộ bản ghi từ database `products` và parse dữ liệu hiện lên khung chat.
- Lệnh `/search serum`: Dùng Query SQL (`SELECT * FROM c WHERE CONTAINS(c.name, 'serum')`) để lọc dữ liệu trực tiếp dưới tầng Query của DB trả về.

### 3.3 Cập nhật dữ liệu (Update / Patch)
*Thao tác:* Gõ lệnh `/skintype`, bảng Menu hiện ra bấm chọn nút *"Da Khô"*.
*Giải thích:*
- Bot lấy Callback Data từ nút bấm.
- Tìm user tương ứng trong bảng `users` và thực thi lệnh **Update** (hoặc Upsert) trường `"skintype": "da khô"`.
- Dựa trên update này, các lệnh`/recommend` sau đó sẽ Get ra kết quả chính xác theo loại da riêng biệt trên Database.

### 3.4 Quy trình Đặt Hàng (Ghi Record phức tạp)
*Thao tác:* Chạy lệnh `/order`, nhập tên hàng, số lượng, địa chỉ và bấm Xác Nhận.
*Giải thích:* 
- Sử dụng *State Machine* (ConversationHandler) để gom dữ liệu theo từng bước.
- Cuối cùng tiến hành **POST** một Transaction tạo ra `order_id` (UUID) mới nạp vào bảng `orders` kèm mốc thời gian đặt hàng `created_at`.
- *(Demo: Mở bảng `orders` trên Web Explorer cho thầy cô xem đơn hàng vừa rớt vào CSDL).*

---

## 4. Tính năng Nâng cao: Tích hợp AI (Google Gemini)

*Thao tác:* Chat với bot bằng lệnh:
`/ask Da tôi hay đổ dầu vùng chữ T và nổi mụn, dùng sữa rửa mặt nào bên bạn?`

*Giải thích (Point quan trọng ghi điểm cao):*
- *"Hệ thống của em không chỉ rẽ nhánh tĩnh (If/Else) theo Keywords, mà em còn **tích hợp API Trí tuệ Nhân tạo Google Gemini (mô hình 3.0 Flash)**."*
- Hệ thống sẽ ngầm lấy (GET) danh sách mỹ phẩm **đang có thực tế** trong cơ sở dữ liệu (Cosmos DB).
- Nhúng danh sách đó vào `System Prompt` (ngữ cảnh hệ thống) sau đó gọi REST API gửi lên server Google Gemini.
- Gemini phân tích câu hỏi của khách hàng, match với kho dữ liệu để tư vấn trả về câu trả lời tự nhiên nhất như 1 chuyên viên thật.

---
**Tóm tắt tắt hệ thống:**
- Dừng Bot: Focus vào Terminal, nhấn `Ctrl + C`.
- Dừng DB: Chuột phải vào biểu tượng Azure Cosmos Emulator ở Taskbar -> Exit.
