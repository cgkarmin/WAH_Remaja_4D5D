import streamlit as st
import pandas as pd
import qrcode
from io import BytesIO
import os

# Load WAH data from CSV
wah_data = pd.read_csv("wah_data.csv", dtype={"Kod": str})

# Dapatkan parameter dari URL
query_params = st.query_params
selected_kod = query_params.get("kod", [None])[0]

# Jika ada kod dalam URL, paparkan WAH yang sepadan
if selected_kod and selected_kod in wah_data["Kod"].values:
    selected_wah = wah_data[wah_data["Kod"] == selected_kod].iloc[0]
else:
    selected_kod = st.selectbox("Pilih Kod WAH", wah_data["Kod"])
    selected_wah = wah_data[wah_data["Kod"] == selected_kod].iloc[0]

# Paparkan Maklumat WAH
st.title("📖 WAH: Warisan, Ayat, Hikmah (4D/5D)")
st.header(f"{selected_wah['Surah']} - Ayat {selected_wah['Ayat']}")
st.subheader("📜 Ayat al-Quran")
st.write(selected_wah['Ayat_Arab'])
st.subheader("📖 Terjemahan")
st.write(selected_wah['Terjemahan'])
st.subheader("💡 Hikmah")
st.write(selected_wah['Hikmah'])

# Format Pantun sebagai 1 rangkap (4 baris)
st.subheader("🎭 Pantun Warisan")
if 'Pantun' in selected_wah:  # Pastikan kolom 'Pantun' wujud
    pantun = selected_wah['Pantun'].strip('"')  # Buang tanda petik di awal dan akhir
    
    # Paparkan pantun seperti dalam database
    st.write(pantun.replace("\\n", "\n"))  # Gantikan \n dengan baris baru
    st.write("")  # Tambah jarak antara rangkap (jika ada rangkap seterusnya)
else:
    st.warning("Tiada data pantun ditemui.")

# Generate QR Code yang menghala ke Streamlit
app_url = f"https://wahremaja4d5d-chou8jzqlcu4wnksjkiqew.streamlit.app/?kod={selected_kod}"
qr = qrcode.make(app_url)
buffer = BytesIO()
qr.save(buffer, format="PNG")
buffer.seek(0)
st.image(buffer, caption="Scan QR untuk melihat halaman ini", use_container_width=True)

# Simpan komen dalam CSV
komen_file = "komen.csv"

if not os.path.exists(komen_file):
    pd.DataFrame(columns=["Kod", "Surah", "Ayat", "Komen"]).to_csv(komen_file, index=False)

st.subheader("💬 Komen & Refleksi")
comment = st.text_area("Apa pendapat anda tentang ayat ini?")
if st.button("Hantar Komen"):
    if comment:
        new_komen = pd.DataFrame({
            "Kod": [selected_wah["Kod"].replace(',', '')],
            "Surah": [selected_wah["Surah"]],
            "Ayat": [selected_wah["Ayat"]],
            "Komen": [comment]
        })
        new_komen.to_csv(komen_file, mode="a", header=False, index=False)
        st.success("Komen anda telah disimpan!")
    else:
        st.warning("Sila tulis komen sebelum menghantar.")

# Paparkan Data dalam Bentuk Jadual
st.subheader("📊 Senarai WAH")
st.dataframe(wah_data)

# Paparkan Komen yang Diterima
st.subheader("📝 Komen Pengguna")
if os.path.exists(komen_file):
    komen_df = pd.read_csv(komen_file, dtype={"Kod": str})
    komen_df["Kod"] = komen_df["Kod"].str.replace(',', '', regex=True)
    st.dataframe(komen_df)
