"""
Script tạo dữ liệu mẫu sản phẩm vào Azure Cosmos DB.
Chạy 1 lần: python data/seed_products.py
"""
import sys, os, uuid
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.cosmos import get_container

PRODUCTS = [
    {"id": str(uuid.uuid4()), "name": "Sữa rửa mặt kiểm soát dầu CeraVe",       "price": 280000,  "skintype": ["da dầu","da hỗn hợp"],              "description": "Làm sạch sâu, kiểm soát dầu nhờn, không gây khô da.", "image": "srmCerave.jpg"},
    {"id": str(uuid.uuid4()), "name": "Toner cân bằng dầu Paula's Choice",        "price": 650000,  "skintype": ["da dầu"],                            "description": "Thu nhỏ lỗ chân lông, kiểm soát bóng dầu cả ngày.", "image": "tonerPaulachoise.jpg"},
    {"id": str(uuid.uuid4()), "name": "Kem dưỡng ẩm không dầu Neutrogena",        "price": 320000,  "skintype": ["da dầu","da hỗn hợp"],              "description": "Dưỡng ẩm nhẹ nhàng, không tắc nghẽn lỗ chân lông.", "image": "kemduongNeutrogena.jpg"},
    {"id": str(uuid.uuid4()), "name": "Serum Niacinamide 10% The Ordinary",       "price": 350000,  "skintype": ["da dầu","da hỗn hợp"],              "description": "Thu nhỏ lỗ chân lông, giảm thâm mụn, kiểm soát dầu.", "image": "serum_10%nia_ordinary.jpg"},
    {"id": str(uuid.uuid4()), "name": "Kem dưỡng ẩm sâu Cetaphil",               "price": 220000,  "skintype": ["da khô","da nhạy cảm"],             "description": "Dưỡng ẩm chuyên sâu 24h, phục hồi hàng rào bảo vệ da.", "image": "kemduongCetaphil.jpg"},
    {"id": str(uuid.uuid4()), "name": "Serum Hyaluronic Acid Vichy",              "price": 580000,  "skintype": ["da khô","da hỗn hợp"],              "description": "Cấp ẩm tức thì, căng mướt làn da suốt 24 giờ.", "image": "serum_HA_Vichy.jpg"},
    {"id": str(uuid.uuid4()), "name": "Sữa rửa mặt dịu nhẹ Bioderma",            "price": 190000,  "skintype": ["da khô","da nhạy cảm"],             "description": "Làm sạch nhẹ nhàng, không gây khô rát.", "image": "srmBioderma.jpg"},
    {"id": str(uuid.uuid4()), "name": "Dầu dưỡng mặt Kiehl's Midnight Recovery",  "price": 1200000, "skintype": ["da khô"],                            "description": "Phục hồi và tái tạo da qua đêm, chống oxy hóa mạnh.", "image": "dauduongMidnightRevery.jpg"},
    {"id": str(uuid.uuid4()), "name": "Kem dưỡng cân bằng ẩm La Roche-Posay",    "price": 450000,  "skintype": ["da hỗn hợp"],                        "description": "Cân bằng độ ẩm cho từng vùng da, không nhờn rít.", "image": "kemduongLaRoche_Posay.jpg"},
    {"id": str(uuid.uuid4()), "name": "Toner hoa hồng Klairs",                    "price": 380000,  "skintype": ["da hỗn hợp","da nhạy cảm"],         "description": "Cân bằng pH, dưỡng ẩm nhẹ, kết cấu trong suốt.", "image": "tonerKlairs.jpg"},
    {"id": str(uuid.uuid4()), "name": "Serum Vitamin C Skinceuticals",             "price": 2800000, "skintype": ["da hỗn hợp","da dầu"],              "description": "Làm sáng da, chống oxy hóa, giảm nám và đốm thâm.", "image": "serumC_Skinceuticals.jpg"},
    {"id": str(uuid.uuid4()), "name": "Kem dưỡng phục hồi Avène Cicalfate",       "price": 390000,  "skintype": ["da nhạy cảm"],                       "description": "Phục hồi da tổn thương, chống kích ứng, làm dịu da đỏ.", "image": "kemduongAvencecicalfate.jpg"},
    {"id": str(uuid.uuid4()), "name": "Kem chống nắng SPF50+ Anessa",             "price": 490000,  "skintype": ["da nhạy cảm","da hỗn hợp","da khô","da dầu"], "description": "Chống nắng UVA/UVB, nhẹ nhàng cho mọi loại da.", "image": "kcnAnessa.jpg"},
    {"id": str(uuid.uuid4()), "name": "Xịt khoáng Evian",                         "price": 150000,  "skintype": ["da nhạy cảm","da khô"],             "description": "Làm mát, xoa dịu da, bổ sung khoáng chất.", "image": "xitkhoang_Evian.jpg"},
    {"id": str(uuid.uuid4()), "name": "Sữa rửa mặt Gentle Skin Cleanser Eucerin", "price": 260000,  "skintype": ["da nhạy cảm","da khô"],             "description": "Dành cho da nhạy cảm, không xà phòng, pH trung tính.", "image": "srm_Eucerin.jpg"},
    {"id": str(uuid.uuid4()), "name": "Sữa rửa mặt Simple",                       "price": 130000,  "skintype": ["da nhạy cảm"],                      "description": "Dành cho da nhạy cảm, không xà phòng, pH trung tính.", "image": "srmSimple.jpg"},
    {"id": str(uuid.uuid4()), "name": "Sữa rửa mặt Cetaphil",                     "price": 200000,  "skintype": ["da nhạy cảm"],                      "description": "Dành cho da nhạy cảm, không xà phòng, pH trung tính.", "image": "srmCentaphil.jpg"},
    {"id": str(uuid.uuid4()), "name": "Serum vitamin C Klairs",                   "price": 380000,  "skintype": ["da nhạy cảm"],                      "description": "Dành cho da nhạy cảm, mới bắt đầu tập dùng vitamin C.", "image": "serum_CKlaris.jpg"},
    {"id": str(uuid.uuid4()), "name": "Nước tẩy trang Bioderma Sensibio H2O",     "price": 450000,  "skintype": ["da nhạy cảm", "da khô"],            "description": "Làm sạch lớp trang điểm và bụi bẩn dịu nhẹ, không cần rửa lại với nước.", "image": "taytrang_Bioderma.jpg"},
    {"id": str(uuid.uuid4()), "name": "Tẩy tế bào chết Paula's Choice 2% BHA",    "price": 890000,  "skintype": ["da dầu", "da hỗn hợp"],             "description": "Loại bỏ tế bào chết, làm sạch sâu lỗ chân lông và hỗ trợ giảm mụn.", "image": "taytbc_Paulachoice.jpg"},
    {"id": str(uuid.uuid4()), "name": "Mặt nạ đất sét Kiehl's Rare Earth",        "price": 850000,  "skintype": ["da dầu", "da hỗn hợp"],             "description": "Hút sạch bã nhờn, se khít lỗ chân lông, làm sạch sâu cho da.", "image": "matna_Kiehl'sRare Earth.jpg"},
    {"id": str(uuid.uuid4()), "name": "Kem chống nắng La Roche-Posay Anthelios",  "price": 475000,  "skintype": ["da dầu", "da hỗn hợp"],             "description": "Kiểm soát bóng nhờn, bảo vệ da tối ưu trước tia UVA/UVB.", "image": "kcn_LarochePosay.jpg"},
    {"id": str(uuid.uuid4()), "name": "Kem dưỡng mắt Estee Lauder ANR",           "price": 1850000, "skintype": ["da khô", "da hỗn hợp", "da dầu", "da nhạy cảm"], "description": "Giảm quầng thâm, ngăn ngừa lão hóa và nếp nhăn vùng mắt.", "image": "duongmat_EsteeLauderANR.jpg"},
    {"id": str(uuid.uuid4()), "name": "Nước tẩy trang L'Oreal Micellar Water",    "price": 170000,  "skintype": ["da dầu", "da hỗn hợp"],             "description": "Công nghệ Micellar làm sạch sâu lớp trang điểm, hạt micelle hút dầu thừa.", "image": "taytrang_LOreal.jpg"},
    {"id": str(uuid.uuid4()), "name": "Nước tẩy trang Garnier Micellar",          "price": 160000,  "skintype": ["da nhạy cảm"],                      "description": "Làm sạch dịu nhẹ không chứa cồn, không gây kích ứng da.", "image": "taytrang_Garnier.jpg"},
    {"id": str(uuid.uuid4()), "name": "Sữa rửa mặt Cosrx Low pH Good Morning",    "price": 220000,  "skintype": ["da dầu", "da nhạy cảm"],            "description": "Độ pH chuẩn 5.5, làm sạch nhẹ nhàng không làm khô căng da.", "image": "srm_Goodmorning.jpg"},
    {"id": str(uuid.uuid4()), "name": "Sữa rửa mặt Senka Perfect Whip",           "price": 120000,  "skintype": ["da thường", "da hỗn hợp"],          "description": "Tạo bọt tơ tằm siêu mịn, rửa sạch bụi bẩn và bã nhờn.", "image": "srmSenka.jpg"},
    {"id": str(uuid.uuid4()), "name": "Sữa rửa mặt Hada Labo Advanced Nourish",   "price": 150000,  "skintype": ["da khô"],                           "description": "Chứa HA dưỡng ẩm sâu, rửa xong da vẫn mềm mại.", "image": "srm_hadalabo.jpg"},
    {"id": str(uuid.uuid4()), "name": "Toner làm dịu da Anua Heartleaf 77%",      "price": 450000,  "skintype": ["da nhạy cảm", "da dầu"],            "description": "Chiết xuất diếp cá làm dịu da mụn, giảm sưng đỏ viêm.", "image": "toner_77%.jpg"},
    {"id": str(uuid.uuid4()), "name": "Toner cấp ẩm Hada Labo Gokujyun",          "price": 280000,  "skintype": ["da khô", "da hỗn hợp"],             "description": "Cấp nước tức thì cho da khô ráp, giúp da ngậm nước căng bóng.", "image": "toner_hadalabo.jpg"},
]

def seed():
    container = get_container("products", "/id")
    for p in PRODUCTS:
        container.create_item(body=p)
    print(f"✅ Đã thêm {len(PRODUCTS)} sản phẩm vào Azure Cosmos DB!")

if __name__ == "__main__":
    seed()
