import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Membaca file CSV dari path lokal
day_df = pd.read_csv("https://raw.githubusercontent.com/tyakartikaa/submission/main/dashboard/daydashboard.csv")
hour_df = pd.read_csv("https://raw.githubusercontent.com/tyakartikaa/submission/main/dashboard/hourdashboard.csv")

# Mengatur judul dashboard
st.title("Bike Sharing Dashboard")

# Menambahkan kolom di bagian kiri untuk rentang tanggal
st.sidebar.header("Filter Rentang Tanggal")

# Rentang tanggal untuk day_df
st.sidebar.write("### Rentang Tanggal untuk Day Dashboard")
start_date_day = st.sidebar.date_input("Pilih Tanggal Mulai (Day Dashboard)", datetime(2011, 1, 1))
end_date_day = st.sidebar.date_input("Pilih Tanggal Akhir (Day Dashboard)", datetime(2012, 12, 31))

# Filter data day_df berdasarkan rentang tanggal yang dipilih
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
filtered_day_df = day_df[(day_df['dteday'] >= pd.to_datetime(start_date_day)) & (day_df['dteday'] <= pd.to_datetime(end_date_day))]

# Rentang tanggal dan waktu untuk hour_df
st.sidebar.write("### Rentang Tanggal dan Waktu untuk Hour Dashboard")
start_date_hour = st.sidebar.date_input("Pilih Tanggal Mulai (Hour Dashboard)", datetime(2011, 1, 1))
end_date_hour = st.sidebar.date_input("Pilih Tanggal Akhir (Hour Dashboard)", datetime(2012, 12, 31))
start_hour = st.sidebar.slider("Pilih Jam Mulai", 0, 23, 0)
end_hour = st.sidebar.slider("Pilih Jam Akhir", 0, 23, 23)

# Filter data hour_df berdasarkan rentang tanggal dan jam yang dipilih
hour_df['dteday_hr'] = pd.to_datetime(hour_df['dteday_hr'])
filtered_hour_df = hour_df[(hour_df['dteday_hr'] >= pd.to_datetime(start_date_hour)) & 
                           (hour_df['dteday_hr'] <= pd.to_datetime(end_date_hour)) & 
                           (hour_df['hr_hr'] >= start_hour) & (hour_df['hr_hr'] <= end_hour)]

# Tampilan utama di halaman utama (bukan sidebar)
st.write("## 1. Dataset (day_df)")

# Menampilkan informasi dataset yang sudah difilter
st.write(f"### Informasi Dataset (day_df) dari {start_date_day} hingga {end_date_day}")
st.write(filtered_day_df.describe())

# Menampilkan dataframe yang sudah difilter
st.write("### DataFrame (day_df) yang Sudah Difilter")
st.dataframe(filtered_day_df)

# Menampilkan line plot jumlah penyewaan per kondisi cuaca (weathersit)
st.write("### Line Plot: Jumlah Penyewaan Sepeda Berdasarkan Kondisi Cuaca (Weathersit)")
weather_rentals = filtered_day_df.groupby('weathersit')['cnt'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(weather_rentals['weathersit'], weather_rentals['cnt'], marker='o', linewidth=2, color="#72BCD4")
ax.set_title("Jumlah Penyewaan Sepeda Berdasarkan Kondisi Cuaca (Weathersit)", loc="center", fontsize=15)
ax.set_xlabel("Kondisi Cuaca (Weathersit)", fontsize=12)
ax.set_ylabel("Jumlah Penyewa (cnt)", fontsize=12)
ax.set_xticks([1, 2, 3, 4])
ax.set_xticklabels(['Cerah', 'Berkabut', 'Hujan', 'Ekstrem'])
plt.ticklabel_format(style='plain', axis='y')
st.pyplot(fig)

# Menampilkan box plot untuk jumlah penyewaan (cnt) berdasarkan weathersit
st.write("### Box Plot: Jumlah Penyewaan Sepeda Berdasarkan Kondisi Cuaca (Weathersit)")
filtered_day_df['weathersit_label'] = filtered_day_df['weathersit'].map({1: 'Cerah', 2: 'Berkabut', 3: 'Hujan', 4: 'Ekstrem'})
order = ['Cerah', 'Berkabut', 'Hujan', 'Ekstrem']
filtered_day_df['weathersit_label'] = pd.Categorical(filtered_day_df['weathersit_label'], categories=order, ordered=True)
fig, ax = plt.subplots()
sns.boxplot(x='weathersit_label', y='cnt', data=filtered_day_df, ax=ax, order=order)
ax.set_title("Jumlah Penyewaan Sepeda Berdasarkan Kondisi Cuaca (Weathersit)")
ax.set_xlabel("Kondisi Cuaca (Weathersit)")
ax.set_ylabel("Jumlah Penyewa (cnt)")
st.pyplot(fig)

# Menampilkan scatter plot antara weathersit dan cnt
st.write("### Scatter Plot: Jumlah Penyewaan vs Kondisi Cuaca (Weathersit)")
filtered_day_df['Jumlah Penyewaan'] = pd.qcut(filtered_day_df['cnt'], q=3, labels=['Rendah', 'Sedang', 'Tinggi'])
fig, ax = plt.subplots()
sns.scatterplot(x='weathersit', y='cnt', hue='Jumlah Penyewaan', data=filtered_day_df, palette='coolwarm', ax=ax)
ax.set_title('Scatter Plot dari Jumlah Penyewaan dan Kondisi Cuaca (Weathersit)')
ax.set_xlabel('Kondisi Cuaca (Weathersit)')
ax.set_ylabel('Total Jumlah Penyewaan')
ax.set_xticks([1, 2, 3, 4])
ax.set_xticklabels(['Cerah', 'Berkabut', 'Hujan', 'Ekstrem'])
st.pyplot(fig)

st.write("## 2. Dataset (hour_df)")

# Menampilkan beberapa informasi dasar tentang dataset yang sudah difilter
st.write(f"### Informasi Dataset (hour_df) dari {start_date_hour} hingga {end_date_hour} dan jam {start_hour} hingga {end_hour}")
st.write(filtered_hour_df.describe())

# Menampilkan dataframe yang sudah difilter
st.write("### DataFrame (hour_df) yang Sudah Difilter")
st.dataframe(filtered_hour_df)

# Menampilkan line chart jumlah penyewaan per jam
st.write("### Line Chart: Jumlah Penyewaan Sepeda Berdasarkan Jam")
hourly_rentals = filtered_hour_df.groupby('hr_hr')['cnt_hr'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(hourly_rentals['hr_hr'], hourly_rentals['cnt_hr'], marker='o', linewidth=2, color="#72BCD4")
ax.set_title("Jumlah Sepeda yang Disewa Berdasarkan Jam (hr)", loc="center", fontsize=15)
ax.set_xlabel("Jam (hr)", fontsize=12)
ax.set_ylabel("Jumlah Sepeda yang Disewa (cnt)", fontsize=12)
ax.set_xticks(range(0, 24))
plt.grid(True)
st.pyplot(fig)

# Menampilkan dodged bar plot untuk jumlah penyewaan pada pengguna casual dan registered berdasarkan jam
st.write("### Dodged Bar Plot: Jumlah Penyewaan Pengguna Casual dan Registered Sepanjang Hari")
hourly_casual_registered_melted = filtered_hour_df.melt(
    id_vars='hr_hr', value_vars=['casual_hr', 'registered_hr'], var_name='User Type', value_name='Rental Count'
)
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x='hr_hr', y='Rental Count', hue='User Type', data=hourly_casual_registered_melted, 
            palette=["skyblue", "salmon"], ax=ax)
ax.set_title("Penyewaan Sepeda oleh Pengguna Casual dan Registered Sepanjang Hari")
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Total Sepeda yang Disewa")
ax.legend(loc="upper right")
plt.grid(True)
st.pyplot(fig)

# Menampilkan scatter plot clustering pada data hour_df
st.write("### Scatter Plot: Jumlah Penyewaan vs Waktu")
hourly_rentals['time_of_day'] = hourly_rentals['hr_hr'].apply(
    lambda hr: 'Dini Hari' if 0 <= hr <= 4 else 'Pagi' if 5 <= hr <= 11 else 'Siang' if 12 <= hr <= 15 else 'Sore' if 16 <= hr <= 19 else 'Malam'
)
hourly_rentals['Jumlah Penyewaan'] = pd.qcut(hourly_rentals['cnt_hr'], 3, labels=['Rendah', 'Sedang', 'Tinggi'])

fig, ax = plt.subplots(figsize=(10, 5))
sns.scatterplot(x='time_of_day', y='cnt_hr', hue='Jumlah Penyewaan', data=hourly_rentals, palette='coolwarm', s=100, ax=ax)

ax.set_title('Scatter Plot Jumlah Sepeda yang Disewa Berdasarkan Waktu', fontsize=15)
ax.set_xlabel('Waktu', fontsize=12)
ax.set_ylabel('Jumlah Sepeda yang Disewa', fontsize=12)
ax.grid(True)
st.pyplot(fig)
