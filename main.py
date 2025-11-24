"""
============================================================
MINI PROJECT 2: ANALISIS DAN VISUALISASI DATA HIV/AIDS ACEH
============================================================

File 'main.py' ini adalah KERANGKA KERJA untuk:
1.  Melakukan analisis data (Peran: Data Analyst).
2.  Membuat visualisasi dari data (Peran: Data Visualizer).

"""

# IMPORT LIBRARY
# Mengimpor library yang diperlukan untuk analisis dan visualisasi

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Muat Data Bersih
file_name = "hiv_aids_cleaned_final.xlsx"

try:
    df = pd.read_excel(file_name)
    print(f"Berhasil memuat data bersih dari '{file_name}'")
except FileNotFoundError:
    print(f"ERROR: File data bersih '{file_name}' tidak ditemukan")
    exit()
except Exception as e:
    print(f"Terjadi error saat membaca file: {e}")
    exit()

print("\n[BAGIAN DATA ANALYST DIMULAI]")
print("Melakukan pengolahan data (agregasi)")

# OLAHAN Pie Chart
df_pie_processed = df.groupby('HIV_AIDS')['Jumlah_kasus'].sum().reset_index()
print("Data untuk Pie Chart siap")

# OLAHAN Bar Chart
df_bar_processed = df.groupby('Kelompok_Umur_Standar')['Jumlah_kasus'].sum()
print("Data untuk Bar Chart Umur siap")

# OLAHAN Multi-Line Chart
df_line_processed = df.groupby(['Tahun', 'HIV_AIDS'])['Jumlah_kasus'].sum().unstack()
print("Data untuk Line Chart siap")

# OLAHAN Heatmap
df_heatmap_processed = df.groupby(['Tahun', 'Kelompok_Umur_Standar'])['Jumlah_kasus'].sum().unstack()
df_heatmap_processed = df_heatmap_processed.transpose()
print("Data untuk Heatmap siap")

# OLAHAN Grouped Bar Chart
df_grouped_processed = df.groupby(['Kelompok_Umur_Standar', 'HIV_AIDS'])['Jumlah_kasus'].sum().unstack()
print("Data untuk Grouped Bar Chart siap")

print("[BAGIAN DATA ANALYST SELESAI]")


# BAGIAN DATA VISUALIZER
# =============================================================================

print("--- [BAGIAN DATA VISUALIZER DIMULAI] ---")

# === VISUAL 1: PIE CHART ===
plt.figure(figsize=(7,7))
plt.pie(
    df_pie_processed['Jumlah_kasus'],
    labels=df_pie_processed['HIV_AIDS'],
    autopct='%1.1f%%',
    startangle=90,
    colors=["#4CAF50", "#FF7043"]
)
plt.title("Persentase Kasus HIV dan AIDS", fontsize=13)
plt.tight_layout()
plt.show()


# === VISUAL 2: BAR CHART UMUR ===
plt.figure(figsize=(8,5))
plt.bar(df_bar_processed.index, df_bar_processed.values, color="#42A5F5")

plt.title("Jumlah Kasus Berdasarkan Kelompok Umur", fontsize=13)
plt.xlabel("Kelompok Umur", fontsize=9)
plt.ylabel("Jumlah Kasus", fontsize=9)

plt.xticks(rotation=45, fontsize=8)
plt.yticks(fontsize=8)

plt.tight_layout()
plt.show()


# === VISUAL 3: MULTI LINE CHART ===
plt.figure(figsize=(9,5))
for kolom in df_line_processed.columns:
    plt.plot(df_line_processed.index, df_line_processed[kolom], marker="o", linewidth=2)

plt.title("Tren Kasus HIV dan AIDS per Tahun", fontsize=13)
plt.xlabel("Tahun", fontsize=9)
plt.ylabel("Jumlah Kasus", fontsize=9)

plt.xticks(df_line_processed.index, fontsize=8)
plt.yticks(fontsize=8)

plt.legend(df_line_processed.columns)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# === VISUAL 4: HEATMAP ===
plt.figure(figsize=(9,6))

# Ganti colormap agar lebih kontras
plt.imshow(df_heatmap_processed, cmap="coolwarm", aspect="auto")

plt.title("Heatmap Kasus Berdasarkan Tahun dan Kelompok Umur", fontsize=13)
plt.xlabel("Tahun", fontsize=9)
plt.ylabel("Kelompok Umur", fontsize=9)

plt.xticks(range(len(df_heatmap_processed.columns)), df_heatmap_processed.columns, fontsize=8)
plt.yticks(range(len(df_heatmap_processed.index)), df_heatmap_processed.index, fontsize=8)

plt.colorbar(label="Jumlah Kasus")
plt.tight_layout()
plt.show()


# === VISUAL 5: GROUPED BAR CHART ===
plt.figure(figsize=(10,5))
x = np.arange(len(df_grouped_processed.index))
width = 0.35

plt.bar(x - width/2, df_grouped_processed['HIV'], width, label='HIV', color="#29B6F6")
plt.bar(x + width/2, df_grouped_processed['AIDS'], width, label='AIDS', color="#EF5350")

plt.title("Perbandingan Kasus HIV dan AIDS Berdasarkan Kelompok Umur", fontsize=13)
plt.xlabel("Kelompok Umur", fontsize=9)
plt.ylabel("Jumlah Kasus", fontsize=9)

plt.xticks(x, df_grouped_processed.index, rotation=45, fontsize=8)
plt.yticks(fontsize=8)

plt.legend()
plt.tight_layout()
plt.show()
