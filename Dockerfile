# Sử dụng image Python nhẹ nhất
FROM python:3.10-slim

# Thiết lập thư mục làm việc
WORKDIR /app

# Copy requirement và cài đặt dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ mã nguồn vào container
COPY . .

# Expose port (Google Cloud Run thường dùng 8080)
EXPOSE 8080

# Chạy ứng dụng
CMD ["python", "app.py"]
