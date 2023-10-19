"""
Mějme zadaný následující seznam naměřených teplot. Seznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech časech - ráno, v poledne, večer a v noci. Krom teplot máme k dispozici i informaci o dnu v týdnu. Pomocí dict comprehension vytvoř slovník, který bude mít následující formát, kde klíčem bude den v týdnu, a hodnotou průměrná teplota ten den {den: průměrná teplota}.
"""
teploty = [
    ["pondělí", 2.1, 5.2, 6.1, -0.1],
    ["úterý", 2.2, 4.8, 5.6, -1.0],
    ["středa", 3.3, 6.5, 5.9, 1.2],
    ["čtvrtek", 2.9, 5.6, 6.0, 0.0],
    ["pátek", 2.0, 4.6, 5.5, -1.2],
    ["sobota", 1.0, 3.2, 2.1, -2.0],
    ["neděle", 0.4, 2.7, 1.3, -2.8]
]

denni_prumer = {den: round((rano + poledne + vecer + noc)/4, 2) for den, rano, poledne, vecer, noc in teploty}
print(denni_prumer)
