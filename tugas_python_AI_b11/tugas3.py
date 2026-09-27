# TUGAS 3   : Python Programming - Python Basics
# DIBERIKAN : 11.00 WIB - Jum'at, 04 September 2026
# DEADLINE  : 23.59 WIB - Sabtu, 12 September 2026
# NAMA FILE : tugas3.py

# NAMA      : AI - SITI FERDA FATINAH SESSU - MERGE 3 (ROTI BUAYA)


# 1. DEKLARASI VARIABEL DAN TIPE DATA (6 Tipe Data)
nama_lengkap = "SITI FERDA FATINAH SESSU"                   # String
semester     = 5                                            # Integer
ips_target   = 3.95                                         # Float
status_aktif = True                                         # boolean
hobi         = ["Mendengar lagu", "Menulis", "Rakit Lego", "Membaca", "Coloring Foto"]  # List
profil_data  = {                                            # dictionary
    "kampus": "Universitas Internasional Batam",
    "Prodi": "Sistem Informasi",
    "Peminatan Jurusan": "Data Intelligence"
}

print("- 1. VARIABEL & TIPE DATA -")
print("Data string     :", nama_lengkap, "| Tipe:", type(nama_lengkap))
print("Data integer    :", semester,     "| Tipe:", type(semester))
print("Data float      :", ips_target,   "| Tipe:", type(ips_target))
print("Data boolean    :", status_aktif, "| Tipe:", type(status_aktif))
print("Data list       :", hobi,         "| Tipe:", type(hobi))
print("Data dictionary :", profil_data,  "| Tipe:", type(profil_data))
print("-" * 157) #sekat pembatas


# 2. MANIPULASI STRING
pesan_semangat = "Tetap semangat yaa belajar dan eksplorasi hal baru nya Fatinah"
print("- 2. MANIPULASI STRING -")

# a. Menggabungkan string (+)
sapaan = "Halo, " + nama_lengkap + "! " + pesan_semangat
print("Hasil Gabungan                :", sapaan)

# b. Menghitung panjang karakter dengan len()
print("Panjang huruf kecil           :", len(pesan_semangat), "karakter (dihitung dari kalimat pesan)")

# c. Mengubah ke huruf besar (.upper())
print("Format huruf besar            :", pesan_semangat.upper())

# d. Mengubah ke huruf kecil (.lower())
print("Format huruf kecil            :", pesan_semangat.lower())

# e. Mengubah kapital di awal kata (.title())
print("Format kapital di awalan kata :", nama_lengkap.title())
print("-" * 157) #sekat pembatas


# 3. OPERASI MATEMATIKA SEDERHANA
angka_pertama = 25
angka_kedua   = 4

print("- 3. OPERASI MATEMATIKA -")
print(f"Angka Pertama = {angka_pertama}, Angka Kedua = {angka_kedua}")
print("Penjumlahan (+)        :", angka_pertama + angka_kedua)
print("Pengurangan (-)        :", angka_pertama - angka_kedua)
print("Perkalian (*)          :", angka_pertama * angka_kedua)
print("Pembagian (/)          :", angka_pertama / angka_kedua)
print("Pembagian Bulat (//)   :", angka_pertama // angka_kedua)
print("Modulus / Sisa Bagi (%):", angka_pertama % angka_kedua)
print("-" * 157) #sekat pembatas


# 4. LIST DAN AKSES ELEMEN
print("- 4. LIST & AKSES ELEMEN -")

# Menampilkan list awal (sudah berisi 5 item dari nomor 1)
print("Daftar hobi awal         :", hobi)

# a. Akses elemen tertentu berdasarkan indeks
print("Elemen pertama (index 0) :", hobi[0])
print("Elemen ketiga  (index 2) :", hobi[2])

# b. Menambah elemen baru ke dalam list (append)
hobi.append("Bermain Game")
print("Setelah ditambah (append):", hobi)

# c. Menghapus elemen
hobi.remove("Menulis")        # Menghapus item berdasarkan nilainya
item_terhapus = hobi.pop()    # Menghapus item urutan paling akhir
print("Setelah remove & pop     :", hobi)
print("Item yang dihapus pop()  :", item_terhapus)
print("-" * 157) # Sekat pembatas


#5. PENGGUNAAN INPUT DARI USER
print("- 5. PENGGUNAAN INPUT DARI USER -")
nama_user = input("Masukkan nama kamu : ")
umur_user = input("Masukkan umur kamu : ")

# Menampilkan kalimat perkenalan
print(f"Halo, nama saya {nama_user} dan umur saya {umur_user} tahun.")
print("-" * 157) # Sekat pembatas