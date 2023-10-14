"""
Aplikace pro zasílání SMS zpráv.
Dotaz na číslo, ověří formát a ze zadaného čísla odstraní případné mezery.
Zeptá se na zprávu, kterou chce zaslat. Vypíše, kolik zpráva bude stát.
První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu True, jinak vrátí hodnotu False.
Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
"""
def over_cislo(cislo):
    cislo = cislo.replace(" ", "")
    c = len(cislo)
    if c == 9:
        return True
    elif c == 13:
        if cislo[:4] == "+420":
            return True
    return False

def cena_zpravy(text):
    a = len(text)
    cena = int(a / 180)
    zbytek = a % 180
    if zbytek > 0:
        cena += 1
    cena = cena * 3
    return int(cena)

cislo = input("Zadej telefonní číslo: ")
if over_cislo(cislo) == False:
    print("Telefonní číslo má chybný formát.")
else:
    text = input("Zadej text: ")
    cena = cena_zpravy(text)
    print(f"Zpráva je za {cena} Kč.")
