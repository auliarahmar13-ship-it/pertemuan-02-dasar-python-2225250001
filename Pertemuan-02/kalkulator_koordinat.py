
# Nama : Aulia Rahma Ramadhani
# NIM  : 2225250001
# Tugas Utama Kalkulator Koordinat

x1 = float(input("Masukkan x titik A: "))
y1 = float(input("Masukkan y titik A: "))
x2 = float(input("Masukkan x titik B: "))
y2 = float(input("Masukkan y titik B: "))

dx = x2 - x1
dy = y2 - y1

jarak = ((dx ** 2) + (dy ** 2)) ** 0.5

xt = (x1 + x2) / 2
yt = (y1 + y2) / 2

print("\n===== HASIL =====")
print(f"Titik A      : ({x1:.2f}, {y1:.2f})")
print(f"Titik B      : ({x2:.2f}, {y2:.2f})")
print(f"dx           : {dx:.2f}")
print(f"dy           : {dy:.2f}")
print(f"Jarak        : {jarak:.2f}")
print(f"Titik Tengah : ({xt:.2f}, {yt:.2f})")