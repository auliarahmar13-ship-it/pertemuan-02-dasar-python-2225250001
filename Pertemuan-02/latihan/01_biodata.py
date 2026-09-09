
# Latihan 1 Biodata Terformat

TAHUN_SEKARANG = 2026

nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
kelas = input("Masukkan Kelas: ")
tahun_lahir = int(input("Masukkan Tahun Lahir: "))

umur = TAHUN_SEKARANG - tahun_lahir

print("\n===== BIODATA =====")
print(f"Nama         : {nama}")
print(f"NIM          : {nim}")
print(f"Kelas        : {kelas}")
print(f"Umur         : sekitar {umur} tahun")
