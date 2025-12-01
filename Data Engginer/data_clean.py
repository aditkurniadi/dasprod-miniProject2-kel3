"""
============================================================
MINI PROJECT 2: Data Cleansing
============================================================

File 'data_clean.py' ini adalah KERANGKA KERJA untuk:
1. Melakukan data cleansing
"""

# IMPORT LIBRARY
import pandas as pd

try:
    data = pd.read_csv('data-mentah.csv', delimiter=';')
    print("Berhasil memuat 'data-mentah.csv' dengan delimiter ';'")
except FileNotFoundError:
    print("ERROR: File 'data-mentah.csv' tidak ditemukan.")
    exit()
except Exception as e:
    print(f"Terjadi error saat membaca CSV: {e}")
    exit()

# Cek apakah kolom yang diperlukan ada
required_cols = ['Kelompok_Umur', 'Tahun', 'HIV_AIDS', 'Jumlah_kasus']
if not all(col in data.columns for col in required_cols):
    print("ERROR: CSV tidak memiliki kolom yang diperlukan.")
    print(f"Kolom yang ada: {data.columns.tolist()}")
    print(f"Kolom yang dibutuhkan: {required_cols}")
    exit()

# Mengelompokkan umur
umur_mapping = {
    # Grup Balita (0-4 Tahun)
    '< 4 Tahun' : '0-4 Tahun',
    '< 1 ahun'  : '0-4 Tahun',
    '1 - 4 Tahun' : '0-4 Tahun',
    
    # Grup Anak (5-14 Tahun)
    '5 - 14 Tahun': '05-14 Tahun',
    
    # Grup Remaja (15-19 Tahun)
    '15 - 19 Tahun': '15-19 Tahun',
    
    # --- GRUP AGRESIF ---
    # Grup Dewasa (20-49 Tahun) - SEMUA digabung
    '20 - 24 Tahun': '20-49 Tahun',
    '25 - 49 Tahun': '20-49 Tahun',
    '20 - 29 Tahun': '20-49 Tahun',
    '30 - 39 Tahun': '20-49 Tahun',
    '40 - 49 Tahun': '20-49 Tahun',
    
    # Grup Lansia (50+ Tahun)
    '> 50 Tahun'  : '50+ Tahun',
    '50 - 59 Tahun': '50+ Tahun',
    '> 60 Tahun'  : '50+ Tahun'
}

# Pemetaan ke kolom 'Kelompok_umur'
# Pastikan tidak ada nilai NaN di 'kelompok_umur' yang bisa menyebabkan error
data['Kelompok_Umur'] = data['Kelompok_Umur'].fillna('Tidak Diketahui')
data['Kelompok_Umur_Standar'] = data['Kelompok_Umur'].replace(umur_mapping)

# Info tambahan: Cek apakah ada yg belum ter-mapping
unmapped = data[~data['Kelompok_Umur'].isin(umur_mapping.keys())]['Kelompok_Umur'].unique()
if len(unmapped) > 0:
    print(f"PERINGATAN: Ada nilai umur yang tidak ter-mapping: {unmapped}")

# Hapus kolom tidak relevan
kolom_dihapus = ['bps_kode_provinsi', 'bps_nama_provinsi', 'satuan']
data = data.drop(columns=kolom_dihapus, errors='ignore')

# Hapus kolom Kelompok_Umur
data = data.drop(columns=['Kelompok_Umur'], errors='ignore')

# Grouping untuk menghilangkan duplikat
print("Melakukan agregasi data...")
data_bersih = (
    data.groupby(['Tahun', 'HIV_AIDS', 'Kelompok_Umur_Standar'])['Jumlah_kasus']
    .sum()
    .reset_index()
)

# Simpan ke file excel
try:
    # Ganti nama file output agar sesuai dengan skrip analitik
    output_filename = 'hiv_aids_cleaned_final_revisi.xlsx' 
    data_bersih.to_excel(output_filename, index=False)
    print(f"Proses data cleansing selesai! File hasil: '{output_filename}'")
except Exception as e:
    print(f"ERROR saat menyimpan ke Excel: {e}")
