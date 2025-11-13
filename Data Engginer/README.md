Peran: Data Engineer

Misi Utama

Tanggung jawab utama dari Data Engineer adalah mengubah data mentah yang tidak konsisten menjadi satu file data bersih (.xlsx) yang terstandar, akurat, dan siap untuk dianalisis oleh Data Analyst.

Langkah Kerja

1. Apa yang Perlu di-Standarisasi (Kolom: Kelompok_Umur)

Kolom Kelompok_Umur memiliki nilai yang tidak konsisten dan tumpang tindih antar tahun. Ini harus dipetakan (di-mapping) ke satu set kategori standar.

Tugas: Buat kamus pemetaan (dictionary) di Python untuk menggabungkan kategori-kategori berikut:

Kategori Balita (Target: '0-4 Tahun')

'< 4 Tahun'

'< 1 ahun' (Perhatikan typo 'ahun')

'1 - 4 Tahun'

Kategori Dewasa (Target: '20-49 Tahun')

'20 - 24 Tahun'

'25 - 49 Tahun'

'20 - 29 Tahun'

'30 - 39 Tahun'

'40 - 49 Tahun'

Kategori Lansia (Target: '50+ Tahun')

'> 50 Tahun'

'50 - 59 Tahun'

'> 60 Tahun'

Kategori Lain (Biarkan): '5 - 14 Tahun' dan '15 - 19 Tahun' sudah konsisten dan tidak perlu dipetakan.

2. Apa yang Perlu di-Perbaiki (Struktur Data)

Kolom Tidak Relevan: Data mentah memiliki kolom yang tidak diperlukan untuk analisis.

Tugas: Hapus kolom-kolom berikut: bps_kode_provinsi, bps_nama_provinsi, dan satuan.

Kolom Lama: Setelah membuat Kelompok_Umur_Standar, kolom Kelompok_Umur yang asli harus dihapus.

Duplikasi Agregat (SANGAT PENTING): Setelah memetakan '20-24 Tahun' dan '25-49 Tahun' (misalnya di tahun 2022) menjadi '20-49 Tahun', kita akan memiliki dua baris data untuk '20-49 Tahun' di tahun 2022.

Format Output:

Tugas: Simpan hasil akhir sebagai file Excel (.xlsx), bukan .csv, untuk kompatibilitas maksimum. Gunakan index=False saat menyimpan.
