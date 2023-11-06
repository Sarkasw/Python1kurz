"""
Evidence aut a vácení auta
"""
class Auto:
    def __init__(self, reg_znacka, typ_vozidla, najete_km, dostupne = True):
        self.reg_znacka = reg_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = dostupne

    def pujc_auto(self):
        if (self.dostupne == True):
            self.dostupne = False
            return "Potvrzuji zapůjčení vozidla."
        else:
            return "Vozidlo není k dispozici."
        
    def vrat_auto(self, stav_tachometru, dny_vypujcky):
        self.najete_km = stav_tachometru
        self.dny_vypujcky = dny_vypujcky
        self.dostupne = True
        print(f"Auto {self.reg_znacka} má najeto {self.najete_km} .")
        if (int(self.dny_vypujcky) > 7):
            return f"Cena zapůjčení je {int(self.dny_vypujcky) * 300} ."
        else:
            return f"Cena zapůjčení je {int(self.dny_vypujcky) * 400} ."

    def get_info(self):
        return f"Auto {self.reg_znacka} je {self.typ_vozidla} ."

peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
skoda = Auto("1P3 4747", "Škoda Octavia", 41253)

vratit = "a"
pujcit = "a"
pujcit = input("Chceš půjčit auto? a/n: ")
while pujcit == "a":
    dotaz = input("Jakou značku chceš půjčit? ")
    if dotaz == "Peugeot":
        print(peugeot.get_info())
        print(peugeot.pujc_auto())
    elif dotaz == "Škoda":
        print(skoda.get_info())
        print(skoda.pujc_auto())
    else:
        print("Máme značku Škoda a Peugeot.")
    if (peugeot.dostupne) == False:
        vratit = input("Chceš vrátit Peugeot? a/n: ")
        if vratit == "a":
            print(peugeot.vrat_auto(48000, 9))
    if (skoda.dostupne) == False:
        vratit = input("Chceš vrátit Škodu? a/n: ")
        if vratit == "a":
            print(skoda.vrat_auto(42000, 5))
    pujcit = input("Chceš půjčit auto? a/n: ")
