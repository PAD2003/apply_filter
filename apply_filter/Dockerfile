# Sử dụng base image có hỗ trợ Python
FROM python:3.9

# Cài đặt libgl1-mesa-glx
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Thiết lập thư mục làm việc
WORKDIR /app

# Sao chép file requirements.txt vào container
COPY requirements.txt .

# Cài đặt các phụ thuộc từ requirements.txt
RUN pip install -r requirements.txt

# Sao chép các tệp tin khác của dự án vào container (nếu cần)
COPY . .

# Thiết lập lệnh mặc định khi chạy container
CMD [ "python", "app.py" ]

# Định nghĩa cổng mở trong container
# EXPOSE 7000
