"""
Mějme zadaný následující seznam naměřených teplot. Seznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech časech - ráno, v poledne, večer a v noci.
"""

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]
#Vytvoř seznam průměrných teplot pro každý den.
prum_teplota = [round(sum(stupne)/len(stupne), 2) for stupne in teploty]
print(prum_teplota)
#Vytvoř seznam ranních teplot.
rano = [stupne[0] for stupne in teploty]
print(rano) 
#Vytvoř seznam nočních teplot.
noc = [stupne[3] for stupne in teploty]
print(noc) 
#Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.
poledne_a_noc = [[stupne[1], stupne[3]] for stupne in teploty]
print(poledne_a_noc) 
