# TUGAS 5   : Python Programming - Python Function and Class
# DIBERIKAN : 11.00 WIB - Jum'at, 04 September 2026
# DEADLINE  : 23.59 WIB - Sabtu, 12 September 2026
# NAMA FILE : tugas5.py

# NAMA      : AI - SITI FERDA FATINAH SESSU - MERGE 3 (ROTI BUAYA)


# 1. FUNCTION
def greet(nama: str) -> str:
    return f"Halo, {nama}!"

def tambah(a: float, b: float = 0.0) -> float:
    return a + b

def rata_rata(angka: list[float]) -> float:
    if not angka:
        return 0.0
    return round(sum(angka) / len(angka), 2)


# 2. CLASS STUDENT
class Student:
    def __init__(self, nama: str, nim: str, nilai: list[float] = None):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai if nilai is not None else []

    def tambah_nilai(self, skor: float) -> None:
        self.nilai.append(skor)

    def rata_nilai(self) -> float:
        # Memanfaatkan function rata_rata() yang dibuat di atas
        return rata_rata(self.nilai)

    def status(self, threshold: float = 70.0) -> str:
        if self.rata_nilai() >= threshold:
            return "LULUS"
        return "TIDAK LULUS"

    def __str__(self) -> str:
        return f"Student(nama='{self.nama}', nim='{self.nim}', rata={self.rata_nilai()}, status={self.status()})"


# 3. DEMO
if __name__ == "__main__":
    # Demo Functions
    print("=== FUNCTIONS ===")
    print(greet("Arifian"))
    print("tambah(5, 7)             :", tambah(5, 7))
    print("tambah(10)               :", tambah(10))
    print("rata_rata([80, 90, 100]) :", rata_rata([80, 90, 100]))
    print("rata_rata([])            :", rata_rata([]))

    # Demo Class Student
    print("\n=== CLASS STUDENT ===")

    # Mahasiswa 1 (Contoh status LULUS)
    mhs1 = Student(nama="Siti Ferda Fatinah Sessu", nim="2431182")
    mhs1.tambah_nilai(95.0)
    mhs1.tambah_nilai(90.0)
    mhs1.tambah_nilai(88.0)
    print(mhs1)
    print(f"Rata-rata: {mhs1.rata_nilai()} | Status: {mhs1.status()}")
    print("-" * 80)

    # Mahasiswa 2 (Contoh status TIDAK LULUS)
    mhs2 = Student(nama="Budi Santoso", nim="2431001")
    mhs2.tambah_nilai(60.0)
    mhs2.tambah_nilai(65.0)
    mhs2.tambah_nilai(55.0)
    print(mhs2)
    print(f"Rata-rata: {mhs2.rata_nilai()} | Status: {mhs2.status()}")
    print("-" * 80)

    # Mahasiswa 3 (Contoh nilai pas batas KKM 70.0 -> LULUS)
    mhs3 = Student(nama="Citra Lestari", nim="2431002")
    mhs3.tambah_nilai(65.0)
    mhs3.tambah_nilai(70.0)
    mhs3.tambah_nilai(75.0)
    print(mhs3)
    print(f"Rata-rata: {mhs3.rata_nilai()} | Status: {mhs3.status()}")