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

# import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- 0. Muat Data Bersih ---
file_name = "hiv_aids_cleaned_final.xlsx"

try:
    df = pd.read_excel(file_name)
    print(f"Berhasil memuat data bersih dari '{file_name}'.")
except FileNotFoundError:
    print(f"ERROR: File data bersih '{file_name}' tidak ditemukan.")
    exit()
except Exception as e:
    print(f"Terjadi error saat membaca file: {e}")
    exit()

print("\n--- [BAGIAN DATA ANALYST DIMULAI] ---")
print("Melakukan pengolahan data (agregasi)...")

# === OLAHAN 1: Pie Chart ===
df_pie_processed = df.groupby('HIV_AIDS')['Jumlah_kasus'].sum().reset_index()
print("1. Data untuk Pie Chart siap.")

# === OLAHAN 2: Bar Chart ===
df_bar_processed = df.groupby('Kelompok_Umur_Standar')['Jumlah_kasus'].sum()
print("2. Data untuk Bar Chart Umur siap.")

# === OLAHAN 3: Multi-Line Chart ===
df_line_processed = df.groupby(['Tahun', 'HIV_AIDS'])['Jumlah_kasus'].sum().unstack()
print("3. Data untuk Line Chart siap.")

# === OLAHAN 4: Heatmap ===
df_heatmap_processed = df.groupby(['Tahun', 'Kelompok_Umur_Standar'])['Jumlah_kasus'].sum().unstack()
df_heatmap_processed = df_heatmap_processed.transpose()
print("4. Data untuk Heatmap siap.")

# === OLAHAN 5: Grouped Bar Chart ===
df_grouped_processed = df.groupby(['Kelompok_Umur_Standar', 'HIV_AIDS'])['Jumlah_kasus'].sum().unstack()
print("5. Data untuk Grouped Bar Chart siap.")

print("--- [BAGIAN DATA ANALYST SELESAI] ---")


#  BAGIAN DATA ANALYST
# =============================================================================

# Tulis code disini


# BAGIAN DATA VISUALIZER
# =============================================================================

# Tulis code disini