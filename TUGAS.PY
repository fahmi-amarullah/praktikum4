# Program: Input Data Mahasiswa
# Menggunakan list untuk menyimpan data banyak mahasiswa

data_mahasiswa = []

while True:
    print()
    nama = input("Nama        : ")
    nim = input("NIM         : ")
    tugas = float(input("Nilai Tugas : "))
    uts = float(input("Nilai UTS   : "))
    uas = float(input("Nilai UAS   : "))

    # Hitung nilai akhir
    akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

    # Simpan ke dalam list sebagai dictionary
    data_mahasiswa.append({
        "nama": nama,
        "nim": nim,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "akhir": akhir
    })

    # Tanya apakah ingin menambah data lagi
    tambah = input("Tambah data (y/t)? ")
    if tambah.lower() == 't':
        break

# Tampilkan data dalam bentuk tabel
print("\nDaftar Nilai Mahasiswa")
print("="*60)
print("| No | Nama        | NIM   | Tugas | UTS  | UAS  | Akhir |")
print("="*60)

no = 1
for mhs in data_mahasiswa:
    print(f"| {no:<2} | {mhs['nama']:<10} | {mhs['nim']:<5} | "
          f"{mhs['tugas']:<5} | {mhs['uts']:<4} | {mhs['uas']:<4} | {mhs['akhir']:<6.2f} |")
    no += 1
print("="*60)
