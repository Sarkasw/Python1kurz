"""
Soubor body.json je JSON, který obsahuje informace o získaných bodech z písemky.

Soubor si ulož a načti do slovníku.

Z písemky nebude známka, ale jen Pass/Fail hodnocení neboli prospěl(a)/neprospěl(a). Vytvoř nový slovník. Jeho klíče budou opět jména žáků, a hodnotou bude řetězec "Pass", pokud má jednotlivec alespoň než 60 bodů. Pokud má méně než 60, hodnota bude "Fail".

Výsledný slovník ulož jako JSON do souboru prospech.json.
"""
import json
prospech = {}
with open("body.json", mode="r", encoding="utf-8") as prospech:
    body = json.load(prospech)
    konec = len(body)
    with open("prospech.json", mode="w", encoding="utf-8") as prospech:
        print('{', file = prospech)
        #json.dump(prospech, soubor, ensure_ascii=False)
        for jmeno, vysledek in body.items():
            konec -= 1
            if vysledek >= 60:
                if konec == 0:
                    print('    "' + jmeno + '": "Pass"', file = prospech)
                else:
                    print('    "' + jmeno + '": "Pass",', file = prospech)
            else:
                if konec == 0:
                    print('    "' + jmeno + '": "Fail"', file = prospech)
                else:
                    print('    "' + jmeno + '": "Fail",', file = prospech)
        print('}', file = prospech)
