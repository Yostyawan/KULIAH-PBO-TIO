class Kendaraan:
    def __init__(self, nama):
        self.nama = nama
        print(f"Sebuah Kendaraan '{self.nama}' dibuat.")
    
    def maju(self):
        print(f"{self.nama} bergerak maju.")
        
class Mobil(Kendaraan):
    def putar_AC(self):
        print(f"{self.nama}: AC dinyalakan, sejuk!")

print("--- Membuat Object Mobil ---")
avanza = Mobil("Avanza putih") 
avanza.maju() 
avanza.putar_AC()

print("---Membuat object motor---")
motor = Kendaraan("motor scoopy")   
motor.maju()   
motor.putar_AC()