# 📊 Phân tích dữ liệu bán hàng bằng Python

Dự án cá nhân thuộc nội dung **5.5 - Phân tích dữ liệu cơ bản với NumPy, Pandas và Matplotlib**.

**Sinh viên:** Bùi Phạm Anh Giang  
**Lớp:** T26CQHT01-B  
**Trường:** Học viện Công nghệ Bưu chính Viễn thông  
**Cố vấn học tập:** Thầy Nguyễn Quang Huy

## 🎯 Mục tiêu dự án

Dự án xây dựng một quy trình phân tích dữ liệu bán hàng hoàn chỉnh: đọc dữ liệu CSV, làm sạch dữ liệu, tính các chỉ số thống kê, phân tích theo nhiều chiều và trực quan hóa kết quả bằng biểu đồ.

## 🔎 Nội dung phân tích

- Thống kê tổng doanh thu, tổng số lượng và doanh thu trung bình mỗi đơn.
- Phân tích doanh thu theo **tháng**.
- Phân tích doanh thu và số lượng theo **sản phẩm**.
- Phân tích doanh thu và số lượng theo **danh mục**.
- Phân tích doanh thu và số lượng theo **khu vực**.
- Phân tích doanh thu và số lượng theo **nhân viên**.
- Tự động xuất biểu đồ vào thư mục `images/`.

## 🛠️ Công nghệ sử dụng

- Python
- NumPy
- Pandas
- Matplotlib
- Visual Studio Code
- GitHub

## 📁 Cấu trúc dự án

```text
sales-data-analysis-python/
├── sales_analysis.py
├── sales_data.csv
├── README.md
└── images/
    ├── doanh_thu_theo_thang.png
    ├── top_san_pham_doanh_thu.png
    ├── doanh_thu_theo_danh_muc.png
    ├── doanh_thu_theo_khu_vuc.png
    └── doanh_thu_theo_nhan_vien.png
```

> Thư mục `images/` được chương trình tự động tạo khi chạy `sales_analysis.py`.

## ▶️ Cách chạy chương trình

1. Tải hoặc clone repository về máy.
2. Mở thư mục dự án bằng VS Code.
3. Cài các thư viện cần thiết:

```bash
pip install numpy pandas matplotlib
```

4. Chạy chương trình:

```bash
python sales_analysis.py
```

5. Xem kết quả trên Terminal và các biểu đồ được lưu trong thư mục `images/`.

## 📈 Kết quả đầu ra

Chương trình hiển thị 6 nhóm kết quả chính:

1. Thống kê tổng quan.
2. Doanh thu theo tháng.
3. Phân tích theo sản phẩm.
4. Phân tích theo danh mục.
5. Phân tích theo khu vực.
6. Phân tích theo nhân viên.

Các biểu đồ giúp so sánh trực quan doanh thu giữa các nhóm và hỗ trợ rút ra nhận xét từ dữ liệu.

## 📝 Ý nghĩa

Dự án giúp thực hành các kỹ năng quan trọng của phân tích dữ liệu cơ bản như `DataFrame`, `groupby`, xử lý ngày tháng, thống kê mô tả và trực quan hóa dữ liệu. Đây cũng là nền tảng để phát triển thêm dashboard, phân tích lợi nhuận hoặc dự báo doanh thu trong tương lai.
