class Hero:
    
    # class variabel/atribut
    jumlah_hero = 0 
    
    # membuat konstruktor
    def __init__(self, nama, health, power, armor):
        # instance/objek atribut
        self.nama = nama
        self.health = health
        self.power = power
        self.armor = armor
        Hero.jumlah_hero += 1 
        
    # membuat method dengan return tanpa param
    def siapa_hero(self):
        return f"Hero {self.nama}, memiliki power {self.power}"
        
    # membuat method dengan param tanpa return
    def health_up(self, up):
        self.health += up # health = health + up (1, dst)
        
    # membuat method dengan return
    def getHealth(self):
        return self.health

# membuat objek
hero1 = Hero("Tio", 100, 50, 10)
hero2 = Hero("Agus", 100, 70, 5)

print(hero1.siapa_hero())
print(hero2.siapa_hero())

print(hero1.getHealth())

hero1.health_up(10)
print(hero1.getHealth())

print("Jumlah Hero : ", Hero.jumlah_hero)

hero3 = Hero("Setiawan",200,90,20)
print(hero3.siapa_hero())

print("jumlah Hero : ", Hero.jumlah_hero)