
# Latihan 4 Nilai Akhir

nama = input("Masukkan nama: ")
tugas = float(input("Masukkan nilai Tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

nilai_akhir = (0.20 * tugas) + (0.30 * uts) + (0.50 * uas)

print("\n===== HASIL NILAI =====")
print(f"Nama         : {nama}")
print(f"Nilai Akhir  : {nilai_akhir:.2f}")

if nilai_akhir >= 80:
    print("Status       : Lulus")
else:
    print("Status       : Belum Lulus")
