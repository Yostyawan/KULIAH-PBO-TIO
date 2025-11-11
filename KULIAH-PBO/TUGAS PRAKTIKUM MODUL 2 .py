class Hero:
    __jumlah = 0  # Private class variable untuk menghitung total Hero yang dibuat

    def __init__(self, nama, health, attPower, armor):
        # Atribut private standar
        self.__name = nama
        self.__healthStandar = health
        self.__attPowerStandar = attPower
        self.__armorStandar = armor
        
        # Atribut level dan exp
        self.__level = 1
        self.__exp = 0
        
        # Atribut dinamis berdasarkan level
        self._healthMax = self.__healthStandar * self.__level  # Diperbaiki: gunakan __healthStandar
        self._attPower = self.__attPowerStandar * self.__level  # Diperbaiki
        self._armor = self.__armorStandar * self.__level  # Diperbaiki
        
        # Health saat ini sama dengan healthMax
        self._health = self._healthMax
        
        # Tambahkan 1 ke jumlah Hero
        Hero.__jumlah += 1

    @property
    def gainEXP(self):
        # Getter untuk gainEXP (hanya pass agar setter bisa berfungsi)
        pass

    @gainEXP.setter
    def gainEXP(self, addEXP):
        # Tambahkan EXP
        self.__exp += addEXP
        
        # Periksa level up
        while self.__exp >= 100:
            print(f"{self.__name} level up")
            self.__level += 1
            self.__exp -= 100
            
            # Hitung ulang atribut dinamis berdasarkan level baru
            self._healthMax = self.__healthStandar * self.__level  # Diperbaiki
            self._attPower = self.__attPowerStandar * self.__level  # Diperbaiki
            self._armor = self.__armorStandar * self.__level  # Diperbaiki
            
            # Set health saat ini ke healthMax baru (karena level up mengisi health penuh)
            self._health = self._healthMax

    def attack(self, musuh):
        # Tambahkan 50 EXP setiap kali menyerang
        self.gainEXP = 50

    @property
    def info(self):
        # Return string info dalam format yang diminta
        return f"{self.__name} level {self.__level}: \n\thealth = {self._health}/{self._healthMax} \n\tattack = {self._attPower} \n\tarmor = {self._armor}"  # Diperbaiki: gunakan __name dan __level

# Kode untuk test case
slardar = Hero('slardar', 100, 5, 10)
axe = Hero('axe', 100, 5, 10)
print(slardar.info)

slardar.attack(axe)
slardar.attack(axe)
slardar.attack(axe)

print(slardar.info)
