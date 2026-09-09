# Pertemuan 02 – Dasar Python

**Nama:** Aulia Rahma Ramadhani  
**NIM:** 2225250001  
**Kelas:** 3A  
**Mata Kuliah:** Algoritma dan Pemrograman

---

# Daftar Berkas

| Berkas | Keterangan |
|--------|------------|
| `01_biodata.py` | Program menampilkan biodata dan menghitung perkiraan umur berdasarkan tahun lahir. |
| `02_persegi_panjang.py` | Program menghitung luas dan keliling persegi panjang menggunakan input panjang dan lebar. |
| `03_konversi_suhu.py` | Program mengonversi suhu dari Celsius ke Fahrenheit dan Kelvin. |
| `04_nilai_akhir.py` | Program menghitung nilai akhir berdasarkan bobot Tugas (20%), UTS (30%), dan UAS (50%). |
| `tugas_kalkulator_koordinat.py` | Program menghitung perubahan koordinat, jarak Euclidean, dan titik tengah dua titik. |
| `Laporan_Pertemuan_02.pdf` | Laporan praktikum yang berisi flowchart, source code, screenshot hasil running, dan pembahasan. |
| `README.md` | Dokumentasi proyek, test case, cara menjalankan program, refleksi, dan sumber. |

# Latihan 1 – Biodata Terformat

## Test Case

### Kasus 1
**Input**
- Nama : Aulia Rahma Ramadhani
- NIM : 2225250001
- Kelas : 3A
- Tahun Lahir : 2005

**Output**
- Umur : sekitar 21 tahun

**Penjelasan:**  
Program menerima data biodata dari pengguna, kemudian menghitung umur menggunakan rumus **2026 − 2005 = 21**. Kata *sekitar* digunakan karena perhitungan hanya berdasarkan tahun lahir.

---

# Latihan 2 – Persegi Panjang

## Test Case

### Kasus 1
**Input**
- Panjang = 8 cm
- Lebar = 5 cm

**Output**
- Luas = 40.00 cm²
- Keliling = 26.00 cm

**Penjelasan:**  
Luas dihitung dengan rumus **8 × 5 = 40**, sedangkan keliling dihitung dengan **2 × (8 + 5) = 26**.

### Kasus 2
**Input**
- Panjang = 2.5 cm
- Lebar = 4 cm

**Output**
- Luas = 10.00 cm²
- Keliling = 13.00 cm

**Penjelasan:**  
Program menerima bilangan desimal (*float*). Luas diperoleh dari **2.5 × 4 = 10**, sedangkan keliling **2 × (2.5 + 4) = 13**.

---

# Latihan 3 – Konversi Suhu

## Test Case

### Kasus 1
**Input**
- Celsius = 0°C

**Output**
- Fahrenheit = 32.00°F
- Kelvin = 273.15 K

**Penjelasan:**  
Program mengubah suhu 0°C ke Fahrenheit dan Kelvin menggunakan rumus konversi. Hasil menunjukkan titik beku air.

### Kasus 2
**Input**
- Celsius = 100°C

**Output**
- Fahrenheit = 212.00°F
- Kelvin = 373.15 K

**Penjelasan:**  
Program mengonversi suhu 100°C sehingga diperoleh 212°F dan 373.15 K, yang merupakan titik didih air.

---

# Latihan 4 – Nilai Akhir

## Test Case

### Kasus 1
**Input**
- Nilai Tugas = 80
- Nilai UTS = 80
- Nilai UAS = 80

**Output**
- Nilai Akhir = 80.00

**Penjelasan:**  
Semua nilai sama sehingga hasil pembobotan **20% + 30% + 50%** tetap menghasilkan nilai akhir **80.00**.

### Kasus 2
**Input**
- Nilai Tugas = 70
- Nilai UTS = 85
- Nilai UAS = 90

**Output**
- Nilai Akhir = 84.50

**Penjelasan:**  
Perhitungan bobot dilakukan sebagai berikut:
- Tugas = 70 × 20% = 14
- UTS = 85 × 30% = 25.5
- UAS = 90 × 50% = 45

Total nilai akhir = **84.50**.

---

# Tugas Utama – Kalkulator Koordinat Dua Titik

## Test Case Wajib

### Kasus 1
**Input**
- Titik A = (0, 0)
- Titik B = (3, 4)

**Output**
- dx = 3.00
- dy = 4.00
- Jarak = 5.00
- Titik Tengah = (1.50, 2.00)

**Penjelasan:**  
Perubahan koordinat adalah **dx = 3** dan **dy = 4**. Jarak dihitung menggunakan rumus Euclidean sehingga hasilnya **5.00**.

### Kasus 2
**Input**
- Titik A = (-2, 1)
- Titik B = (4, 1)

**Output**
- dx = 6.00
- dy = 0.00
- Jarak = 6.00
- Titik Tengah = (1.00, 1.00)

**Penjelasan:**  
Karena kedua titik memiliki nilai y yang sama, maka **dy = 0** sehingga jarak hanya dipengaruhi oleh sumbu x.

### Kasus 3
**Input**
- Titik A = (2.5, -1)
- Titik B = (2.5, 3)

**Output**
- dx = 0.00
- dy = 4.00
- Jarak = 4.00
- Titik Tengah = (2.50, 1.00)

**Penjelasan:**  
Kedua titik memiliki nilai x yang sama sehingga **dx = 0**. Jarak hanya berubah pada sumbu y sebesar **4 satuan**.

---

# Cara Menjalankan

Buka terminal pada folder utama proyek, kemudian jalankan file yang ingin diuji dengan perintah berikut:

```bash
python latihan/01_biodata.py
python latihan/02_persegi_panjang.py
python latihan/03_konversi_suhu.py
python latihan/04_nilai_akhir.py
python tugas_kalkulator_koordinat.py
```

---

# Refleksi

Pada Pertemuan 02 saya mempelajari dasar-dasar Python, seperti penggunaan **input**, **output**, variabel, tipe data (`int`, `float`, dan `string`), serta operasi aritmatika. Saya juga belajar membuat program sederhana, menggunakan **f-string** untuk menampilkan hasil yang rapi, dan menguji program dengan beberapa **test case** untuk memastikan hasil perhitungan sudah benar.

---

# Sumber

- Modul/Panduan Pertemuan 02 Algoritma dan Pemrograman.
- Materi praktikum yang diberikan oleh dosen.

