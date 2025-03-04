# WAH: Warisan, Ayat, Hikmah (4D/5D)
Aplikasi interaktif yang memaparkan WAH dalam bentuk kod 4D/5D menggunakan **Streamlit**.

## 📌 Fungsi Utama:
- Memilih kod 4D/5D untuk melihat ayat al-Quran, terjemahan, hikmah, dan pantun warisan.
- Menjana **QR Code** untuk terus melihat ayat penuh di Quran.com.
- Membolehkan pengguna memberikan komen dan refleksi.

## 📂 Struktur Folder:
```
📁 WAH_Remaja_4D5D/
    ├── 📄 app.py   # Aplikasi utama Streamlit
    ├── 📄 wah_data.csv   # Data ayat, hikmah & pantun dalam CSV
    ├── 📁 assets/   # Folder untuk QR Code dan media
    ├── 📁 docs/   # Dokumentasi projek
    ├── 📄 requirements.txt   # Senarai pustaka Python yang diperlukan
    ├── 📄 README.md   # Dokumentasi projek
```

## 🚀 **Cara Jalankan Aplikasi di Laptop**
1. **Pasang pustaka yang diperlukan:**  
   ```bash
   pip install streamlit pandas qrcode[pil]
   ```
2. **Jalankan aplikasi:**  
   ```bash
   streamlit run app.py
   ```

## 📊 **Data WAH** (Contoh Kod 4D/5D)
| Kod 4D/5D | Surah | Ayat | Hikmah |
|-----------|--------|------|--------------------|
| 1810      | Al-Kahf | 10   | Berlindung dengan doa |
| 2286      | Al-Baqarah | 286 | Allah tidak membebani kita |

Selamat menggunakan aplikasi ini! 😊
