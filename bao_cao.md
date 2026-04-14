# BÁO CÁO ĐỒ ÁN

## ĐỀ TÀI: XÂY DỰNG CHATBOT TƯ VẤN VÀ HỖ TRỢ ĐẶT HÀNG MỸ PHẨM TRÊN NỀN TẢNG TELEGRAM TÍCH HỢP AI

---

## CHƯƠNG 1: GIỚI THIỆU DỰ ÁN

### 1.1 Lý do chọn đề tài

Thị trường mỹ phẩm hiện nay vô cùng phong phú và đa dạng với hàng ngàn dòng sản phẩm khác nhau đến từ vô số thương hiệu. Người tiêu dùng, đặc biệt là phái đẹp, thường xuyên gặp khó khăn trong việc lựa chọn sản phẩm phù hợp với tình trạng làn da của mình (da dầu, da khô, da hỗn hợp, da nhạy cảm,...). Việc sử dụng sai mỹ phẩm không những không mang lại hiệu quả mà còn có thể gây kích ứng và tổn thương da. Theo cách thức mua hàng truyền thống, họ phải liên hệ fanpage hoặc website và chờ đợi nhân viên tư vấn trực tuyến phản hồi. Quá trình này gây mất thời gian, trải nghiệm người dùng bị gián đoạn và trực tiếp làm giảm tỷ lệ chuyển đổi đơn hàng của các doanh nghiệp vừa và nhỏ (SMEs).

Bên cạnh đó, môn học "Các nền tảng phát triển phần mềm" đặt ra yêu cầu sinh viên phải biết ứng dụng các mô hình điện toán đám mây (Cloud Computing) tiên tiến hiện nay vào việc giải quyết các bài toán thực tiễn. Do đó, việc xây dựng một hệ thống chatbot tự động, được lưu trữ, xử lý và vận hành trực tuyến trên nền tảng đám mây (Cloud Platform) không chỉ giải quyết triệt để bài toán chậm trễ trong khâu tư vấn của thị trường mỹ phẩm, mà còn đáp ứng xuất sắc các mục tiêu học thuật về Cloud, API và Backend Development của môn học.

### 1.2 Mục tiêu của dự án

Mục tiêu cốt lõi của dự án là thiết kế, xây dựng và triển khai thành công hệ thống chatbot mang tên Lumi Beauty trên nền tảng nhắn tin bảo mật Telegram. Hệ thống hướng đến việc hoàn thành các mục tiêu cụ thể sau:

- Xây dựng hệ thống luồng hội thoại kịch bản (Rule-based Chatbot) kết hợp với Trí tuệ nhân tạo (AI) thông qua Google Gemini API, với độ trễ thấp để tương tác tự nhiên, thân thiện với người dùng.
- Tự động hóa quá trình xác định loại da thông qua bảng chọn tương tác (Inline Keyboard) và đưa ra gợi ý mỹ phẩm (recommendation) mang tính cá nhân hóa cao dựa trên dữ liệu loại da đã lưu trong cơ sở dữ liệu.
- Quản lý quy trình bán hàng khép kín: từ việc giới thiệu danh mục sản phẩm theo 7 nhóm (Làm sạch & Tẩy trang, Toner & Xịt khoáng, Serum & Tinh chất, Kem dưỡng & Mắt, Kem chống nắng, Mặt nạ & Khác, Tất cả sản phẩm), hỗ trợ công cụ tìm kiếm theo từ khóa (keyword search), xem ảnh sản phẩm minh họa, đến việc ghi nhận đầy đủ thông tin đặt hàng và giao hàng của khách.
- Xây dựng trang quản trị Admin Dashboard bằng Flask để theo dõi thống kê, quản lý người dùng, đơn hàng và sản phẩm trực quan.
- Nắm vững và áp dụng thành công kiến trúc Cloud Platform bằng cách đóng gói ứng dụng qua Docker Container, triển khai trên Render.com và lưu trữ dữ liệu tập trung tại cơ sở dữ liệu đám mây MongoDB Atlas.

### 1.3 Phạm vi dự án

Do giới hạn về thời gian thực hiện (05 tuần theo quy định của đồ án), dự án được khoanh vùng trong phạm vi sau:

- **Đối tượng phục vụ:** Khách hàng cá nhân có nhu cầu tư vấn cơ bản về da và mua sắm các loại mỹ phẩm chăm sóc da mặt (Skincare) trực tuyến.
- **Nền tảng giao tiếp (Frontend):** Ứng dụng Telegram trên các nền tảng Mobile/PC/Web.
- **Tính năng giới hạn:** Tập trung phát triển sâu chức năng tư vấn loại da (Da dầu, Da khô, Da hỗn hợp, Da nhạy cảm), tìm kiếm sản phẩm, xem ảnh minh họa sản phẩm và tạo đơn hàng. Dự án chưa tích hợp xử lý cổng thanh toán trực tuyến (Payment Gateway) và các nghiệp vụ giao hàng phức tạp (Logistics Tracking).

### 1.4 Phân công công việc và tiến độ thực hiện

Để đảm bảo tiến độ dự án, nhóm 3 thành viên đã áp dụng mô hình quản lý dự án linh hoạt, chia nhỏ các nhiệm vụ theo đúng năng lực của từng thành viên:

| STT | Thành Viên | Vai trò & Trách nhiệm chính | Mức độ hoàn thành |
|-----|-----------|------------------------------|-------------------|
| 1 | Trịnh Ngọc Minh Nhật | Telegram Bot Developer: Lập trình Logic Chatbot, thiết lập các lệnh (Commands), xử lý ConversationHandler (quy trình đặt hàng) và Error Handling. | 100% |
| 2 | Trần An Kỳ | Backend & Cloud Engineer: Thiết kế cấu trúc Database, viết các truy vấn dữ liệu. Thiết lập và triển khai (Deploy) hệ thống lên Render.com (Docker). Phân tích cấu trúc API. | 100% |
| 3 | Phan Thanh Tú | BA & Documentation: Phân tích thiết kế hệ thống, thiết kế UI/UX (Figma). Chịu trách nhiệm viết báo cáo kỹ thuật, tài liệu hướng dẫn (Manual) và thiết kế Slide thuyết trình. | 100% |

**Tiến độ thực hiện dự án (Timeline):**

- **Tuần 08 - 09:** Phân tích yêu cầu, đăng ký đề tài. Khởi tạo Telegram Bot qua BotFather. Thiết kế cấu trúc Cơ sở dữ liệu.
- **Tuần 10:** Lập trình Backend (Python). Tích hợp Database MongoDB Atlas. Kiểm thử luồng đặt hàng. Triển khai lên Render.com và tiến hành Deploy. Phân tích API JSON.
- **Tuần 11:** Chạy kiểm thử hệ thống trực tuyến (UAT). Viết tài liệu báo cáo, hoàn thiện hồ sơ dự án, đóng gói source code (zip) và chuẩn bị slide thuyết trình Demo.

### 1.5 Module đã học trên môi trường Điện toán Đám mây liên quan đến đề tài

> **Learning Path:** Introduction to Azure Bot Service and Bot Framework Composer
>
> **Nguồn:** https://learn.microsoft.com/en-us/training/modules/intro-to-bot-service-bot-framework-composer/
>
> **Thời lượng ước tính:** 4 giờ 29 phút | Learning Path | 5 Modules

#### Lý do chọn module này

Module "Introduction to Azure Bot Service and Bot Framework Composer" được lựa chọn vì có liên quan trực tiếp đến đề tài đồ án **"Xây dựng Chatbot tư vấn mỹ phẩm Lumi Beauty trên Telegram"**. Cả hai đều xoay quanh bài toán thiết kế, xây dựng và triển khai chatbot trên nền tảng đám mây Microsoft Azure. Thông qua khóa học này, thành viên nhóm đã nắm vững các khái niệm nền tảng về kiến trúc bot, quy trình hosting trên Azure và cách các dịch vụ Cloud phối hợp với nhau — từ đó áp dụng tư duy kiến trúc tương tự vào dự án Lumi Beauty bằng phương pháp Code-first (Python + Telegram Bot API) thay vì Low-code (Composer).

#### Module 1: Introduction (Giới thiệu)

**Tóm tắt:** Phần này giới thiệu cách thiết kế, xây dựng và triển khai các chatbot thông minh cấp doanh nghiệp bằng Microsoft Bot Framework và Azure Bot Service. Thông qua tình huống thực tế tại một công ty bán lẻ trực tuyến, người học sẽ tìm hiểu cách tự động hóa quy trình chăm sóc khách hàng trên website và mạng xã hội. Giải pháp này tập trung vào việc sử dụng Bot Framework Composer để tạo ra các bot dễ quản lý, có khả năng mở rộng và tích hợp xử lý ngôn ngữ tự nhiên mà không cần tự phát triển các mô hình học máy phức tạp.

**Mục tiêu học tập:**

- Nắm vững các tính năng và chức năng cốt lõi của một chatbot hiện đại.
- Hiểu quy trình thiết kế bot và cách thức vận hành của Azure Bot Service.
- Học cách tạo bot thông qua công cụ trực quan Bot Framework Composer.
- Nhận diện cách các thành phần trong Azure Bot Service phối hợp với nhau trên nền tảng đám mây Azure.

**Yêu cầu tiên quyết:**

- Kinh nghiệm làm việc cơ bản với cổng thông tin Azure (Azure Portal).
- Kiến thức tổng quát về điện toán đám mây.

**Liên hệ với đồ án Lumi Beauty:** Dự án Lumi Beauty cũng bắt đầu từ bài toán tự động hóa tư vấn khách hàng cho ngành bán lẻ mỹ phẩm. Thay vì dùng Bot Framework Composer (Low-code), nhóm chọn phương pháp Code-first bằng Python + `python-telegram-bot` SDK để có toàn quyền kiểm soát logic nghiệp vụ phức tạp (đặt hàng, tích hợp AI Gemini, quản lý trạng thái ConversationHandler).

#### Module 2: What are Bot Service and Bot Framework?

**Tóm tắt:** Phần này làm rõ khái niệm về chatbot và các công cụ hỗ trợ xây dựng chúng từ Microsoft. Bot là ứng dụng tương tác với người dùng qua văn bản, đồ họa hoặc giọng nói để tự động hóa các tác vụ lặp đi lặp lại. Azure Bot Service đóng vai trò là nền tảng lưu trữ (hosting) và quản lý, cung cấp các cơ chế xác thực và tích hợp kênh (Channels). Trong khi đó, Microsoft Bot Framework cung cấp bộ công cụ phát triển toàn diện bao gồm Composer (thiết kế trực quan), SDK (lập trình chuyên sâu) và Emulator (giả lập để kiểm thử).

**Mục tiêu học tập:**

- Phân biệt vai trò của Bot Service (Hạ tầng/Lưu trữ) và Bot Framework (Công cụ phát triển).
- Nắm vững các thành phần cốt lõi: Bot Framework Composer, SDK, và Emulator.
- Tìm hiểu các tính năng chính của một Bot: Tiếp nhận đầu vào, suy luận (reasoning) và phản hồi.
- Nhận diện các công cụ bổ trợ khác như Microsoft Copilot Studio và QnA Maker.

**Nội dung chi tiết:**

- **Azure Bot Service:** Tập hợp các dịch vụ để lưu trữ bot, hỗ trợ đa kênh (SMS, Teams, Web...) và quản lý tài nguyên tập trung qua tài nguyên "Azure Bot".
- **Bot Framework Composer:** IDE mã nguồn mở với canvas thiết kế trực quan, giúp tạo hội thoại, mô hình hiểu ngôn ngữ (LUIS) mà không cần viết nhiều code.
- **Bot Framework SDK:** Bộ thư viện modular (C#, JS, Python, Java) để mở rộng các tác vụ phức tạp như tích hợp dịch vụ bên thứ ba.
- **Bot Framework Emulator:** Ứng dụng desktop để chat thử với bot và kiểm tra các gói tin JSON được trao đổi trước khi triển khai lên Cloud.

**Liên hệ với đồ án Lumi Beauty:** Trong dự án Lumi Beauty, vai trò tương đương với Azure Bot Service là **Render.com** (hosting mã nguồn Python qua Docker) kết hợp **MongoDB Atlas** (lưu trữ dữ liệu). Vai trò tương đương Bot Framework SDK chính là thư viện `python-telegram-bot` v20+ — đều là bộ công cụ lập trình để xây dựng logic bot. Thay vì dùng Bot Framework Emulator, nhóm sử dụng chế độ **Long Polling** (`app.run_polling()`) để kiểm thử trực tiếp trên ứng dụng Telegram thật trong giai đoạn phát triển.

#### Module 3: How Azure Bot Service Works

**Tóm tắt:** Giai đoạn này tập trung vào quy trình khép kín từ thiết kế đến triển khai bot. Bot package (gói bot) bao gồm logic hội thoại, tích hợp kênh và mã nguồn tùy chỉnh, được lưu trữ trên Azure dưới dạng một Web App. Việc sử dụng Composer cho phép xây dựng các luồng hội thoại (Dialogs) phức tạp, tích hợp AI mạnh mẽ (LUIS, QnA Maker) và kiểm thử trực tiếp trong môi trường local trước khi phát hành lên Cloud.

**Mục tiêu học tập:**

- Hiểu kiến trúc của một bot package và cách nó được host trên Azure Bot Service.
- Xác định các yếu tố then chốt khi lập kế hoạch xây dựng bot: mục đích, đối tượng người dùng và nền tảng sử dụng.
- Nắm vững cách xây dựng luồng hội thoại (Dialogs) và sử dụng các yếu tố trực quan như Cards để tăng trải nghiệm người dùng.
- Hiểu cách mở rộng khả năng ngôn ngữ với LUIS/QnA Maker và tích hợp code qua SDK.

**Nội dung chi tiết:**

- **Lập kế hoạch thiết kế:** Ưu tiên trải nghiệm người dùng (UX) bằng cách trả lời các câu hỏi: Bot giải quyết vấn đề gì? Ai là người dùng? Bot chạy trên nền tảng nào (Mobile, Web, Teams...)?
- **Xây dựng với Composer:**
  - *Dialogs:* Điều khiển luồng hội thoại, từ đơn giản (hỏi-đáp) đến phức tạp (vòng lặp, rẽ nhánh, ngắt quãng).
  - *Skills:* Đóng gói các chức năng (như quản lý lịch) thành các module có thể tái sử dụng cho nhiều bot khác nhau.
  - *Visual Elements:* Sử dụng Cards, hình ảnh và nút bấm để tạo nội dung phong phú thay vì chỉ văn bản thuần túy.
- **Tích hợp AI & Kiểm thử:**
  - *LUIS & QnA Maker:* Cung cấp khả năng hiểu ngôn ngữ tự nhiên và trích xuất câu hỏi từ tài liệu FAQ sẵn có.
  - *Web Chat:* Công cụ kiểm thử tích hợp ngay trong Composer để gỡ lỗi và kiểm tra trạng thái bot mà không cần publish.
- **Mở rộng & Triển khai:** Sử dụng Bot Framework SDK (Visual Studio/VS Code) để viết thêm middleware hoặc tính năng đặc thù, sau đó publish trực tiếp từ Composer lên Azure App Service.

**Liên hệ với đồ án Lumi Beauty:** Khái niệm **Dialogs** trong Bot Framework tương đương với `ConversationHandler` trong `python-telegram-bot` mà nhóm sử dụng để quản lý luồng đặt hàng 5 bước (CHOOSE_PRODUCT → ENTER_QUANTITY → ENTER_NAME → ENTER_ADDRESS → CONFIRM_ORDER). Khái niệm **Visual Elements (Cards, nút bấm)** tương đương với **Inline Keyboard** mà nhóm triển khai cho chọn loại da (4 nút), chọn danh mục sản phẩm (7 nút) và xác nhận đơn hàng (2 nút). Thay vì dùng LUIS để xử lý ngôn ngữ tự nhiên, nhóm tích hợp **Google Gemini AI** với kỹ thuật Dynamic Prompting để tư vấn dựa trên kho sản phẩm thực tế.

#### Module 4: When to Use the Azure Bot Service and Bot Framework

**Tóm tắt:** Việc lựa chọn công cụ phụ thuộc vào yêu cầu về độ phức tạp và khả năng tùy chỉnh. Đối với các kịch bản doanh nghiệp yêu cầu sự kết hợp giữa thiết kế nhanh và khả năng mở rộng sâu bằng code, Bot Framework Composer là lựa chọn hàng đầu. Nó vượt trội hơn các giải pháp no-code đơn thuần nhờ khả năng tích hợp sẵn AI và cho phép can thiệp vào mã nguồn qua SDK.

**Mục tiêu học tập:**

- Xác định các tiêu chí quan trọng khi chọn công cụ: tính đơn giản, khả năng mở rộng và tích hợp NLP.
- So sánh ba công cụ chính: Microsoft Copilot Studio, QnA Maker và Bot Framework Composer.
- Hiểu lý do tại sao Composer là giải pháp cân bằng nhất cho các nhu cầu AI hội thoại chuyên nghiệp.

**Nội dung chi tiết:**

- **Yêu cầu từ doanh nghiệp:** Bot phải dễ tạo/quản lý nhưng cũng phải dễ mở rộng bằng mã nguồn và tích hợp sẵn khả năng hiểu ngôn ngữ tự nhiên mà không cần tự phát triển mô hình Machine Learning.
- **Đánh giá các công cụ:**
  - *Microsoft Copilot Studio (Power Virtual Agents):* Giao diện no-code tuyệt vời cho người dùng không chuyên. Tuy nhiên, hạn chế trong việc tích hợp sâu các tài nguyên LUIS cấu hình sẵn, không phù hợp cho các kịch bản tùy biến cao.
  - *QnA Maker:* Tối ưu để biến tài liệu tĩnh (FAQ, PDF) thành lớp hỏi-đáp hội thoại. Hạn chế lớn nhất là không hỗ trợ tùy chỉnh trực tiếp luồng hội thoại và logic kinh doanh phức tạp.
  - *Bot Framework Composer & Azure Bot Service:* Là "điểm ngọt" (sweet spot) vì cung cấp IDE trực quan cho nhà phát triển, hỗ trợ mạnh mẽ LUIS/QnA Maker và cho phép dùng SDK để xử lý các logic phức tạp (như gọi REST API).
- **Kết luận:** Bot Framework Composer được lựa chọn vì đáp ứng hoàn hảo cả 3 yêu cầu: trực quan, tích hợp AI mạnh mẽ và khả năng mở rộng không giới hạn qua mã nguồn.

**Liên hệ với đồ án Lumi Beauty:** Dự án Lumi Beauty đã lựa chọn phương pháp **Code-first** (Python Webhook trên Render.com kết hợp MongoDB Atlas) thay vì Low-code (Composer) hay No-code (Copilot Studio). Lý do là vì đề tài yêu cầu xử lý nghiệp vụ phức tạp: tính giỏ hàng, quản lý ConversationHandler đa bước, tích hợp Google Gemini API bên ngoài hệ sinh thái Microsoft, và xây dựng Admin Dashboard bằng Flask. Đây chính là minh chứng cho việc sử dụng SDK mở rộng mà Module 4 đề cập — khi yêu cầu vượt quá khả năng của các công cụ trực quan, lập trình viên cần can thiệp trực tiếp vào mã nguồn.

#### Module 5: Kiểm tra kiến thức (Module Assessment)

**Kết quả:** Đã hoàn thành bài kiểm tra trắc nghiệm với kết quả đạt **100%**. Các kiến thức cốt lõi đã được xác nhận bao gồm:

| Chủ đề | Kiến thức xác nhận |
|--------|-------------------|
| Công cụ thiết kế trực quan | **Bot Framework Composer** là công cụ chính cho phép xây dựng bot bằng giao diện thiết kế trực quan thay vì chỉ dùng code như SDK. |
| Xử lý ngôn ngữ tự nhiên (NLP) | Trong Composer, **LUIS** là dịch vụ tích hợp sẵn cung cấp khả năng xử lý ngôn ngữ tự nhiên chuyên sâu (như nhận diện ý định và thực thể). |
| Kiểm soát luồng hội thoại | **Dialogs** là tính năng duy nhất trong Composer chuyên dùng để quản lý và điều khiển luồng hội thoại giữa người dùng và bot. |

#### Bảng tổng hợp: So sánh kiến trúc Azure Bot Service với Lumi Beauty

| Thành phần Azure Bot Service | Vai trò | Thành phần tương đương trong Lumi Beauty | Ghi chú |
|------------------------------|---------|------------------------------------------|---------|
| Azure Bot Service | Hosting & quản lý bot | Render.com + Docker Container | Sử dụng Cloud PaaS |
| Bot Framework Composer | IDE trực quan thiết kế bot | Visual Studio Code + Python | Nhóm chọn Code-first thay vì Low-code |
| Bot Framework SDK | Thư viện lập trình mở rộng | `python-telegram-bot` v20+ | Cùng vai trò: SDK xử lý logic bot |
| Bot Framework Emulator | Kiểm thử local | Chế độ Long Polling + Telegram App | Kiểm thử trực tiếp trên Telegram thật |
| LUIS (Language Understanding) | NLP - Hiểu ngôn ngữ tự nhiên | Google Gemini AI + Dynamic Prompting | Gemini mạnh hơn: sinh hội thoại tự nhiên |
| QnA Maker | Hỏi-đáp từ tài liệu FAQ | Danh sách sản phẩm từ MongoDB Atlas | Dữ liệu sản phẩm được nạp vào AI prompt |
| Channels (Teams, Web, SMS) | Đa kênh giao tiếp | Telegram Bot API | Tập trung vào 1 kênh Telegram |
| Dialogs | Quản lý luồng hội thoại | ConversationHandler (5 states) | Cùng mục đích: quản lý state machine |
| Cards & Visual Elements | UI phong phú trong chat | Inline Keyboard (4+7+2 nút) | Telegram hỗ trợ nút bấm tương tác |

---

## CHƯƠNG 2: CƠ SỞ LÝ THUYẾT VÀ CÔNG NGHỆ SỬ DỤNG

### 2.1 Chatbot và xu hướng tự động hóa chăm sóc khách hàng

Trong lĩnh vực làm đẹp, khách hàng luôn cần sự tư vấn cá nhân hóa dựa trên tình trạng làn da của họ. Để giải quyết bài toán này, thay vì chỉ sử dụng mô hình Rule-based Chatbot (Chatbot theo kịch bản cứng nhắc), nhóm đã quyết định tích hợp mô hình ngôn ngữ lớn Gemini AI thông qua API. Cụ thể, hệ thống sử dụng mô hình `gemini-2.0-flash` với cơ chế Model Fallback (tự động chuyển sang `gemini-1.5-flash` nếu model chính gặp lỗi) để đảm bảo tính ổn định.

Đặc biệt, để khắc phục nhược điểm "ảo giác" (Hallucination) – khi AI tự động bịa ra các sản phẩm không có thật, hệ thống Lumi Beauty đã áp dụng kỹ thuật Prompt Engineering động (Dynamic Prompting). Bot sẽ gọi hàm `_product_list_for_prompt()` để truy xuất trực tiếp toàn bộ danh sách 65 mỹ phẩm hiện có từ MongoDB Atlas, nạp vào System Prompt và ép Gemini chỉ được phép tư vấn trong phạm vi kho hàng thực tế. Ngoài ra, AI được cấu hình để đóng vai "Lumi – chuyên gia tư vấn mỹ phẩm", trả lời tối đa 250 chữ, và bắt buộc phải hướng dẫn khách gõ lệnh `/order` khi muốn mua hàng thay vì tự mình chốt đơn. Điều này giúp chatbot vừa có sự giao tiếp mềm mỏng, tự nhiên của AI, vừa đảm bảo tính chính xác tuyệt đối trong khâu bán hàng.

### 2.2 Nền tảng Telegram Bot API và cơ chế hoạt động

Telegram là một trong những nền tảng nhắn tin phổ biến nhất toàn cầu, nổi tiếng với tốc độ, bảo mật mã hóa và một hệ sinh thái hỗ trợ lập trình viên xây dựng bot vô cùng mạnh mẽ thông qua HTTP API. Trong kiến trúc của Lumi Beauty, Telegram Bot đóng vai trò là giao diện người dùng (Front-end). Ưu điểm của việc dùng Telegram:

- **Zero-Installation:** Người dùng không cần phải tải thêm bất kỳ ứng dụng mua sắm nào, không cần tạo tài khoản mật khẩu phức tạp. Mọi thứ được đồng bộ qua định danh `telegram_id`.
- **UI Elements phong phú:** Telegram API hỗ trợ gửi văn bản, hình ảnh, cũng như tạo các bảng chọn tương tác (Inline Keyboard), giúp trải nghiệm mua sắm trở nên trực quan giống như một Mini-App. Hệ thống sử dụng Inline Keyboard cho việc chọn loại da (4 nút: Da dầu, Da khô, Da hỗn hợp, Da nhạy cảm), chọn danh mục sản phẩm (7 nút theo nhóm), và xác nhận/hủy đơn hàng.
- **Cơ chế giao tiếp:** Bot của nhóm sử dụng cơ chế Long Polling (`app.run_polling()`) trong quá trình phát triển (Backend liên tục gọi lên Telegram Server để kiểm tra tin nhắn mới) và cơ chế Webhook (`app.run_webhook()`) khi đưa lên môi trường Production trên Render.com (Telegram tự động đẩy tin nhắn về Server ngay khi có phát sinh), giúp tối ưu hóa tài nguyên mạng. Biến môi trường `ENVIRONMENT` quyết định chế độ chạy.

### 2.3 Ngôn ngữ lập trình Python và kiến trúc Bất đồng bộ (Asyncio)

Dự án được viết hoàn toàn bằng ngôn ngữ lập trình Python kết hợp với thư viện `python-telegram-bot` (phiên bản v20+). Python được chọn làm ngôn ngữ core backend vì cú pháp vô cùng rõ ràng, hệ sinh thái thư viện khổng lồ và đặc biệt tối ưu cho các tác vụ xử lý chuỗi và phát triển ứng dụng mạng. Điểm nổi bật về mặt kỹ thuật trong mã nguồn của nhóm là việc sử dụng triệt để kiến trúc Bất đồng bộ (Asynchronous Programming với `async/await`). Tất cả các hàm xử lý lệnh trong `bot/handlers.py` đều được khai báo là `async def`, cho phép máy chủ xử lý hàng trăm tin nhắn của các khách hàng khác nhau cùng một lúc mà không bị treo. Đồng thời, cơ chế `ConversationHandler` của thư viện được sử dụng để duy trì trạng thái ngữ cảnh (State Management) cho luồng đặt hàng qua 5 trạng thái: `CHOOSE_PRODUCT` → `ENTER_QUANTITY` → `ENTER_NAME` → `ENTER_ADDRESS` → `CONFIRM_ORDER`, giúp bot "nhớ" được người dùng đang ở bước nào trong quy trình.

### 2.4 Nền tảng điện toán đám mây và triển khai

Để đáp ứng yêu cầu cốt lõi của môn học về việc triển khai trên Cloud Platform, hệ thống được thiết kế theo mô hình PaaS (Platform as a Service), giúp tách biệt hoàn toàn rủi ro quản lý hạ tầng vật lý:

- **Render.com (Web Service):** Là nền tảng Cloud PaaS hỗ trợ triển khai ứng dụng Docker Container tự động từ GitHub repository. Nhóm sử dụng Render Free Plan để chạy bot 24/7 với chế độ Webhook. Render cung cấp sẵn chứng chỉ bảo mật SSL/TLS, tên miền HTTPS (`https://lumi-beauty-bot.onrender.com`) và cho phép cấu hình các Biến môi trường (Environment Variables) để bảo mật `TELEGRAM_TOKEN`, `MONGO_URI`, `GEMINI_API_KEY` một cách an toàn nhất.
- **MongoDB Atlas (NoSQL):** Để lưu trữ dữ liệu, nhóm sử dụng cơ sở dữ liệu phi cấu trúc MongoDB Atlas (gói Free Tier M0, 512MB). Hệ thống tổ chức dữ liệu thành 3 collection: `users` (thông tin khách hàng), `products` (danh mục sản phẩm) và `orders` (đơn hàng). Cấu trúc linh hoạt của NoSQL cho phép dễ dàng thêm bớt các trường thông tin của mỹ phẩm mà không làm gãy vỡ (break) hệ thống cơ sở dữ liệu đang vận hành. Kết nối qua thư viện `pymongo[srv]`.

---

## CHƯƠNG 3: PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG

### 3.1 Phân tích yêu cầu và Biểu đồ Use Case

Từ các bài toán thực tế đã khảo sát, hệ thống Lumi Beauty Chatbot cần giải quyết hai nhóm tác nhân chính:

1. **Khách hàng (User):** Cần một công cụ để tra cứu thông tin nhanh, muốn biết da mình hợp với cái gì và muốn thao tác đặt hàng ít rườm rà nhất. Ngoài ra, khách hàng có thể chat tự nhiên bằng tiếng Việt để được AI tư vấn chuyên sâu.
2. **Quản trị viên (Admin):** Cần theo dõi thống kê (số người dùng, đơn hàng, doanh thu), quản lý trạng thái đơn hàng, xem danh sách sản phẩm và gửi thông báo tới khách hàng qua Telegram khi cập nhật đơn hàng.

Hình 3.1: Biểu đồ tình huống sử dụng (Use Case Diagram) của hệ thống.

### 3.2 Kiến trúc hệ thống trên Cloud

Hệ thống được thiết kế theo mô hình kiến trúc Micro-services cơ bản trên nền tảng đám mây, đảm bảo khả năng tách rời và mở rộng độc lập:

Hình 3.2: Kiến trúc tổng thể của hệ thống triển khai trên Cloud.

- **Tầng Client (Giao diện):** Ứng dụng Telegram trên thiết bị người dùng (Mobile/PC/Web) và trình duyệt Web để truy cập Admin Dashboard.
- **Tầng Integration (Tích hợp API):** Telegram Bot API tiếp nhận và mã hóa tin nhắn JSON. Google Gemini API xử lý yêu cầu tư vấn bằng ngôn ngữ tự nhiên.
- **Tầng Application (Xử lý cốt lõi):** Chạy trên Render.com (Docker Container), gồm hai thành phần:
  - **Bot Server** (`app.py`): Dùng thư viện `python-telegram-bot` xử lý các Command Handler, Callback Query Handler, Message Handler và Conversation Handler.
  - **Dashboard Server** (`dashboard.py`): Ứng dụng Flask cung cấp REST API (`/api/stats`, `/api/users`, `/api/orders`, `/api/products`) và giao diện quản trị web.
- **Tầng Data (Dữ liệu):** MongoDB Atlas lưu trữ dữ liệu theo thời gian thực trong 3 collection: `users`, `products`, `orders`.

### 3.3 Sơ đồ tuần tự (Sequence Diagram) luồng Đặt hàng

Sơ đồ tuần tự thể hiện rõ giao tiếp dữ liệu giữa người dùng, hệ thống bot và cơ sở dữ liệu trong quá trình quan trọng nhất: Đặt hàng.

Hình 3.3: Biểu đồ tuần tự biểu diễn quá trình khởi tạo và xác nhận Đơn hàng.

Giải thích luồng chạy:

1. Khách hàng gửi lệnh `/order` tới Telegram.
2. Telegram API đẩy dữ liệu về Server trên Render.com. Bot phản hồi: "Vui lòng nhập tên sản phẩm bạn muốn đặt".
3. Khách hàng nhập tên sản phẩm. Bot tìm kiếm sản phẩm trong Database (tìm chính xác bằng `get_product_by_name()`, nếu không tìm thấy sẽ tìm gần đúng bằng `search_products()`). Nếu tìm thấy, bot lưu thông tin sản phẩm vào `context.user_data` và hỏi số lượng.
4. Khách hàng nhập số lượng. Bot kiểm tra tính hợp lệ (phải là số nguyên dương), sau đó hỏi họ tên người nhận hàng.
5. Khách hàng nhập họ tên. Bot lưu và hỏi địa chỉ giao hàng.
6. Khách hàng nhập địa chỉ. Bot tổng hợp toàn bộ thông tin và hiển thị bảng xác nhận kèm 2 nút Inline Keyboard: "✅ Xác nhận đặt hàng" và "❌ Hủy".
7. Nếu khách xác nhận, bot gọi `orders.create_order()` để tạo đơn hàng mới với `order_id` là UUID tự sinh, `status` mặc định là "Đang xử lý", và `created_at` là thời điểm hiện tại. Bot gửi tin nhắn "Đặt hàng thành công" kèm mã đơn hàng cho khách.

### 3.4 Danh sách chức năng (Function List)

| Tên chức năng | Lệnh (Command) | Quy trình thực thi hệ thống |
|---------------|-----------------|------------------------------|
| Bắt đầu | `/start` | Khởi tạo phiên làm việc mới. Lưu `telegram_id` và `full_name` vào container `users`. Gửi thông điệp chào mừng và danh sách 8 lệnh hỗ trợ. |
| Khảo sát da | `/skintype` | Hiển thị Inline Keyboard với 4 nút chọn (Da dầu, Da khô, Da hỗn hợp, Da nhạy cảm). Khi chọn, cập nhật trường `skintype` của user vào Database bằng `update_one()`. |
| Gợi ý | `/recommend` | Đọc `skintype` hiện tại từ collection `users`. Truy vấn sản phẩm bằng `find({"skintype": skin})` và trả về tối đa 8 sản phẩm phù hợp. |
| Xem danh mục | `/products` | Hiển thị Inline Keyboard gồm 7 nút danh mục. Khi chọn danh mục, bot lọc sản phẩm theo từ khóa trong tên và gửi kèm ảnh minh họa từ thư mục `img/`. |
| Tìm kiếm | `/search [từ khóa]` | Bóc tách từ khóa. So khớp chuỗi (String Matching) trong Python trên toàn bộ sản phẩm từ Database. Trả về kết quả nếu tìm thấy. |
| Xem ảnh | `/xem [tên SP]` | Tìm sản phẩm theo từ khóa, hiển thị ảnh minh họa kèm thông tin chi tiết (giá, loại da, mô tả). Ảnh được ưu tiên lấy từ thư mục `img/` local. |
| Lên đơn | `/order` | Kích hoạt chuỗi ConversationHandler 5 bước: Tên SP → Số lượng → Họ tên người nhận → Địa chỉ → Xác nhận. |
| Lịch sử | `/myorder` | Truy vấn collection `orders` với `find({"user_id": uid}).sort("created_at", -1).limit(10)`, giới hạn 10 đơn gần nhất. |
| Tư vấn AI | `/ask [câu hỏi]` | Gọi Google Gemini API với Dynamic Prompt chứa danh sách sản phẩm thực tế từ Database. |
| Chat tự nhiên | *(nhắn tin bất kỳ)* | Mọi tin nhắn không bắt đầu bằng `/` sẽ được tự động gửi đến Gemini AI để tư vấn. |

### 3.5 Thiết kế cơ sở dữ liệu (Data Dictionary)

Hệ thống sử dụng cơ sở dữ liệu NoSQL MongoDB Atlas với cấu trúc Document (JSON). Database có tên `lumibeauty` chứa 3 collection:

**1. Collection: `users` (Khách hàng)**

- `id` (String): Khóa chính, bằng giá trị `telegram_id`. Ví dụ: `"123456789"`.
- `telegram_id` (String): Định danh duy nhất của người dùng trên Telegram.
- `username` (String): Tên hiển thị `full_name` trên Telegram. Mặc định `"Khách hàng"` nếu null.
- `skintype` (String | null): Lưu trạng thái da bằng tiếng Việt: `"da dầu"`, `"da khô"`, `"da hỗn hợp"`, `"da nhạy cảm"`. Mặc định là `null`.

**2. Collection: `products` (Sản phẩm)**

- `id` (String): Khóa chính, chuỗi UUID tự sinh.
- `name` (String): Tên đầy đủ của mỹ phẩm. Ví dụ: `"Sữa rửa mặt kiểm soát dầu CeraVe"`.
- `price` (Number): Mức giá bán (VNĐ). Ví dụ: `280000`.
- `skintype` (Array of String): Mảng chứa các loại da có thể sử dụng. Ví dụ: `["da dầu", "da hỗn hợp"]`.
- `description` (String): Công dụng và hướng dẫn sử dụng.
- `image` (String): Tên file ảnh trong thư mục `img/`. Ví dụ: `"srmCerave.jpg"`.
- `image_url` (String): URL ảnh dự phòng (placeholder).

**3. Collection: `orders` (Đơn đặt hàng)**

- `id` (String): Chuỗi UUID tự sinh bằng `uuid.uuid4()`.
- `user_id` (String): Khóa ngoại, `telegram_id` của người đặt.
- `customer_name` (String): Họ tên người nhận hàng do khách nhập.
- `product_name` (String): Tên sản phẩm khách đặt.
- `quantity` (Integer): Số lượng sản phẩm (bắt buộc > 0).
- `address` (String): Địa chỉ giao nhận.
- `status` (String): Trạng thái đơn hàng. Mặc định: `"Đang xử lý"`. Có thể chuyển sang `"Đã giao"` hoặc `"Đã hủy"` qua Admin Dashboard.
- `created_at` (String): Dấu thời gian ISO 8601 lúc chốt đơn, sinh bằng `datetime.now().isoformat()`.

#### 3.5.1: Minh họa cấu trúc JSON

```json
// Cấu trúc Collection: products
{
  "id": "a1b2c3d4-e5f6-...",
  "name": "Serum Niacinamide 10% The Ordinary",
  "price": 350000,
  "skintype": ["da dầu", "da hỗn hợp"],
  "description": "Thu nhỏ lỗ chân lông, giảm thâm mụn, kiểm soát dầu.",
  "image": "serum_10%nia_ordinary.jpg",
  "image_url": "https://picsum.photos/seed/lumibeauty-004/600/600"
}

// Cấu trúc Collection: users
{
  "id": "123456789",
  "telegram_id": "123456789",
  "username": "Minh Nhật",
  "skintype": "da dầu"
}

// Cấu trúc Collection: orders
{
  "id": "f47ac10b-58cc-...",
  "user_id": "123456789",
  "customer_name": "Nguyễn Văn A",
  "product_name": "Serum Niacinamide 10% The Ordinary",
  "quantity": 2,
  "address": "Quận 1, TP.HCM",
  "status": "Đang xử lý",
  "created_at": "2026-04-07T09:30:00.123456"
}
```

### 3.6 Sơ đồ luồng xử lý đặt hàng (Flowchart)

Để xử lý ngoại lệ (Exception Handling), đặc biệt là trường hợp khách hàng cố tình nhập sai định dạng, hệ thống áp dụng luồng kiểm tra dữ liệu nghiêm ngặt tại mỗi bước:

Hình 3.6: Lưu đồ thuật toán xử lý ngoại lệ (Error Handling) của luồng đặt hàng.

- **Bước nhập tên sản phẩm:** Nếu sản phẩm không tồn tại chính xác trong Database, hệ thống tự động tìm kiếm gần đúng bằng `search_products()`. Nếu vẫn không tìm thấy, bot yêu cầu nhập lại.
- **Bước nhập số lượng:** Sử dụng `int()` để chuyển đổi và kiểm tra `qty <= 0` với `try/except ValueError`. Nếu không hợp lệ, bot thông báo "Số lượng không hợp lệ. Vui lòng nhập số nguyên dương" và yêu cầu nhập lại.
- **Bước xác nhận:** Khách có thể bấm "❌ Hủy" bất kỳ lúc nào hoặc gõ `/cancel` để hủy toàn bộ quy trình đặt hàng.

### 3.7 Đặc tả giao thức giao tiếp và Cấu trúc API (API Specification)

Một phần cốt lõi của hệ thống Chatbot chính là quá trình trao đổi dữ liệu qua lại (Request-Response Flow) giữa máy chủ Telegram và Backend Python triển khai trên Cloud.

**Cơ chế hoạt động:** Khi người dùng gửi một tin nhắn trên ứng dụng Telegram, máy chủ Telegram sẽ sinh ra một Update object và bắn một POST Request mang theo chuỗi dữ liệu định dạng JSON tới Webhook URL trên Render.com của nhóm.

**1. Cấu trúc JSON Request (Từ Telegram gửi tới Backend):**

Ví dụ khi khách hàng gõ lệnh `/skintype`, chuỗi JSON thực tế (Payload) mà máy chủ Python nhận được sẽ có cấu trúc như sau:

```json
{
  "update_id": 987654321,
  "message": {
    "message_id": 105,
    "from": {
      "id": 123456789,
      "is_bot": false,
      "first_name": "Anh",
      "username": "anh_nguyen",
      "language_code": "vi"
    },
    "chat": {
      "id": 123456789,
      "first_name": "Anh",
      "username": "anh_nguyen",
      "type": "private"
    },
    "date": 1698765432,
    "text": "/skintype",
    "entities": [
      {
        "offset": 0,
        "length": 9,
        "type": "bot_command"
      }
    ]
  }
}
```

**Phân tích kiểu dữ liệu (Data Types) trong Request:**

- `update_id` (Integer): ID định danh duy nhất cho mỗi bản ghi cập nhật, dùng để tránh xử lý trùng lặp.
- `from.id` (Integer): Chính là `telegram_id` sẽ được hệ thống trích xuất và chuyển thành String để lưu vào cơ sở dữ liệu Database thông qua hàm `save_user(user.id, display_name)`.
- `text` (String): Nội dung tin nhắn người dùng nhập. Thư viện `python-telegram-bot` tự động phân luồng dựa trên `CommandHandler` đã đăng ký trong `app.py`.
- `entities.type` (String): Telegram tự động nhận diện chuỗi có dấu `/` ở đầu là một `bot_command` (lệnh bot).

**2. Cấu trúc JSON Response (Từ Backend phản hồi lại Telegram):**

Sau khi xử lý logic, hệ thống Python sẽ gọi một HTTP POST Request tới Endpoint API của Telegram: `https://api.telegram.org/bot<TOKEN>/sendMessage`.

Ví dụ chuỗi JSON hệ thống gửi đi để phản hồi:

```json
{
  "chat_id": 123456789,
  "text": "💆 *Hãy cho tôi biết loại da của bạn nhé!*\n\nChọn loại da bên dưới để tôi gợi ý sản phẩm phù hợp nhất cho bạn:",
  "parse_mode": "Markdown",
  "reply_markup": {
    "inline_keyboard": [
      [
        {"text": "🌟 Da dầu", "callback_data": "skin_oily"},
        {"text": "💧 Da khô", "callback_data": "skin_dry"}
      ],
      [
        {"text": "✨ Da hỗn hợp", "callback_data": "skin_combo"},
        {"text": "🌸 Da nhạy cảm", "callback_data": "skin_sensitive"}
      ]
    ]
  }
}
```

**Phân tích kiểu dữ liệu trong Response:**

- `chat_id` (Integer): Mã phòng chat, lấy trực tiếp từ `message.chat.id` của Request.
- `text` (String): Chuỗi văn bản tư vấn. Hỗ trợ định dạng Markdown với `*in đậm*` và `_in nghiêng_`.
- `parse_mode` (String): Quy định định dạng văn bản (Markdown) để hiển thị chữ in đậm, in nghiêng trên giao diện người dùng.
- `reply_markup` (Object): Đối tượng Inline Keyboard chứa mảng các nút bấm tương tác, mỗi nút có `text` hiển thị và `callback_data` để backend nhận diện lựa chọn.

Nhờ việc trích xuất và xử lý đúng định dạng JSON này, hệ thống đảm bảo duy trì tính ổn định, tách biệt hoàn toàn Logic Code và Giao diện UI.

---

## CHƯƠNG 4: SO SÁNH, PHÂN TÍCH SWOT VÀ ĐỀ XUẤT GIẢI PHÁP

### 4.1 So sánh với các ứng dụng tương tự (Compare similar apps)

Để kiểm chứng tính khả thi và tối ưu của Lumi Beauty, nhóm đã tiến hành khảo sát và đánh giá với 2 hệ thống Chatbot/Trợ lý ảo nổi bật trong ngành bán lẻ mỹ phẩm hiện nay: Chatbot Fanpage Hasaki (Facebook Messenger) và Trợ lý ảo Shopee Beauty (In-app).

| Tiêu chí | Chatbot Hasaki (Facebook) | Trợ lý Shopee Beauty | Lumi Beauty (Sản phẩm nhóm) |
|----------|--------------------------|---------------------|------------------------------|
| Nền tảng host | Messenger (Thuộc Meta) | App Shopee Nội bộ | Telegram API |
| Tốc độ tải (Latency) | Chậm. Thường bị độ trễ do tải nhiều hình ảnh quảng cáo động. | Phụ thuộc cấu hình điện thoại. App nặng dễ gây giật lag. | Gần như tức thời (< 0.5s). Tối ưu hóa nhờ chuẩn giao tiếp Text-based. |
| Logic cá nhân hóa | Yếu. Kịch bản tĩnh. Cuối cùng vẫn điều hướng ra gặp tổng đài viên con người. | Chỉ hỗ trợ trả lời FAQ (câu hỏi thường gặp), không lưu đặc điểm da cá nhân. | Mạnh mẽ. Ghi nhớ hồ sơ `skintype` của từng user vào MongoDB Atlas. Truy xuất và đề xuất sản phẩm dựa theo dữ liệu đó bằng truy vấn `find()`. Kết hợp AI Gemini tư vấn dựa trên danh sách sản phẩm thực tế. |
| Tư vấn AI | Không có AI tư vấn. | Không hỗ trợ AI tư vấn da. | Tích hợp Google Gemini `gemini-2.0-flash` với Dynamic Prompting. AI đóng vai chuyên gia tư vấn, chỉ gợi ý sản phẩm có trong kho hàng thực tế. |
| Hạ tầng Cloud | Đóng (Private Cloud của doanh nghiệp). | Máy chủ độc quyền của sàn TMĐT. | Render.com (Docker) + MongoDB Atlas. Chuẩn điện toán đám mây công cộng (Public Cloud), minh bạch và dễ triển khai. |
| Quản lý dữ liệu rác | Người dùng liên tục bị spam tin khuyến mãi hàng tuần. | Bị nhồi nhét Notification voucher. | Anti-Spam. Hệ thống chỉ tương tác khi có lệnh (Pull mechanism), bảo vệ quyền riêng tư tuyệt đối cho khách hàng. |
| Quản trị viên | Không rõ công cụ quản trị. | Công cụ nội bộ của sàn. | Có Admin Dashboard riêng biệt (Flask Web App) tại `http://localhost:5050` để quản lý user, đơn hàng, sản phẩm và thống kê doanh thu. |

### 4.2 Phân tích SWOT của dự án Lumi Beauty

Mô hình SWOT giúp nhận diện rõ ràng trạng thái hiện tại của giải pháp phần mềm nhóm phát triển:

- **Strengths (Điểm mạnh):** Giao diện cực kỳ nhẹ, không cần cài đặt ứng dụng phức tạp. Chi phí duy trì hệ thống thấp nhờ sử dụng Render.com Free Plan và MongoDB Atlas Free Tier. Tự động hóa được khâu tư vấn da tốn nhiều nhân lực nhất. Tích hợp AI Gemini nâng cao trải nghiệm tư vấn tự nhiên. Có Admin Dashboard để quản trị đơn hàng và gửi thông báo cho khách qua Telegram.
- **Weaknesses (Điểm yếu):** Giao diện của Telegram chủ yếu là văn bản và Inline Keyboard, thiếu các thao tác vuốt, kéo thả hình ảnh sống động như trên các Website TMĐT chuyên nghiệp. Chưa có tính năng thanh toán trực tuyến.
- **Opportunities (Cơ hội):** Xu hướng mua sắm qua tin nhắn (Conversational Commerce) đang bùng nổ. Có thể bán giải pháp (SaaS) này cho các Shop mỹ phẩm online nhỏ lẻ không có chi phí làm App riêng. Có thể mở rộng sang Zalo ZCA cho thị trường Việt Nam.
- **Threats (Thách thức):** Rủi ro thay đổi chính sách từ Telegram API hoặc chi phí Cloud tăng nếu lượng người dùng vượt quá ngưỡng Free-tier. Google Gemini API có thể thay đổi model hoặc chính sách miễn phí. Render.com Free Plan có cold start ~30-60s khi bot không hoạt động.

### 4.3 Đề xuất giải pháp của nhóm (Recommend a solution)

Từ các phân tích chuyên sâu trên, nhóm chúng em mạnh dạn đề xuất một giải pháp công nghệ chuyển đổi số (Digital Transformation) tối ưu và tiết kiệm nhất dành cho các Shop Mỹ phẩm SME:

1. **Từ bỏ ứng dụng di động độc lập, chuyển sang Bot API:** Việc phát triển một App iOS/Android tốn hàng trăm triệu đồng và chi phí duy trì cao. Giải pháp của nhóm là tận dụng Telegram Bot (hoặc tương lai là Zalo ZCA). Doanh nghiệp có sẵn một lượng khách hàng lớn mà không cần tốn chi phí Marketing mảng "Cài đặt ứng dụng". Tốc độ chốt sale qua chat luôn cao hơn tỷ lệ tự lướt Web.

2. **Triển khai hạ tầng không máy chủ vật lý (Serverless/PaaS):** Khuyến nghị các doanh nghiệp từ bỏ việc mua Server đặt tại cửa hàng để tránh rủi ro bảo mật và hỏng hóc phần cứng. Áp dụng giải pháp Cloud PaaS (như Render.com, Azure App Service), doanh nghiệp chỉ phải trả tiền dựa trên lượng tài nguyên tiêu thụ thực tế. Khi cần mở rộng quy mô, doanh nghiệp có thể nâng cấp lên gói Paid để có thêm tài nguyên CPU/RAM và loại bỏ cold start.

3. **Chăm sóc Data-Driven thay vì Spam:** Cần thay đổi tư duy nhắn tin hàng loạt (Broadcast Spam) sang tư duy cá nhân hóa. Bằng cách sử dụng Database NoSQL để lưu trữ tình trạng da (`skintype`) của từng khách hàng, hệ thống có thể lập trình để nhắc nhở khách hàng mua lại sữa rửa mặt trị mụn khi hệ thống tính toán được chai cũ (mua cách đây 3 tháng) có thể đã dùng hết. Admin Dashboard cho phép quản trị viên theo dõi và cập nhật trạng thái đơn hàng, tự động gửi thông báo cho khách qua Telegram.

### 4.4 Tối ưu hóa chi phí vận hành trên Cloud (Cloud Cost Optimization)

Kiến trúc của hệ thống Lumi Beauty Chatbot được thiết kế chiến lược để tận dụng tối đa các tài nguyên miễn phí (Free Tier) trong giai đoạn khởi chạy:

- **Tối ưu chi phí Cơ sở dữ liệu:** Sử dụng MongoDB Atlas với gói Free Tier M0 (cung cấp miễn phí 512MB lưu trữ, Shared Cluster). Mức tài nguyên này dư sức quản lý 65 sản phẩm trong kho hàng, hàng nghìn bản ghi người dùng và lịch sử đơn hàng mà không phát sinh thêm chi phí duy trì hàng tháng.
- **Tối ưu chi phí Máy chủ:** Bằng cách đóng gói ứng dụng qua Docker Container (base image `python:3.10-slim` chỉ ~120MB), mã nguồn trở nên độc lập và triển khai trên gói Free của Render.com với tự động build từ GitHub.
- **Tối ưu chi phí Trí tuệ nhân tạo:** Tích hợp mô hình `gemini-2.0-flash` vừa đảm bảo tốc độ phản hồi nhanh, vừa tận dụng chính sách miễn phí hạn ngạch lớn dành cho nhà phát triển từ Google. Hệ thống còn có cơ chế Model Fallback tự động chuyển sang `gemini-1.5-flash` khi model chính gặp lỗi.

Giải pháp này giúp hệ thống chứng minh được tính khả thi về mặt tài chính, sẵn sàng vận hành với chi phí cơ sở hạ tầng ban đầu gần như bằng 0.

---

## CHƯƠNG 5: TRIỂN KHAI VÀ SẢN PHẨM THỬ NGHIỆM

### 5.1 Thiết lập môi trường và Quy trình triển khai trên Cloud

Hệ thống phần mềm được nhóm tuân thủ theo các bước quản lý vòng đời ứng dụng (ALM) cơ bản, từ viết code tại Local đến khi đưa lên Cloud.

**1. Môi trường phát triển cục bộ (Local Development):**

- **IDE:** Visual Studio Code.
- **Ngôn ngữ:** Python 3.10. Các thư viện phụ thuộc được đóng gói chuẩn chỉnh trong file `requirements.txt` bao gồm: `python-telegram-bot[webhooks]>=20.0`, `python-dotenv`, `pymongo[srv]`, `google-genai`, `flask`, `requests`.
- **Bảo mật:** Biến môi trường cực kỳ nhạy cảm như `TELEGRAM_TOKEN`, `MONGO_URI`, `GEMINI_API_KEY` được lưu trữ an toàn trong file `.env` và được cho vào `.gitignore` để tránh bị rò rỉ (leak) khi đưa mã nguồn lên Internet. File `.env.example` được cung cấp như template cho người mới tham gia dự án.
- **Database:** Sử dụng MongoDB Atlas Free Tier (M0 Shared Cluster) để phát triển và triển khai. Kết nối qua `pymongo[srv]` với connection string `mongodb+srv://...`.

**2. Cấu trúc thư mục dự án:**

```
cosmetic-telegram-bot/
├── app.py                  # Entry point – Bot Server (Polling/Webhook)
├── dashboard.py            # Admin Dashboard – Flask Web Server (port 5050)
├── bot/                    # Module xử lý giao tiếp Telegram
│   ├── __init__.py
│   ├── handlers.py         # Xử lý tất cả lệnh và callback
│   ├── keyboards.py        # Định nghĩa Inline Keyboard
│   ├── messages.py         # Các thông điệp mẫu
│   └── ai.py               # Kết nối Google Gemini AI
├── database/               # Module kết nối MongoDB Atlas
│   ├── __init__.py
│   ├── mongo.py            # Khởi tạo MongoClient, database, collection
│   ├── users.py            # CRUD collection users
│   ├── products.py         # Query collection products
│   └── orders.py           # CRUD collection orders
├── data/
│   ├── __init__.py
│   ├── seed_products.py    # Script nạp 65 sản phẩm mẫu vào DB
│   └── img_folder_map.json # Map tên sản phẩm → file ảnh
├── img/                    # 32 file ảnh sản phẩm thực tế (.jpg)
├── images/                 # Ảnh theo tên sản phẩm (fallback)
├── templates/
│   └── dashboard.html      # Giao diện Admin Dashboard
├── render.yaml             # Cấu hình triển khai Render.com
├── requirements.txt        # Dependencies Python
├── Dockerfile              # Đóng gói Docker (python:3.10-slim)
├── .env                    # Biến môi trường (gitignore)
├── .env.example            # Template biến môi trường
├── .gitignore              # Danh sách file bỏ qua khi push Git
└── README.md               # Tài liệu dự án
```

**3. Quy trình đóng gói và triển khai lên Render.com:**

- **Đóng gói ứng dụng (Containerization):** Hệ thống sử dụng Docker để đóng gói toàn bộ mã nguồn và thư viện phụ thuộc. Dockerfile được thiết kế tối ưu với cache layer: copy `requirements.txt` trước để `pip install` chỉ chạy lại khi dependencies thay đổi, sau đó mới copy toàn bộ source code.
- **Bảo mật biến môi trường:** File `.env` bị chặn bởi `.gitignore`. Trên môi trường Cloud, các biến này được cấu hình an toàn trực tiếp vào phần Environment Variables của Render Dashboard.
- **Triển khai (Deployment):** Render.com kết nối trực tiếp với GitHub repository. Mỗi khi có commit mới trên branch `main`, Render tự động build Docker Image từ `Dockerfile` và khởi chạy container với lệnh `python app.py`. Biến `ENVIRONMENT=production` kích hoạt chế độ Webhook, bot lắng nghe trên port do Render inject (mặc định 10000) với `WEBHOOK_URL=https://lumi-beauty-bot.onrender.com`. Cấu hình triển khai được định nghĩa trong file `render.yaml`.

### 5.2 Admin Dashboard – Hệ thống quản trị web

Bên cạnh Telegram Bot, nhóm đã phát triển một **Admin Dashboard** bằng Flask (`dashboard.py`) cho phép quản trị viên:

- **Xem thống kê tổng quan** (`/api/stats`): Tổng số người dùng, tổng đơn hàng, tổng sản phẩm và doanh thu (tính từ giá sản phẩm × số lượng, loại trừ đơn "Đã hủy").
- **Quản lý người dùng** (`/api/users`): Xem danh sách, tìm kiếm theo username hoặc telegram_id, xóa user.
- **Quản lý đơn hàng** (`/api/orders`): Xem tất cả đơn, lọc theo trạng thái, **cập nhật trạng thái đơn hàng** (Đang xử lý → Đã giao / Đã hủy). Khi admin cập nhật trạng thái, hệ thống tự động gửi thông báo Telegram cho khách hàng thông qua hàm `_notify_telegram()`.
- **Quản lý sản phẩm** (`/api/products`): Xem danh sách, tìm kiếm theo tên hoặc mô tả.

Dashboard chạy độc lập tại `http://localhost:5050` với giao diện HTML trong `templates/dashboard.html`.

### 5.3 Phân tích hiệu suất hệ thống trên Cloud (Concurrency, Scaling, Latency)

**1. Khả năng chịu tải đồng thời (Concurrent Users):** Mã nguồn Python được viết hoàn toàn trên nền tảng `asyncio` (Asynchronous I/O). Khi Khách hàng A đang mất 5 giây để gõ tên sản phẩm cần mua, Thread của máy chủ không bị đóng băng (block) mà ngay lập tức được giải phóng để phản hồi tư vấn loại da cho Khách hàng B, tối ưu hóa triệt để CPU và RAM.

**2. Khả năng mở rộng (Scaling Strategy):** Render.com Free Plan chạy trên 1 instance. Khi cần mở rộng quy mô phục vụ nhiều người dùng hơn, có thể nâng cấp lên gói Paid để có thêm tài nguyên và loại bỏ cold start. Kiến trúc Docker Container cho phép dễ dàng chuyển đổi sang các nền tảng Cloud khác (Azure, AWS, GCP) khi cần.

**3. Tối ưu hóa độ trễ mạng (Latency):** MongoDB Atlas cluster được triển khai trên Cloud, đảm bảo thời gian đọc dữ liệu nhanh. Tổng thời gian phản hồi trung bình < 500ms khi server đang active. Lưu ý: Render.com Free Plan có cơ chế cold start (~30-60 giây) khi bot không nhận request trong 15 phút, sau đó phản hồi bình thường.

### 5.4 Kịch bản kiểm thử hệ thống (Test Cases)

| Mã TC | Chức năng | Hành động của người dùng | Kết quả mong đợi (Expected) | Trạng thái |
|-------|-----------|--------------------------|------------------------------|------------|
| TC_01 | Start Bot | User lần đầu nhấn Start hoặc gõ `/start`. | Bot gửi lời chào có emoji, hiển thị danh sách 8 lệnh hỗ trợ. User được lưu vào collection `users` với `full_name`. | PASS |
| TC_02 | Lưu loại da | Gõ `/skintype`, chọn nút "🌟 Da dầu". | Bot hiển thị Inline Keyboard 4 nút. Sau khi chọn, thông báo "✅ Đã lưu loại da: Da dầu". Database cập nhật `skintype = "da dầu"`. | PASS |
| TC_03 | Gợi ý SP | Gõ `/recommend` sau khi đã chọn loại da. | Bot truy vấn `find({"skintype": skin})` và trả về tối đa 8 sản phẩm phù hợp với loại da đã lưu, kèm giá và mô tả. | PASS |
| TC_04 | Xem danh mục | Gõ `/products`, chọn danh mục "☀️ Kem chống nắng". | Bot hiển thị 7 nút danh mục. Khi chọn, bot gửi từng sản phẩm kèm ảnh minh họa từ thư mục `img/`. | PASS |
| TC_05 | Tìm kiếm rỗng | Gõ `/search` không có từ khóa. | Bot nhắc nhở cú pháp: "Vui lòng nhập từ khóa. Ví dụ: `/search serum`". Không bị Crash. | PASS |
| TC_06 | Tìm kiếm có kết quả | Gõ `/search cetaphil`. | Bot trả về danh sách sản phẩm có chứa "cetaphil" trong tên hoặc mô tả. | PASS |
| TC_07 | Order - Lỗi nhập liệu | Gõ `/order`, ở bước "Nhập số lượng", cố tình nhập chữ "Năm cái". | Bot từ chối: "❌ Số lượng không hợp lệ. Vui lòng nhập số nguyên dương." Yêu cầu nhập lại, không crash. | PASS |
| TC_08 | Order - Thành công | Gõ `/order`, nhập tên SP hợp lệ, nhập số "2", nhập họ tên, nhập địa chỉ "Quận 1, HCM", bấm "✅ Xác nhận". | Bot báo "✅ Đặt hàng thành công!" kèm mã đơn. Dữ liệu xuất hiện trên MongoDB Atlas với `status = "Đang xử lý"`, có `customer_name` và `created_at`. | PASS |
| TC_09 | Order - Hủy | Đang trong luồng `/order`, gõ `/cancel`. | Bot báo "❌ Đã hủy đặt hàng." và xóa `user_data`. Không tạo đơn trong DB. | PASS |
| TC_10 | Tư vấn AI | Gõ `/ask Da tôi hay đổ dầu, nên dùng sữa rửa mặt nào?` | Bot gọi Gemini API, trả về tư vấn dựa trên sản phẩm thực tế trong DB. Nếu khách muốn mua, AI hướng dẫn gõ `/order`. | PASS |
| TC_11 | Chat tự nhiên | Nhắn tin "mình bị mụn nên xài gì?" (không có `/`). | Bot tự động gửi đến Gemini AI và trả về câu tư vấn tự nhiên bằng tiếng Việt. | PASS |

### 5.5 Hình ảnh demo sản phẩm thực tế

**1. Khởi động hệ thống và Khảo sát loại da thông minh**

Hình 5.5.1: Giao diện chào mừng hiển thị danh sách 8 lệnh hỗ trợ, và bảng chọn Inline Keyboard 4 loại da khi gõ `/skintype`.

**2. Module Gợi ý mỹ phẩm và Tìm kiếm sản phẩm theo nhu cầu**

Hình 5.5.2: Bot truy xuất Database trả về sản phẩm phù hợp với loại da khi gõ `/recommend`. Giao diện Inline Keyboard 7 danh mục khi gõ `/products` với ảnh sản phẩm kèm theo.

**3. Quá trình xử lý hội thoại Đặt hàng (Order Flow)**

Hình 5.5.3: Chuỗi hội thoại 5 bước: `/order` → nhập tên sản phẩm → nhập số lượng → nhập họ tên người nhận → nhập địa chỉ → xác nhận đơn hàng kèm nút "✅ Xác nhận" và "❌ Hủy".

**4. Kiến trúc dữ liệu được lưu trữ thành công trên Cloud Database**

Hình 5.5.4: Dữ liệu đơn hàng trên MongoDB Atlas hiển thị các trường `user_id`, `customer_name`, `product_name`, `quantity`, `address`, `status = "Đang xử lý"` và `created_at` được đồng bộ Real-time.

**5. Admin Dashboard – Giao diện quản trị**

Hình 5.5.5: Giao diện Admin Dashboard tại `http://localhost:5050` với thống kê tổng quan (Users, Orders, Products, Revenue), bảng quản lý đơn hàng có thể cập nhật trạng thái và tự động gửi thông báo Telegram cho khách.

---

## CHƯƠNG 6: KẾT LUẬN VÀ HƯỚNG PHÁT TRIỂN

### 6.1 Kết luận

Dự án "Xây dựng Chatbot tư vấn mỹ phẩm Lumi Beauty trên Telegram triển khai trên nền tảng Cloud" đã hoàn thành các tiêu chí và mục tiêu học thuật đề ra ban đầu. Xuyên suốt quá trình từ lên ý tưởng đến hoàn thiện sản phẩm, nhóm chúng em đã áp dụng nhuần nhuyễn những kiến thức cốt lõi từ môn học "Các nền tảng phát triển phần mềm" để đạt được những thành tựu sau:

- **Về mặt kỹ thuật phần mềm:** Thiết kế và lập trình thành công một trợ lý ảo bằng ngôn ngữ Python với mã nguồn được tổ chức module rõ ràng (`bot/`, `database/`, `data/`). Áp dụng kiến trúc bất đồng bộ (`async/await`) và quản lý phiên làm việc thông minh qua `ConversationHandler` 5 trạng thái. Tích hợp thành công Google Gemini AI với kỹ thuật Dynamic Prompting để tư vấn dựa trên dữ liệu thực tế.

- **Về mặt tư duy hệ thống & Cloud:** Hiện thực hóa thành công các khái niệm về Cloud Computing. Sử dụng MongoDB Atlas (NoSQL) với 3 collection (`users`, `products`, `orders`). Đóng gói ứng dụng bằng Docker Container, triển khai trên Render.com và hỗ trợ hai chế độ vận hành (Polling cho local, Webhook cho production).

- **Về mặt nghiệp vụ thực tiễn:** Xây dựng được luồng nghiệp vụ kinh doanh có tính ứng dụng cao: Khảo sát da → Tư vấn sản phẩm cá nhân hóa → Duyệt danh mục 7 nhóm → Tìm kiếm & Xem ảnh sản phẩm → Đặt hàng 5 bước → Xem lịch sử. Ngoài ra còn có Admin Dashboard cho phép quản trị viên theo dõi thống kê, quản lý đơn hàng và gửi thông báo tự động cho khách hàng. Danh mục sản phẩm gồm 65 mỹ phẩm đa dạng từ sữa rửa mặt, toner, serum đến kem chống nắng, mặt nạ và sản phẩm đặc trị.

### 6.2 Hướng phát triển

Dù đã nỗ lực hoàn thiện ở mức cao nhất, nhưng với giới hạn thời gian 05 tuần, sản phẩm vẫn là một bản MVP (Minimum Viable Product). Để biến Lumi Beauty trở thành một sản phẩm thương mại điện tử hoàn chỉnh, nhóm đề xuất các hướng nâng cấp:

- **Tích hợp Trí tuệ nhân tạo (Computer Vision & Machine Learning):** Khách hàng có thể chụp ảnh khuôn mặt gửi thẳng vào bot. AI trên Server sẽ dùng OpenCV/TensorFlow phân tích tình trạng mụn, nám, đổ bóng nhờn và đưa ra kết luận loại da một cách khách quan nhất.

- **Tích hợp Cổng thanh toán trực tuyến (Payment Gateway):** Hiện tại đơn hàng chỉ dừng ở mức ghi nhận (COD). Tương lai cần kết nối API với các ví điện tử như VNPay, MoMo hoặc Stripe. Bot sẽ trả về mã QR Code thanh toán động, khách quét mã và bot tự động chuyển trạng thái đơn hàng sang "Đã thanh toán".

- **Nâng cấp Admin Dashboard:** Bổ sung biểu đồ thống kê doanh thu theo thời gian, quản lý thêm/sửa/xóa sản phẩm trực tiếp, xuất file báo cáo Excel, và phân quyền đa cấp cho nhân viên.

- **Mở rộng nền tảng:** Phát triển thêm phiên bản cho Zalo OA (Official Account) để tiếp cận thị trường Việt Nam rộng hơn, nơi Zalo có lượng người dùng lớn hơn Telegram.

---

## TÀI LIỆU THAM KHẢO

1. Tài liệu môn học Nền tảng phát triển phần mềm - Khoa Công Nghệ Thông Tin, Đại học Văn Lang.
2. Microsoft Learn (2025). Introduction to Azure Bot Service and Bot Framework Composer. Truy cập từ: https://learn.microsoft.com/en-us/training/modules/intro-to-bot-service-bot-framework-composer/
3. Microsoft Learn (2025). Introduction to Azure App Service, Cloud Deployments and PaaS Architectures. Truy cập từ: https://learn.microsoft.com/en-us/azure/app-service/
4. Microsoft Azure Architecture Center (2025). Design principles for Azure applications. Truy cập từ: https://learn.microsoft.com/en-us/azure/architecture/guide/
5. Microsoft Learn (2025). Azure Cosmos DB for NoSQL Documentation. Truy cập từ: https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/
6. Telegram (2025). Telegram Bot API Official Documentation & Core Updates. Truy cập từ: https://core.telegram.org/bots/api
7. Python-Telegram-Bot (2025). Python-Telegram-Bot (PTB) Library Documentation v20+. Truy cập từ: https://docs.python-telegram-bot.org/
8. Google AI for Developers (2025). Gemini API Documentation. Truy cập từ: https://ai.google.dev/docs
9. C. S. R. Prabhu (2019). Cloud Computing: Concepts, Technology & Architecture. Nhà xuất bản Pearson.
10. Thomas Erl, Ricardo Puttini, Zaigham Mahmood (2013). Cloud Computing: Concepts, Technology & Architecture. Prentice Hall.
