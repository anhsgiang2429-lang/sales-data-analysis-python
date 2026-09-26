from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "sales_data.csv"
IMAGE_DIR = BASE_DIR / "images"
IMAGE_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA_FILE)
df["Ngày bán"] = pd.to_datetime(df["Ngày bán"])
df = df.drop_duplicates().dropna()

tong_doanh_thu = df["Doanh thu"].sum()
tong_so_luong = df["Số lượng"].sum()
doanh_thu_tb = np.mean(df["Doanh thu"])

print("=== THỐNG KÊ TỔNG QUAN ===")
print(f"Tổng doanh thu: {tong_doanh_thu:,.0f} VNĐ")
print(f"Tổng số lượng: {tong_so_luong} sản phẩm")
print(f"Doanh thu trung bình/đơn: {doanh_thu_tb:,.0f} VNĐ")

df["Tháng"] = df["Ngày bán"].dt.to_period("M").astype(str)
monthly = df.groupby("Tháng")["Doanh thu"].sum()
product = df.groupby("Sản phẩm").agg(So_luong=("Số lượng", "sum"), Doanh_thu=("Doanh thu", "sum")).sort_values("Doanh_thu", ascending=False)

print("\n=== DOANH THU THEO THÁNG ===")
print(monthly)
print("\n=== PHÂN TÍCH THEO SẢN PHẨM ===")
print(product)

plt.figure(figsize=(9, 5))
plt.plot(monthly.index, monthly.values / 1_000_000, marker="o")
plt.title("Doanh thu theo tháng")
plt.xlabel("Tháng")
plt.ylabel("Doanh thu (triệu VNĐ)")
plt.grid(alpha=0.25)
plt.tight_layout()
plt.savefig(IMAGE_DIR / "doanh_thu_theo_thang.png", dpi=160)
plt.close()

top_products = product.head(6).sort_values("Doanh_thu")
plt.figure(figsize=(9, 5))
plt.barh(top_products.index, top_products["Doanh_thu"] / 1_000_000)
plt.title("Top sản phẩm theo doanh thu")
plt.xlabel("Doanh thu (triệu VNĐ)")
plt.tight_layout()
plt.savefig(IMAGE_DIR / "top_san_pham_doanh_thu.png", dpi=160)
plt.close()

print(f"\nĐã lưu biểu đồ vào: {IMAGE_DIR}")
print("Chương trình chạy hoàn tất.")
