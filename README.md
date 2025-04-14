# ExoExpo - Visualisasi Data Eksoplanet

ExoExpo adalah aplikasi web interaktif yang menampilkan visualisasi data eksoplanet. Proyek ini bertujuan untuk memanfaatkan data astronomi dari arsip publik seperti NASA Exoplanet Archive untuk visualisasi yang lebih mudah diakses bagi masyarakat umum.

> **Status**: Work in Progress (WIP)

---

## Teknologi yang Digunakan

### Frontend
- [React.js](https://reactjs.org/)
- [TailwindCSS](https://tailwindcss.com/)
- [Axios](https://axios-http.com/)

### Backend
- [Flask](https://flask.palletsprojects.com/)
- [Pandas](https://pandas.pydata.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Flask-CORS](https://flask-cors.readthedocs.io/)

### Deployment
- **Frontend**: Vercel
- **Backend**: Heroku

---

## Struktur Direktori

```
exoexpo/
├── backend/          # Flask API + koneksi database PostgreSQL
│   ├── app.py        # Server utama Flask
│   └── data_utils.py # Loader data eksoplanet ke PostgreSQL
│
├── frontend/         # Aplikasi React.js
│   ├── public/
│   └── src/
│       ├── components/
│       └── App.jsx
│
├── exoplanets_clean.csv   # Dataset eksoplanet yang telah dibersihkan (sementara lokal)
└── README.md
```

---

## Fitur yang Sudah Dikerjakan

- Setup proyek React dengan TailwindCSS
- Setup backend Flask dan endpoint `/planets` statis
- Instalasi dan konfigurasi PostgreSQL lokal
- Script Python untuk load data eksoplanet ke database
- Struktur awal API untuk fetch data dari database (WIP)

---

## Rencana Fitur Berikutnya

- Visualisasi: Scatter plot massa vs periode orbit
- Visualisasi: Informasi umum tiap planet dan simulasi orbitnya
- Filter berdasarkan metode penemuan, jarak, tahun
- Interaksi dinamis antara frontend dan backend
- Deployment ke Vercel dan Heroku

---

## Sumber Data

Data diambil dari:
- [NASA Exoplanet Archive + TESS](https://exoplanetarchive.ipac.caltech.edu/)

---