import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data from the file day_aul
day_aul = pd.read_csv('all_data.csv')  # Ganti 'day_aul.csv' dengan nama file yang sesuai

# Streamlit App
st.title('Dashboard Analisis Pengguna Sepeda')

# Tabs
tabs = ["Visualisasi Jumlah Pengguna", "Analisis Jumlah Pengguna"]
current_tab = st.sidebar.radio("Pilih Tab", tabs)

if current_tab == tabs[0]:
    # Visualisasi Jumlah Pengguna
    st.subheader('Visualisasi Jumlah Pengguna Sepeda per Bulan')

    # Membuat plot line chart
    fig, ax = plt.subplots(figsize=(10, 6))
    grouped = day_aul.groupby('mnth')
    result = grouped[['casual', 'registered']].sum().reset_index()
    result = result[result['mnth'].between(1, 12)]
    ax.plot(result['mnth'], result['casual'], label='Kasual')
    ax.plot(result['mnth'], result['registered'], label='Terdaftar')

    # Menambahkan judul dan label sumbu
    ax.set_title('Jumlah Pengguna Sepeda per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Pengguna')

    # Menambahkan legenda
    ax.legend()

    # Menampilkan plot di aplikasi Streamlit
    st.pyplot(fig)
elif current_tab == tabs[1]:
    # Analisis Jumlah Pengguna
    st.subheader('Analisis Jumlah Pengguna Sepeda per Bulan')

    # Menghitung jumlah pengguna sepeda per bulan
    jumlah_pengguna_per_mnth = day_aul.groupby('mnth')['cnt'].sum()

    # Menampilkan hasil perhitungan
    st.write("Jumlah pengguna sepeda per bulan:")
    st.write(jumlah_pengguna_per_mnth)

    # Visualisasi dengan bar plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(jumlah_pengguna_per_mnth.index, jumlah_pengguna_per_mnth)
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Pengguna Sepeda')
    ax.set_title('Jumlah Pengguna Sepeda per Bulan')

    # Menampilkan plot di aplikasi Streamlit
    st.pyplot(fig)
