# BÁO CÁO MÔN HỌC: ĐIỆN TOÁN ĐÁM MÂY (CLOUD COMPUTING)
**Đề tài:** Ứng dụng Điện toán đám mây xây dựng Chatbot tư vấn mỹ phẩm tích hợp AI (Lumi Beauty)

---

## I. CÁC ĐIỂM CƠ BẢN CỦA ĐIỆN TOÁN ĐÁM MÂY (ĐTĐM) THỂ HIỆN TRONG DỰ ÁN
Dự án Lumi Beauty Bot tận dụng tối đa 5 đặc trưng cơ bản của Cloud Computing (theo tiêu chuẩn NIST):
1. **On-demand self-service (Tự phục vụ theo nhu cầu):** Các tài nguyên (App Service, Cosmos DB) được khởi tạo và cấu hình tự động thông qua Azure Portal mà không cần tương tác trực tiếp với nhân viên quản trị server.
2. **Broad network access (Truy cập mạng rộng rãi):** Chatbot được truy cập mọi lúc, mọi nơi thông qua nền tảng Telegram trên cả thiết bị di động (Mobile) lẫn máy tính (Desktop).
3. **Resource pooling (Dùng chung tài nguyên):** Hạ tầng máy chủ của Microsoft Azure được chia sẻ, cấp phát cho ứng dụng Web App và Database thông qua cơ chế serverless và resource group ảo hóa.
4. **Rapid elasticity (Co giãn nhanh chóng):** Azure App Service và Cosmos DB có khả năng tự động "Scale up/Scale out" (mở rộng RAM/CPU, tăng RU/s) khi lượng người dùng nhắn tin cho bot tăng đột biến trong các khung giờ cao điểm mua sắm.
5. **Measured service (Dịch vụ đo lường được):** Chi phí sử dụng Cosmos DB và lượng token gọi API Google Gemini được đo lường chính xác theo dung lượng/số request thực tế sử dụng (Pay-as-you-go).

---

## II. PHÂN TÍCH CÁC MÔ HÌNH DỊCH VỤ ĐTĐM TRONG DỰ ÁN (SaaS, PaaS, IaaS)

Dự án này là minh chứng rõ nét cho việc ứng dụng và kết hợp nhiều mô hình dịch vụ ĐTĐM khác nhau:

### 1. PaaS (Platform as a Service) - Trọng tâm của dự án
Toàn bộ dự án được xây dựng và triển khai dựa trên mô hình **PaaS** của hệ sinh thái Microsoft Azure:
- **Azure App Service:** Là một nền tảng PaaS hoàn chỉnh cho việc hosting mã nguồn Python (Webhook/Polling của Bot). Nhóm không cần quan tâm đến Hệ điều hành bên dưới (Ubuntu/Windows), không cần cài đặt Python Runtime thủ công hay cấu hình Nginx/Apache. Azure lo toàn bộ hạ tầng, nhóm chỉ việc "Push code" lên.
- **Azure Cosmos DB:** Database theo mô hình PaaS (NoSQL). Cung cấp khả năng lưu trữ dữ liệu phân tán nhiều khu vực (Global distribution) với độ trễ tính bằng mili-giây mà không cần quản trị viên cấu hình cluster hay backup.

### 2. SaaS (Software as a Service)
- **Telegram Platform:** Giao diện cho người dùng tương tác với hệ thống chính là ứng dụng Telegram. Nhóm tận dụng Telegram như một phần mềm dịch vụ (SaaS) sẵn có để hiển thị nút bấm, Menu, lịch sử chat thay vì phải tự viết một ứng dụng di động tốn kém thời gian.
- **Google Generative AI (Gemini):** Module Trí tuệ nhân tạo được sử dụng theo dạng SaaS (API-as-a-Service). Dịch vụ này nhận dữ liệu đầu vào (Prompt & tin nhắn của user) và trả về nội dung tư vấn sẵn sàng sử dụng.

### 3. IaaS (Infrastructure as a Service)
- Trong phạm vi đồ án để tối ưu hóa thời gian và chi phí, nhóm **KHÔNG** sử dụng mô hình IaaS (ví dụ: Azure Virtual Machines). Việc phải cấp phát Máy ảo (VM), tự cài Hệ điều hành, tự thiết lập tường lửa (Firewall) và tự duy trì server sẽ làm mất đi tính linh hoạt "Serverless" của ứng dụng Chatbot này hiện tại.

---

## III. KIẾN TRÚC TRONG ĐIỆN TOÁN ĐÁM MÂY CỦA HỆ THỐNG

Kiến trúc của dự án tuân theo mô hình **Microservices-oriented & Serverless architecture**:

1. **Client Layer:** Ứng dụng Telegram (iOS/Android/PC).
2. **API Gateway / Middleware:** Telegram Bot API Server đóng vai trò trung gian tiếp nhận và điều hướng tin nhắn.
3. **Compute Layer (Application Logic):** Mã nguồn Python (thư viện `python-telegram-bot`) chạy độc lập (Isolated) trên **Azure App Service**. Chịu trách nhiệm:
   - Phân tích cú pháp tin nhắn (Regex, Command Handlers).
   - Quản lý trạng thái hộp thoại (Conversation States) khi đặt hàng.
4. **AI & Cognitive Services Layer:** Module `ai.py` giao tiếp với **Google Gemini API** qua giao thức HTTPS RESTful để xử lý ngôn ngữ tự nhiên (NLP) cho tính năng `/ask`.
5. **Data Layer:** 
   - Lưu trữ dữ liệu quy mô lớn (Users, Products, Orders) tại **Azure Cosmos DB**.
   - Thiết kế Document-oriented (JSON) phù hợp với cơ sở dữ liệu phi quan hệ, sử dụng Partition Keys để tối ưu hóa chi phí truy vấn.

---

## IV. CÁC MODULE ĐÃ HỌC TRÊN NHÀ CUNG CẤP MICROSOFT AZURE DÙNG TRONG ĐỒ ÁN
*(Tùy chọn mục này theo yêu cầu giảng viên)*

Tuy bài học thực hành trên lớp có sử dụng **Azure Bot Service & Bot Framework Composer**, nhưng để chứng minh khả năng lập trình chuyên sâu, giải quyết bài toán nghiệp vụ phức tạp (như tính giỏ hàng, gọi API AI ngoài), nhóm đã chọn tiếp cận kiến trúc **Code-first** (Sử dụng Python Webhook trên App Service) kết hợp với **Azure Cosmos DB** thay cho luồng kéo-thả (Low-code) của Composer.

**Các dịch vụ Microsoft Cloud áp dụng:**
1. **Azure Active Directory (Entra ID):** Quản lý định danh (Identity), cho phép phân quyền (RBAC) để truy cập an toàn vào Portal dự án.
2. **Azure App Service:** Triển khai mã lệnh Python lên đám mây.
3. **Azure Cosmos DB:** Xây dựng cơ sở dữ liệu phi cấu trúc tốc độ cao, độ trễ thấp.
4. **GitHub x Azure Continuous Deployment (Tùy chọn):** Kết nối mã nguồn từ GitHub tự động cập nhật lên Azure (CI/CD Pipeline) mỗi khi có thay đổi code. 
