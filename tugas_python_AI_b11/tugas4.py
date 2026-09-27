# TUGAS 4   : Python Programming - Python Data Structures
# DIBERIKAN : 11.00 WIB - Jum'at, 04 September 2026
# DEADLINE  : 23.59 WIB - Sabtu, 12 September 2026
# NAMA FILE : tugas4.py

# NAMA      : AI - SITI FERDA FATINAH SESSU - MERGE 3 (ROTI BUAYA)


# 1. LIST – AKSES & MANIPULASI
print("- 1. LIST: AKSES & MANIPULASI -")

# Buat list 6 elemen campuran
data = ["apel", 10, "jeruk", 20, "mangga", 30]  # index 0: "apel", index 1: 10, index 2: "jeruk", index 3: 20, index 4: "mangga", index 5: 30
print("List awal       :", data)

# Akses pertama, terakhir, dan slicing loncat 2 langkah [start:stop:step]
print("Elemen pertama  :", data[0])
print("Elemen terakhir :", data[-1])
print("Slicing [0:6:2] :", data[0:6:2])     #start dari index 0, stop di index 6 dengan lompatan 2 langkah. jadi itu akan mengambil index 0, 2, 4. hasilnya ['apel', 'jeruk', 'mangga'], lalu akan kembali ke list awal lagi untuk index ke enamnya di apel.

# Manipulasi list
print("\nSebelum diubah  :", data)

data.append("pisang")         # Tambah ke belakang
data.insert(1, "anggur")      # Sisip di posisi kedua
data.extend(["melon", 50])    # Tambah beberapa data sekaligus
data.pop()                    # Hapus data paling belakang
data.remove(10)               # Hapus angka 10

print("Sesudah diubah  :", data)
print("-" * 82) #sekat pembatas


# 2. TUPLE – IMMUTABILITY & UNPACKING
print("- 2. TUPLE: IMMUTABILITY & UNPACKING -")

# Tuple dengan >= 5 elemen
data_tuple = ("Siti Ferda Fatinah Sessu", "Sistem Informasi", 2024, 3.95, "Batam", "Aktif")
print("Data Tuple               :", data_tuple)
print("Panjang Tuple (len)      :", len(data_tuple))
print("Akses Elemen Indeks ke-1 :", data_tuple[1])

# Unpacking (minimal 3 variabel dengan *rest)
nama, prodi, *detail_lain = data_tuple
print("Hasil Unpacking nama     :", nama)
print("Hasil Unpacking prodi    :", prodi)
print("Hasil Unpacking *rest    :", detail_lain)
print("-" * 82) #sekat pembatas


# 3. SET – KEUNIKAN & OPERASI HIMPUNAN
print("- 3. SET: KEUNIKAN & OPERASI HIMPUNAN -")

# Dua set angka (tumpang tindih di angka 3 dan 4)
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("Set A                :", set_a)
print("Set B                :", set_b)

# Operasi himpunan
print("Gabungan (|)         :", set_a | set_b)    # Semua angka digabung
print("Irisan (&)           :", set_a & set_b)    # Angka yang sama di kedua set
print("Selisih (A - B)      :", set_a - set_b)    # Angka di A yang tidak ada di B
print("Beda Simetris (^)    :", set_a ^ set_b)    # Semua angka kecuali yang sama

# Bukti duplikat otomatis dibuang
angka_kembar = {1, 1, 2, 2, 3, 3}
print("\nData kembar dimasukkan : {1, 1, 2, 2, 3, 3}")
print("Hasil otomatis unik    :", angka_kembar)
print("-" * 82) #sekat pembatas


# 4. DICTIONARY – KEY/VALUE DASAR
print("- 4. DICTIONARY: DATA MAHASISWA -")
mahasiswa = {
    "nama": "Siti Ferda Fatinah Sessu",
    "nim": "2431182",
    "angkatan": 2024,
    "kota": "Batam"
}
print("Dict awal                :", mahasiswa)

# Operasi: tambah key, ubah nilai, hapus key
mahasiswa["status"] = "Aktif"     # Tambah key baru
mahasiswa["kota"] = "Makassar" # Ubah nilai key
del mahasiswa["angkatan"]         # Hapus key

print("Dict setelah diedit      :", mahasiswa)
print("Keys ()                  :", list(mahasiswa.keys()))
print("Values ()                :", list(mahasiswa.values()))
print("Items ()                 :", list(mahasiswa.items()))

print("\nIterasi Key - Value:")
for key, val in mahasiswa.items():
    print(f"  * {key} : {val}")
print("-" * 82) #sekat pembatas


# 5. NESTED STRUCTURES
print("- 5. NESTED STRUCTURES (DAFTAR BUKU) -")

# List berisi 4 dictionary novel karya Tere Liye
daftar_buku = [
    {"judul": "Bumi", "penulis": "Tere Liye", "tahun": 2014},
    {"judul": "Bulan", "penulis": "Tere Liye", "tahun": 2015},
    {"judul": "Hujan", "penulis": "Tere Liye", "tahun": 2016},
    {"judul": "Bintang", "penulis": "Tere Liye", "tahun": 2017}
]

# Cetak semua judul menggunakan for loop
print("Daftar Semua Judul Buku:")
for buku in daftar_buku:
    print(f"  - {buku['judul']}")

# Filter buku terbit >= 2016 dengan list comprehension
buku_terbaru = [buku["judul"] for buku in daftar_buku if buku["tahun"] >= 2016]
print("\nBuku terbit >= 2016 (List Comp):", buku_terbaru)
print("-" * 82) #sekat pembatas


# 6. COMPREHENSION & UTILITAS
print("- 6. COMPREHENSION & UTILITAS -")

# a. List comprehension dari angka 1–20 (genap & kuadrat)
angka = range(1, 21)
list_genap = [x for x in angka if x % 2 == 0]
list_kuadrat = [x**2 for x in angka]

print("List Angka Genap (1-20)   :", list_genap)
print("List Angka Kuadrat (1-20) :", list_kuadrat)

# b. Dict comprehension mapping genap/ganjil untuk angka 1–10
mapping_angka = {x: ("genap" if x % 2 == 0 else "ganjil") for x in range(1, 11)}
print("\nMapping Ganjil/Genap (1-10):", mapping_angka)

# c. Set comprehension: ambil huruf unik (lowercase) dari kalimat judul buku
kalimat = "membaca novel tere liye"
huruf_unik = {huruf for huruf in kalimat.lower() if huruf != " "}

print("\nKalimat Asli              :", kalimat)
print("Huruf Unik (Set Comp)     :", sorted(huruf_unik))
print("-" * 82) # Sekat pembatas


# 7. KEANGGOTAAN & PENCARIAN SEDERHANA
print("- 7. KEANGGOTAAN & PENCARIAN SEDERHANA -")

# Menggunakan data novel dan kota agar nyambung dengan nomor sebelumnya
daftar_novel = ["Bumi", "Bulan", "Hujan", "Bintang"]
daftar_kota  = {"Batam", "Makassar", "Bandung"}

# a. Pengecekan pada list menggunakan 'in' dan mencari letaknya dengan index()
cari_buku = "Hujan"
if cari_buku in daftar_novel:
    posisi = daftar_novel.index(cari_buku)
    print(f"Buku '{cari_buku}' ditemukan di dalam list pada indeks ke-{posisi}.")
else:
    print(f"Buku '{cari_buku}' tidak ada di daftar.")

# b. Pengecekan pada set menggunakan 'in'
cari_kota = "Batam"
if cari_kota in daftar_kota:
    print(f"Kota '{cari_kota}' ditemukan di dalam himpunan set kota.")
else:
    print(f"Kota '{cari_kota}' tidak ditemukan.")

print("-" * 82) # Sekat pembatas