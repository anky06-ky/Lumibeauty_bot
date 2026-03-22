import os
import google.generativeai as genai
from database.products import get_all_products
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

def get_ai_response(user_query: str) -> str:
    if not GEMINI_API_KEY:
        return "Xin lỗi, tính năng AI hiện chưa được cấu hình. Vui lòng liên hệ admin."
        
    try:
        products = get_all_products()
        product_list_str = "\n".join([f"- {i+1}. {p['name']} (Giá: {p['price']} VNĐ, Loại da: {', '.join(p.get('skintype', []))}): {p.get('description', '')}" for i, p in enumerate(products)])
        
        system_prompt = f"""Bạn là Lumi, một chuyên gia tư vấn mỹ phẩm nhiệt tình và thân thiện của cửa hàng Lumi Beauty.
Bạn sẽ giúp khách hàng chọn sản phẩm phù hợp với tình trạng da của họ và hỗ trợ mua hàng bằng tiếng Việt.
Hãy trả lời ngắn gọn, lịch sự, có sử dụng emoji, cách dòng dễ đọc. KHÔNG trả lời quá dài (tối đa 250 chữ).

Đây là danh sách các sản phẩm ĐANG CÓ tại cửa hàng cùng Số thứ tự của chúng:
{product_list_str}

LƯU Ý QUAN TRỌNG DÀNH CHO BẠN:
1. Khi khách hàng hỏi tư vấn da: Hãy phân tích và đưa ra 1-2 gợi ý tốt nhất từ danh sách trên cùng lý do phù hợp.
2. NẾU KHÁCH TỎ Ý ĐỊNH MUA HÀNG (Ví dụ: "Tôi muốn mua số 6", "Lấy cho tôi cái này", "Đặt hàng", "Giá bao nhiêu"): BẮT BUỘC BẠN PHẢI HƯỚNG DẪN HỌ NHƯ SAU: "Tuyệt vời quá! Để đặt hàng, bạn hãy gõ lệnh /order và làm theo hướng dẫn của tớ nha! 🥰🛒"
3. KHÔNG BAO GIỜ tự mình chốt/xác nhận đơn hàng, luôn luôn bắt khách hàng gõ lệnh /order.

Câu hỏi/Tin nhắn của khách hàng: {user_query}
"""
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(system_prompt)
        return response.text
    except Exception as e:
        print(f"Gemini API Error: {e}")
        return "Xin lỗi, hiện tại Trí tuệ AI đang bận hoặc quá tải. Bạn vui lòng gõ lệnh lập trình sẵn (VD: /order, /products) hoặc thử chat lại sau một lát nhé! 🌸"
