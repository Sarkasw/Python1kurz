"""
ukol-02
Šárka

Dotaz na kód součástky,
dotaz na množství, které chce zákazník koupit. 
Obě informace uložit.
Pokud zadaný kód není ve slovníku, není součástka skladem. Vypiš, že součástka není skladem.
Pokud zadaná součástka na skladě je, ale je jí méně, než požaduje zákazník, vypiš text o tom, že lze prodat pouze omezené množství kusů. Následně součástku odeber ze slovníku, protože je vyprodaná.
Pokud zadaná součástka na skladě je a je jí dostatek, vypiš informaci, že poptávku lze uspokojit v plné výši, a sniž počet součástek na skladě o množství požadované zákazníkem.
"""

sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}
kod_soucastky = input("Zadej kód součástky: ")
if kod_soucastky in sklad:
    mnozstvi = int(input("Zadej množství: ")) 
    if sklad[kod_soucastky] < mnozstvi:
        print(f"Lze prodat pouze {sklad[kod_soucastky]} kusů.")
        sklad.pop(kod_soucastky)
    else:
        print("Poptávku lze uspokojit v plné výši.")
        sklad[kod_soucastky] -= mnozstvi
else:
    print(f"Součástka {kod_soucastky} není skladem.")
for kod_soucastky, kusy in sklad.items():
    print(f"Součástka {kod_soucastky} skladem {kusy} kusů.")
"""
Dle zadání by input na řádku 22 měl být před if na řádku 21, ale
množství by se zadávalo i u součástky, která není na skladě. 
"""