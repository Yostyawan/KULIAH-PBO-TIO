class Rectangle:
    def __init__(self, length, width):
        """
        Konstruktor untuk menginisialisasi panjang dan lebar persegi panjang.
        """
        self._length = length  # Atribut private untuk panjang
        self._width = width    # Atribut private untuk lebar
    
    def calculate_area(self):
        """
        Metode untuk menghitung luas persegi panjang.
        Rumus: luas = panjang * lebar
        """
        return self._length * self._width
    
    def calculate_perimeter(self):
        """
        Metode untuk menghitung keliling persegi panjang.
        Rumus: keliling = 2 * (panjang + lebar)
        """
        return 2 * (self._length + self._width)
    
    def display_info(self):
        """
        Metode tambahan untuk menampilkan informasi persegi panjang.
        """
        print(f"Panjang: {self._length}")
        print(f"Lebar: {self._width}")
        print(f"Luas: {self.calculate_area()}")
        print(f"Keliling: {self.calculate_perimeter()}")
# Bagian utama program (main)
if __name__ == "__main__":
    print("=== Program Menghitung Luas dan Keliling Persegi Panjang ===")
    
    # Input dari pengguna
    try:
        length = float(input("Masukkan panjang persegi panjang: "))
        width = float(input("Masukkan lebar persegi panjang: "))
        
        # Validasi input (harus positif)
        if length <= 0 or width <= 0:
            print("Error: Panjang dan lebar harus lebih besar dari 0!")
        else:
            # Membuat objek dari kelas Rectangle
            rect = Rectangle(length, width)
            
            # Menampilkan hasil
            print("\nInformasi Persegi Panjang:")
            rect.display_info()
            
    except ValueError:
        print("Error: Input harus berupa angka!")