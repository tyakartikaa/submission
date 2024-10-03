# Bike Sharing Dashboard

Ini adalah dashboard interaktif yang dibuat menggunakan **Streamlit** untuk menampilkan dan menganalisis data penggunaan bike-sharing. Dashboard ini memungkinkan pengguna untuk memfilter data berdasarkan rentang waktu dan menganalisis pola penggunaan sepeda dalam berbagai kondisi cuaca.

## Fitur Dashboard

- **Filter Rentang Waktu**: Pilih rentang tanggal untuk melihat data penyewaan sepeda dalam periode tertentu.
- **Informasi Dataset**: Menampilkan statistik deskriptif dari data yang telah difilter.
- **Visualisasi Data**:
  - **Histogram**: Distribusi jumlah penyewaan sepeda.
  - **Scatter Plot**: Hubungan antara jumlah penyewaan sepeda dan kondisi cuaca.
  - **Box Plot**: Distribusi penyewaan sepeda berdasarkan kondisi cuaca.
  - **Line Plot**: Tren jumlah penyewaan sepeda berdasarkan kondisi cuaca.

## Instalasi
1. **Clone repository ini** atau buat folder proyek baru di lokal Anda.
2. pip install -r requirements.txt
3. **Pastikan Anda memiliki dataset** (`day.csv`) yang akan digunakan. Dataset ini harus ditempatkan di direktori yang sama dengan file dashboard.

## Menjalankan Dashboard
Untuk menjalankan dashboard, ikuti langkah-langkah berikut:
1. **Buka terminal atau command prompt** dan arahkan ke folder proyek Anda.
2. **Jalankan perintah berikut** untuk memulai aplikasi Streamlit:
   streamlit run dashboard.py
   Di mana `dashboard.py` adalah nama file Python yang berisi kode dashboard.
3. Setelah menjalankan perintah di atas, **Streamlit akan membuka jendela browser** yang menampilkan dashboard.
   
## Penggunaan

1. **Pilih rentang waktu**: Gunakan komponen date picker di sebelah kiri untuk memilih rentang tanggal yang ingin dianalisis.
2. **Lihat visualisasi data**: Di bagian kanan, Anda akan melihat beberapa visualisasi seperti histogram, scatter plot, box plot, dan line plot yang menggambarkan hubungan antara jumlah penyewaan sepeda dan kondisi cuaca.
3. **Eksplorasi data**: Anda dapat berinteraksi dengan data dan visualisasi untuk menemukan wawasan terkait pola penggunaan sepeda dalam sistem bike-sharing.

## Catatan

- Pastikan file dataset `day.csv` berada di direktori yang sama dengan file `dashboard.py`.
- Jika ada error terkait file dataset, pastikan nama file dan lokasi file sudah benar.
