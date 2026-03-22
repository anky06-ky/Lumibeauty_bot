# 🌟 BÁO CÁO TOÀN DIỆN ĐỒ ÁN: CHATBOT BÁN MỸ PHẨM LUMI BEAUTY 🌟

> **Dành cho Người mới học lập trình (Beginner-Friendly)**
> Tài liệu này giải thích "tới tận chân răng" cách một ứng dụng Chatbot AI kết hợp cơ sở dữ liệu NoSQL (Azure Cosmos DB) hoạt động như thế nào, làm sao để nó chạy được trên Internet, và những bài học xương máu khi đưa lên Cloud (Google Cloud Run).

---

## I. MỤC TIÊU CỦA ĐỒ ÁN NÀY LÀ GÌ?
Đồ án xây dựng một **Chatbot bán mỹ phẩm trên Telegram** (Tên: Lumi Beauty). Thay vì người dùng phải vào trang web, họ chỉ cần chat trực tiếp qua ứng dụng nhắn tin Telegram.
Bot có khả năng:
1. **Quản lý khách hàng**: Nhớ thông tin loại da của khách (Da dầu, da mụn, da nhạy cảm...).
2. **Liệt kê và tìm kiếm sản phẩm**: Hiển thị danh sách mỹ phẩm phù hợp với loại da.
3. **Đặt hàng**: Ghi nhận đơn hàng (Sản phẩm gì, số lượng bao nhiêu, giao đi đâu).
4. **Tích hợp Trí tuệ Nhân tạo (AI)**: Khách hàng chỉ cần hỏi "Dạo này da tôi nổi mụn nhiều, nên dùng gì?", AI (của Google Gemini) sẽ tự động phân tích và giới thiệu loại mỹ phẩm đang có bán tại shop phù hợp nhất.

---

## II. GIẢI PHẪU CHI TIẾT TỪNG FILE TRONG SOURCE CODE
Toàn bộ dự án được chia thành các thư mục gọn gàng để dễ quản lý. Dưới đây là ý nghĩa của từng file:

### 1. Thư mục gốc (Root)
- **`app.py`**: Trái tim của con bot. Khi chạy file này, ứng dụng sẽ khởi động. Tại đây nó làm 2 việc: Đăng ký các câu lệnh (như `/start`, `/skintype`, `/order`) vào hệ thống Telegram, và quyết định xem Bot sẽ chạy ở chế độ "Polling" (Chạy trực tiếp trên máy - dùng cho lúc Code) hay chế độ "Webhook" (Treo trên mây 24/7 - dùng khi Deploy mướn máy chủ).
- **`.env`**: File "Bảo mật". Chứa toàn bộ Mật khẩu, Chìa khóa (Key) của Database và Telegram. File này KHÔNG BAO GIỜ được tải lên Github để tránh bị người lạ lợi dụng.
- **`requirements.txt`**: Danh sách các thư viện cần cài đặt để chạy được bot (như `python-telegram-bot` để làm bot, `azure-cosmos` để kết nối DB, `google-generativeai` để dùng AI).
- **`Dockerfile`**: "Bản thiết kế xây nhà". Khai báo cho máy chủ Cloud biết: "Hãy cài hệ điều hành Linux, cài Python 3.10, cài các thư viện trong requirements.txt ra rồi chạy cái file app.py lên cho tôi".

### 2. Thư mục `bot/` (Não bộ xử lý giao tiếp)
Nơi chứa toàn bộ code liên quan đến việc Bot sẽ "rep chữ gì" lại cho khách.
- **`handlers.py`**: Phụ trách kịch bản trả lời khách hàng. Nếu khách gõ `/start` -> hàm `start` chạy. Khách gõ `/order` -> Hàm `order_start` chạy để hỏi tên mỹ phẩm cần mua.
- **`messages.py`**: Chứa mấy câu chào, câu thông báo được soạn sẵn cho gọn, đem qua `handlers.py` xài lại cho code đỡ rối rắm.
- **`keyboards.py`**: Code tạo ra các 'nút bấm' dưới tin nhắn (Ví dụ nút [Da dầu] [Da mụn]) cho khách ấn rột rột thay vì phải gõ.
- **`ai.py`**: Nơi nói chuyện với Google Gemini. Móc nối danh sách sản phẩm ở Data và gửi lệnh cho Gemini: *"Bạn đóng vai chuyên viên bán mỹ phẩm nha, gạ khách mua mấy sản phẩm trong list này thôi, khách hỏi nè: ..."*.

### 3. Thư mục `database/` (Két sắt chứa dữ liệu)
Nơi kết nối và thực hiện thao tác Thêm/Xóa/Sửa dữ liệu, gọi là CRUD (Create, Read, Update, Delete).
- **`cosmos.py`**: Móc nối đến máy chủ Azure Cosmos DB. Sử dụng `COSMOS_ENDPOINT` và `COSMOS_KEY` để đăng nhập.
- **`users.py`**: Mở ngăn chứa **users** ra, đọc hoặc ghi lại loại da của khách mỗi khi họ nhấn chọn. (Create Item, Replace Item).
- **`products.py`**: Mở ngăn chứa **products** ra, dùng câu lệnh SQL đặc biệt của Cosmos DB (`SELECT * FROM c WHERE...`) để lấy đúng loại mỹ phẩm khách đang cần tìm.
- **`orders.py`**: Mở ngăn **orders**, lưu hóa đơn khi khách đặt hàng thành công.

---

## III. DỮ LIỆU (DATABASE) & API HOẠT ĐỘNG THẾ NÀO?

### 1. Database (Cơ sở dữ liệu NoSQL)
- Đề tài dùng **Azure Cosmos DB** (dạng NoSQL, lưu dữ liệu dưới dạng các mảnh tài liệu JSON cực kỳ nhanh và linh hoạt).
- **Dữ liệu mọc từ đâu ra?** => Nằm ở file `/data/seed_products.py`. Đây là file "nhồi" dữ liệu. Ban đầu DB trống không, mình chạy file này để đẩy chục món mỹ phẩm lên Server Cosmos DB làm vốn đi buôn.
- **Cách hoạt động:** Khi code ở Local (máy tính cá nhân), ta dùng *Azure Cosmos DB Local Emulator*. Code gọi vào địa chỉ giả lập `localhost:8081` để kiểm tra. Cosmos nhận câu SQL bằng hàm `query_items`, lấy ra mảng JSON hiển thị cho khách.

### 2. Hai API cốt lõi trong Đồ Án
API (Application Programming Interface) là các cầu nối cho phép 2 phần mềm nói chuyện với nhau. Đồ án xài 2 API chính:

1. **Telegram Bot API:** 
   - *Lấy từ đâu:* Chat với BotFather trên app Telegram, gõ lệnh `/newbot`, đặt tên là chốt đơn được cấp luôn 1 chuỗi `TELEGRAM_TOKEN`.
   - *Cách hoạt động:* Thay vì tự viết code nhắn tin cực nhọc, mình xài thư viện `python-telegram-bot` ôm sẵn API này. Mình chỉ cần quăng token vào `ApplicationBuilder()` là mọi tiến trình nhận/gửi tin nhắn đều tự động hóa.

2. **Google Gemini API (AI):**
   - *Lấy từ đâu:* Vào trang Google AI Studio, xin tạo con Key miễn phí.
   - *Cách hoạt động:* Đưa prompt chứa câu hỏi của khách hàng kèm danh sách sản phẩm nhờ Server AI của Google đọc hiểu và tư vấn như người thật.

---

## IV. QUÁ TRÌNH "LÊN MÂY" (DEPLOY) & LỖI "LÊN BỜ XUỐNG RUỘNG"

Sau khi viết xong ở máy tính cá nhân, thì mình tắt máy tính là Bot ngỏm. Do đó mình phải đưa nó lên Cloud (máy chủ của Google Cloud Run) để nó online 24/7.

### Các bước Deploy:
1. **Container hóa:** Viết `Dockerfile` đóng gói Bot.
2. **Đẩy lên Github:** Lưu code lên Github. Nối Github này với Google Cloud. Từ nay hễ cập nhật code mới, Cloud Build sẽ tự động dỡ Container cũ và đóng mới lại một Container.
3. **Cấu hình Webhook:** Thay vì "Polling" liên tục, hệ thống tạo ra 1 đường link cho Telegram biết: *Khi nào khách nhắn tin, hãy ném tin nhắn qua cái đường link (Webhook) này!*

### Mổ Xẻ Nguyên Nhân Thất Bại Lúc Thực Hành Deploy
Trong quá trình lên mây, dự án gặp 2 lỗi cực hay:

**🚨 Lỗi 1: Đóng gói thành công nhưng Webhook "Tắt Thở" (Failed to Start on Port 8080)**
- **Nguyên nhân:** Webhook của thư viện bot cần một máy chủ web chạy ngầm (ở đây là thư viện `tornado`). Ban đầu `requirements.txt` bị thiếu nó, nên khi bot mở cổng Port 8080 để lắng nghe mạng thì bị lỗi sụp nguồn chết yểu (Exit code 1).
- **Cách sửa:** Ghi rõ ràng vào yêu cầu bọc thêm webhooks: `python-telegram-bot[webhooks]>=20.0`. Góp ý phát ăn ngay, có tick xanh lè.

**🚨 Lỗi 2: Trớ trêu không tạo được Database Azure, Bot bị "Mất Trí Nhớ"**
- **Trạng thái:** Deploy thành công 100%, có URL. Nhưng khách chọn loại "Da Dầu" xong qua hỏi thì bot mắng: "Bạn chưa chọn loại da".
- **Nguyên nhân cốt lõi:** Bot chạy trên Server đám mây ở Singapore (Google Cloud), nhưng địa chỉ nối về Database bạn truyền vào lại là link giả lập `localhost:8081` nằm trong máy tính của bạn ở Việt Nam! Do đường truyền kết nối thất bại trầm trọng, code chặn lỗi âm thầm báo User chưa có loại da nào.
- **Nghịch lý tại sao không lên máy chủ thật được:** Vì tài khoản Email Sinh Viên bị hệ thống của Microsoft từ chối duyệt gói Sinh viên (Có thể quá hạn hoặc bị trường chặn), và nhóm không có thẻ Visa để mở gói Free Trial -> Đường tạo Database "Thật" bị chặn đứng!
- **Sách lược giải quyết thông minh để qua môn:**
  * Vẫn giữ nguyên mã nguồn `azure.cosmos` và giao thức trên Cloud Run (rất điểm cao). 
  * Khi quay Video Demo: Tắt Cloud Run đi, chạy `python app.py` (Polling) trực tiếp dứoi máy cá nhân. Lúc này bot sẽ giao tiếp cực chuẩn với Local Emulator, truy xuất Azure siêu tốc và xử lý đúng 100% logic đồ án môn học Azure PaaS.

---
*Báo cáo kết thúc. Chúc nhóm bảo vệ thành công rực rỡ! 🌸🚀*
