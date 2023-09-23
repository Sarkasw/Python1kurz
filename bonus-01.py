"""
bonus-01
Šárka

fomátování jména a příjmení
všechna písmena velká (vypíše např. JANA MALÁ)
všechna písmena malá (vypíše např. jana malá)
standardní varianta - první písmeno velké, další malá (vypíše např. Jana Malá)
iniciály (vypíše např. J. M.)
křestní jméno zkrácené na první písmeno a příjmení, pokud je křestní jméno delší než 5 znaků. Jinak vypíše standardní variantu, tj. první písmeno velké, další malá (u vstupu Jarmila Malá by došlo ke zkrácení křestního jména, zatímco u vstupu Jana Malá nikoliv)
"""
jmeno_a_prijmeni = input("Zadej jméno a příjmení: ")

print(jmeno_a_prijmeni.upper())
print(jmeno_a_prijmeni.lower())
cast = jmeno_a_prijmeni.split(" ")
jmeno = cast[0]
prijmeni = cast[1]
print(jmeno[0].upper() + jmeno[1:].lower() + " " + prijmeni[0].upper() + prijmeni[1:].lower())
print(jmeno[0].upper() + "." + " " + prijmeni[0].upper()+ ".")
if len(jmeno) >5:
    print(jmeno[0].upper() + "." + " " + prijmeni[0].upper() + prijmeni[1:].lower())
else:
    print(jmeno[0].upper() + jmeno[1:].lower() + " " + prijmeni[0].upper() + prijmeni[1:].lower())
    