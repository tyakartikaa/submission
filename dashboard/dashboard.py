import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Membaca file CSV
df = pd.read_csv("dashboard/daydashboard.csv")

# Mengatur judul dashboard
st.title("Bike Sharing Dashboard")

# Membuat layout dengan kolom
col1, col2 = st.columns([1, 3])  # Kolom 1 untuk rentang waktu, kolom 2 untuk plot

# Menempatkan rentang waktu di sebelah kiri (kolom 1)
with col1:
    st.write("### Rentang Waktu")
    start_date = st.date_input("Pilih tanggal mulai", datetime(2011, 1, 1))
    end_date = st.date_input("Pilih tanggal akhir", datetime(2012, 12, 31))

# Filter data berdasarkan rentang tanggal yang dipilih
df['dteday'] = pd.to_datetime(df['dteday'])
filtered_data = df[(df['dteday'] >= pd.to_datetime(start_date)) & (df['dteday'] <= pd.to_datetime(end_date))]

# Menempatkan plot di sebelah kanan (kolom 2)
with col2:
    # Menampilkan beberapa informasi dasar tentang dataset
    st.write("### Informasi Dataset")
    st.write(filtered_data.describe())

    # Menampilkan dataframe yang sudah difilter
    st.write("### DataFrame")
    st.dataframe(filtered_data)

    # Menampilkan line plot jumlah penyewaan per kondisi cuaca (weathersit)
    st.write("### Line Plot: Jumlah Penyewaan Sepeda Berdasarkan Kondisi Cuaca (Weathersit)")
    weathersit_grouped = filtered_data.groupby('weathersit').cnt.sum().reset_index()
    fig, ax = plt.subplots()
    ax.plot(weathersit_grouped['weathersit'], weathersit_grouped['cnt'], marker='o', color='skyblue')
    plt.title("Jumlah Penyewaan Sepeda Berdasarkan Kondisi Cuaca (Weathersit)")
    plt.xlabel("Kondisi Cuaca (Weathersit)")
    plt.ylabel("Jumlah Penyewaan (cnt)")
    ax.set_xticks([1, 2, 3])
    st.pyplot(fig)

    # Menampilkan box plot untuk jumlah penyewaan (cnt) berdasarkan weathersit
    st.write("### Box Plot: Jumlah Penyewaan Sepeda Berdasarkan Kondisi Cuaca (Weathersit)")
    fig, ax = plt.subplots()
    sns.boxplot(x='weathersit', y='cnt', data=filtered_data, ax=ax)
    plt.title("Jumlah Penyewaan Sepeda Berdasarkan Kondisi Cuaca (Weathersit)")
    plt.xlabel("Kondisi Cuaca (Weathersit)")
    plt.ylabel("Jumlah Penyewaan")
    st.pyplot(fig)
    
    # Menampilkan scatter plot antara weathersit dan cnt
    st.write("### Scatter Plot: Jumlah Penyewaan vs Kondisi Cuaca (Weathersit)")
    filtered_data['Jumlah Penyewaan'] = pd.qcut(filtered_data['cnt'], 3, labels=['Rendah', 'Sedang', 'Tinggi'])
    fig, ax = plt.subplots()
    sns.scatterplot(x='weathersit', y='cnt', hue='Jumlah Penyewaan', data=filtered_data, ax=ax)
    plt.title("Scatter Plot dari Jumlah Penyewaan dan Kondisi Cuaca (Weathersit)")
    plt.xlabel("Kondisi Cuaca (Weathersit)")
    plt.ylabel("Total Jumlah Penyewaan")
    st.pyplot(fig)

