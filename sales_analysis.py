from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "sales_data.csv"
IMAGE_DIR = BASE_DIR / "images"
IMAGE_DIR.mkdir(parents=True, exist_ok=True)

# 1. Đọc và làm sạch dữ liệu
df = pd.read_csv(DATA_FILE)
df["Ngày bán"] = pd.to_datetime(df["Ngày bán"])
df = df.drop_duplicates().dropna()

# 2. Thống kê tổng quan
tong_doanh_thu = df["Doanh thu"].sum()
tong_so_luong = df["Số lượng"].sum()
doanh_thu_tb = np.mean(df["Doanh thu"])

print("=== THỐNG KÊ TỔNG QUAN ===")
print(f"Tổng doanh thu: {tong_doanh_thu:,.0f} VNĐ")
print(f"Tổng số lượng: {tong_so_luong} sản phẩm")
print(f"Doanh thu trung bình/đơn: {doanh_thu_tb:,.0f} VNĐ")

# 3. Phân tích theo tháng
df["Tháng"] = df["Ngày bán"].dt.to_period("M").astype(str)
monthly = df.groupby("Tháng")["Doanh thu"].sum()

# 4. Phân tích theo sản phẩm
product = (
    df.groupby("Sản phẩm")
      .agg(So_luong=("Số lượng", "sum"), Doanh_thu=("Doanh thu", "sum"))
      .sort_values("Doanh_thu", ascending=False)
)

# 5. Phân tích theo danh mục
category = (
    df.groupby("Danh mục")
      .agg(So_luong=("Số lượng", "sum"), Doanh_thu=("Doanh thu", "sum"))
      .sort_values("Doanh_thu", ascending=False)
)

# 6. Phân tích theo khu vực
region = (
    df.groupby("Khu vực")
      .agg(So_luong=("Số lượng", "sum"), Doanh_thu=("Doanh thu", "sum"))
      .sort_values("Doanh_thu", ascending=False)
)

# 7. Phân tích theo nhân viên
employee = (
    df.groupby("Nhân viên")
      .agg(So_luong=("Số lượng", "sum"), Doanh_thu=("Doanh thu", "sum"))
      .sort_values("Doanh_thu", ascending=False)
)

# 8. In kết quả
print("\n=== DOANH THU THEO THÁNG ===")
print(monthly)

print("\n=== PHÂN TÍCH THEO SẢN PHẨM ===")
print(product)

print("\n=== PHÂN TÍCH THEO DANH MỤC ===")
print(category)

print("\n=== PHÂN TÍCH THEO KHU VỰC ===")
print(region)

print("\n=== PHÂN TÍCH THEO NHÂN VIÊN ===")
print(employee)

# 9. Biểu đồ doanh thu theo tháng
plt.figure(figsize=(9, 5))
plt.plot(monthly.index, monthly.values / 1_000_000, marker="o")
plt.title("Doanh thu theo tháng")
plt.xlabel("Tháng")
plt.ylabel("Doanh thu (triệu VNĐ)")
plt.grid(alpha=0.25)
plt.tight_layout()
plt.savefig(IMAGE_DIR / "doanh_thu_theo_thang.png", dpi=160)
plt.close()

# 10. Biểu đồ top sản phẩm theo doanh thu
top_products = product.head(6).sort_values("Doanh_thu")
plt.figure(figsize=(9, 5))
plt.barh(top_products.index, top_products["Doanh_thu"] / 1_000_000)
plt.title("Top sản phẩm theo doanh thu")
plt.xlabel("Doanh thu (triệu VNĐ)")
plt.tight_layout()
plt.savefig(IMAGE_DIR / "top_san_pham_doanh_thu.png", dpi=160)
plt.close()

# 11. Biểu đồ doanh thu theo danh mục
plt.figure(figsize=(8, 5))
plt.bar(category.index, category["Doanh_thu"] / 1_000_000)
plt.title("Doanh thu theo danh mục")
plt.xlabel("Danh mục")
plt.ylabel("Doanh thu (triệu VNĐ)")
plt.tight_layout()
plt.savefig(IMAGE_DIR / "doanh_thu_theo_danh_muc.png", dpi=160)
plt.close()

# 12. Biểu đồ doanh thu theo khu vực
plt.figure(figsize=(8, 5))
plt.bar(region.index, region["Doanh_thu"] / 1_000_000)
plt.title("Doanh thu theo khu vực")
plt.xlabel("Khu vực")
plt.ylabel("Doanh thu (triệu VNĐ)")
plt.tight_layout()
plt.savefig(IMAGE_DIR / "doanh_thu_theo_khu_vuc.png", dpi=160)
plt.close()

# 13. Biểu đồ doanh thu theo nhân viên
plt.figure(figsize=(8, 5))
plt.bar(employee.index, employee["Doanh_thu"] / 1_000_000)
plt.title("Doanh thu theo nhân viên")
plt.xlabel("Nhân viên")
plt.ylabel("Doanh thu (triệu VNĐ)")
plt.tight_layout()
plt.savefig(IMAGE_DIR / "doanh_thu_theo_nhan_vien.png", dpi=160)
plt.close()

print(f"\nĐã lưu 5 biểu đồ vào: {IMAGE_DIR}")
print("Chương trình chạy hoàn tất.")
