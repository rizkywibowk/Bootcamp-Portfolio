import streamlit as st

st.title("Kegemaran Gen Z")

st.header("Welcome to My Streamlit App!")
st.text("Tolong Bantu saya untuk mengisi pertanyaan pertanyaan mudah dibawah.")

name = st.text_input("Masukkan nama kamu:")
age = st.slider("Umur kamu berapa?", 10, 60)
hobby = st.selectbox("Pilih hobi kamu:", ["Ngoding", "Gaming", "Nonton", "Olahraga"])

if st.button("Submit"):
    st.success(f"Halo {name}, umur kamu {age} tahun dan hobi kamu {hobby}!")

import pandas as pd
import numpy as np

# Membuat DataFrame
data = pd.DataFrame({
    'x': np.arange(1, 11),
    'y': np.random.randint(1, 20, 10)
})

# Menampilkan subheader
st.subheader("Visualisasi Data Interaktif")

# Pilih jenis chart
chart_type = st.radio("Pilih jenis chart:", ["Line", "Bar"])

# Fungsi untuk menampilkan chart berdasarkan pilihan
def chart_type(data, chart_type):
    if chart_type == "Line":
        st.line_chart(data.set_index('x'))
    else:
        st.bar_chart(data.set_index('x'))

# Menampilkan chart berdasarkan pilihan
chart_type(data, chart_type)