"""
Typování
"""
def over_cislo(cislo: str, ignoreSpaces: bool = False) -> bool:
    if ignoreSpaces == True:
        cislo = cislo.replace(" ", "")
    c = len(cislo)
    if c == 9:
        return True
    elif c == 13:
        if cislo[:4] == "+420":
            return True
    return False

def cena_zpravy(text: str) -> int:
    a = len(text)
    cena = int(a / 180)
    zbytek = a % 180
    if zbytek > 0:
        cena += 1
    cena = cena * 3
    return cena

cislo = input("Zadej telefonní číslo: ")
if over_cislo(cislo, True) == False:
    print("Telefonní číslo má chybný formát.")
else:
    text = input("Zadej text: ")
    cena = cena_zpravy(text)
    print(f"Zpráva je za {cena} Kč.")
