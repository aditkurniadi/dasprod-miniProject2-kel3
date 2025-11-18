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

# 1. PIE CHART
#=================
plt.figure(figsize=(6,6))
plt.pie(
    df_pie_processed['Jumlah_kasus'],
    labels=df_pie_processed['HIV_AIDS'],
    autopct='%1.1f%%',
    startangle=90
)
plt.title("Distribusi Kasus HIV vs AIDS")
plt.show()

# 2. BAR CHART (UMUR)
#=====================
plt.figure(figsize=(8,5))
plt.bar(df_bar_processed.index, df_bar_processed.values)
plt.title("Jumlah Kasus Berdasarkan Kelompok Umur")
plt.xlabel("Kelompok Umur")
plt.ylabel("Jumlah Kasus")
plt.xticks(rotation=50)
plt.show()

# 3. MULTI-LINE CHART (Trend per Tahun)
# =======================
plt.figure(figsize=(10,6))
for kolom in df_line_processed.columns:
    plt.plot(df_line_processed.index, df_line_processed[kolom], marker='o', label=kolom)

plt.title("Trend Kasus HIV dan AIDS per Tahun")
plt.xlabel("Tahun")
plt.ylabel("Jumlah Kasus")
plt.legend()
plt.grid(True)
plt.show()



# 4. HEATMAP: Tahun vs Kelompok Umur
# =======================
plt.figure(figsize=(8,5))
plt.imshow(df_heatmap_processed, aspect='auto', cmap='Reds')
plt.colorbar(label="Jumlah Kasus")
plt.xticks(ticks=range(len(df_heatmap_processed.columns)), labels=df_heatmap_processed.columns)
plt.yticks(ticks=range(len(df_heatmap_processed.index)), labels=df_heatmap_processed.index)
plt.title("Heatmap Kasus per Tahun dan Kelompok Umur")
plt.show()



# 5. GROUPED BAR CHART
# =======================
plt.figure(figsize=(10,5))
x = np.arange(len(df_grouped_processed.index))
width = 0.35

plt.bar(x - width/2, df_grouped_processed['HIV'], width, label='HIV')
plt.bar(x + width/2, df_grouped_processed['AIDS'], width, label='AIDS')

plt.title("Perbandingan Kasus HIV dan AIDS Berdasarkan Kelompok Umur")
plt.xticks(x, df_grouped_processed.index, rotation=45)
plt.ylabel("Jumlah Kasus")
plt.legend()
plt.show()


print("--- [BAGIAN VISUALISASI SELESAI] ---")