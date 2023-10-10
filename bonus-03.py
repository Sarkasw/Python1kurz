"""
Krom souboru s body si ulož a načti do druhého slovníku ještě soubor bonusy.json. Obsahuje bonusové body získané během semestru. Pozor, bonusové body získali jen někteří žáci.

Tvým úkolem je žákům přiřadit známky na základě součtu bodů z písemky a bonusových bodů. Bodová rozhraní (vztahují se na součet) najdeš zde:

1: 90 a více
2: 70-89
3: 50-69
4: 30-49
5: 29 a méně
Výsledný slovník ulož jako JSON do souboru znamky.json.
"""
import json

with open("body.json", mode="r", encoding="utf-8") as data:
    kod = json.load(data)
with open("bonusy.json", mode="r", encoding="utf-8") as bonus:
    kod2 = json.load(bonus)

    with open("znamky.json", mode="w", encoding="utf-8") as soubor:
        for jmeno, vysledek in kod.items():
            if jmeno in kod2:
                for jmeno2, vysledek2 in kod2.items():
                    celkem = int(vysledek) + int(vysledek2)
                    if celkem >= 90:
                        kod[jmeno] = "1"
                    elif celkem >= 70:
                        kod[jmeno] = "2"
                    elif celkem >= 50:
                        kod[jmeno] = "3"
                    elif celkem >= 30:
                        kod[jmeno] = "4"
                    else:
                        kod[jmeno] = "5"
            else:
                celkem = int(vysledek)
                if celkem >= 90:
                    kod[jmeno] = "1"
                elif celkem >= 70:
                    kod[jmeno] = "2"
                elif celkem >= 50:
                    kod[jmeno] = "3"
                elif celkem >= 30:
                    kod[jmeno] = "4"
                else:
                    kod[jmeno] = "5"
        json.dump(kod, soubor, ensure_ascii=False, indent = 4)
