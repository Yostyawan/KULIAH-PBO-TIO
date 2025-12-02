class Pegawai:
    def __init__(self, nama, nip, gaji_pokok):
        self.nama = nama
        self.nip = nip
        self.__gaji_pokok = gaji_pokok
    
    def get_gaji_pokok(self):
        return self.__gaji_pokok
    
    def hitung_bonus(self):
        # Method ini akan di-override oleh child classes
        return 0
    
    def get_gaji_total(self):
        # Menggunakan int() agar hasil selalu integer (tanpa .0)
        return int(self.__gaji_pokok + self.hitung_bonus())
    
    def tampilkan_info(self):
        print(f"Nama: {self.nama}, NIP: {self.nip}")
        print(f"Gaji Pokok: Rp {self.__gaji_pokok:,}")

class Manager(Pegawai):
    def __init__(self, nama, nip, gaji_pokok, tunjangan_jabatan):
        super().__init__(nama, nip, gaji_pokok)
        self.tunjangan_jabatan = tunjangan_jabatan
    
    def hitung_bonus(self):
        return 0.15 * self.get_gaji_pokok()
    
    def tampilkan_info(self):
        print("--- Info Manager ---")  # Header wajib ada
        super().tampilkan_info()  # Cetak nama, NIP, gaji pokok
        print(f"Tunjangan: Rp {self.tunjangan_jabatan:,}")
        print(f"Gaji Total Manager: Rp {self.get_gaji_total():,}")
        print("=" * 30)

class StaffTeknis(Pegawai):
    def __init__(self, nama, nip, gaji_pokok, jumlah_proyek):
        super().__init__(nama, nip, gaji_pokok)
        self.jumlah_proyek = jumlah_proyek
    
    def hitung_bonus(self):
        return 500000 * self.jumlah_proyek
    
    def tampilkan_info(self):
        print("--- Info Staff Teknis ---")
        super().tampilkan_info()
        print(f"Jumlah Proyek: {self.jumlah_proyek}")
        print(f"Gaji Total Staff: Rp {self.get_gaji_total():,}")
        print("=" * 30)

# Membuat instance
manager = Manager("Budi Hartono", "M-001", 10000000, 5000000)
staff = StaffTeknis("Susi Susanti", "S-001", 6000000, 3)

# Menampilkan info (pastikan ini dijalankan!)
manager.tampilkan_info()
staff.tampilkan_info()

# Tes Keamanan (Encapsulasi)
print("--- Tes Keamanan (Encapsulasi) ---")
try:
    print(staff.__gaji_pokok)  # Akan gagal
except AttributeError as e:
    print(f"ERROR: {e} -> TIDAK BISA diakses langsung dari luar!")
    print(f"Gaji Total Susi (tetap): Rp {staff.get_gaji_total():,}")
