"""
Evidence aut
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
    
    def get_info(self):
        return f"Auto {self.reg_znacka} je {self.typ_vozidla}"

peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
skoda = Auto("1P3 4747", "Škoda Octavia", 41253)

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
    pujcit = input("Chceš půjčit auto? a/n: ")
