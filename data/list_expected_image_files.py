"""In ra danh sách tên file .jpg nên đặt trong thư mục /images (chạy từ thư mục gốc project)."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from data.seed_products import PRODUCTS  # noqa: E402

if __name__ == "__main__":
    import pathlib

    root = pathlib.Path(__file__).resolve().parent.parent
    out = root / "images" / "EXPECTED_FILENAMES.txt"
    lines = []
    for p in PRODUCTS:
        safe = "".join(c for c in p["name"] if c not in r'\/:*?"<>|')
        lines.append(f"{safe}.jpg")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {len(lines)} lines to {out}")
