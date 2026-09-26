# 📊 Phân tích dữ liệu bán hàng bằng Python

Dự án cá nhân thuộc nội dung **5.5 - Phân tích dữ liệu cơ bản với NumPy, Pandas và Matplotlib**.

**Sinh viên:** Bùi Phạm Anh Giang  
**Lớp:** T26CQHT01-B  
**Trường:** Học viện Công nghệ Bưu chính Viễn thông  
**Cố vấn học tập:** Thầy Nguyễn Quang Huy

## 🎯 Mục tiêu dự án

Xây dựng quy trình phân tích dữ liệu bán hàng: đọc CSV, làm sạch, tính thống kê, phân tích theo nhiều chiều và trực quan hóa kết quả.

## 🔎 Nội dung phân tích

- Thống kê tổng doanh thu, tổng số lượng và doanh thu trung bình mỗi đơn.
- Doanh thu theo **tháng**.
- Doanh thu và số lượng theo **sản phẩm**.
- Doanh thu và số lượng theo **danh mục**.
- Doanh thu và số lượng theo **khu vực**.
- Doanh thu và số lượng theo **nhân viên**.

## 🛠️ Công nghệ

Python · NumPy · Pandas · Matplotlib · VS Code · GitHub

## 📁 Cấu trúc dự án

```text
sales-data-analysis-python/
├── sales_analysis.py
├── sales_data.csv
├── README.md
└── images/
    ├── doanh_thu_theo_thang.svg
    ├── top_san_pham_doanh_thu.svg
    ├── doanh_thu_theo_danh_muc.svg
    ├── doanh_thu_theo_khu_vuc.svg
    └── doanh_thu_theo_nhan_vien.svg
```

## ▶️ Cách chạy

```bash
pip install numpy pandas matplotlib
python sales_analysis.py
```

Khi chạy, chương trình in kết quả ra Terminal và tự động tạo các biểu đồ PNG trong thư mục `images/`.

## 📈 Kết quả trực quan

### 1. Doanh thu theo tháng
![Doanh thu theo tháng](images/doanh_thu_theo_thang.svg)

### 2. Top sản phẩm theo doanh thu
![Top sản phẩm theo doanh thu](images/top_san_pham_doanh_thu.svg)

### 3. Doanh thu theo danh mục
![Doanh thu theo danh mục](images/doanh_thu_theo_danh_muc.svg)

### 4. Doanh thu theo khu vực
![Doanh thu theo khu vực](images/doanh_thu_theo_khu_vuc.svg)

### 5. Doanh thu theo nhân viên
![Doanh thu theo nhân viên](images/doanh_thu_theo_nhan_vien.svg)

## 📌 Một số kết quả nổi bật

- Tổng doanh thu: **3.258.823.000 VNĐ**.
- Tổng số lượng bán: **703 sản phẩm**.
- Tháng có doanh thu cao nhất: **04/2026**.
- Sản phẩm tạo doanh thu cao nhất: **Laptop**.
- Danh mục tạo doanh thu cao nhất: **Điện tử**.
- Khu vực tạo doanh thu cao nhất: **Miền Nam**.
- Nhân viên tạo doanh thu cao nhất: **An**.

> Dữ liệu trong dự án là dữ liệu mô phỏng phục vụ mục đích học tập.

## 📝 Ý nghĩa

Dự án thực hành các kỹ năng `DataFrame`, `groupby`, xử lý ngày tháng, thống kê mô tả và trực quan hóa dữ liệu. Có thể phát triển tiếp thành dashboard, phân tích lợi nhuận hoặc dự báo doanh thu.