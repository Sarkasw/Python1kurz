
"""
Regularní výrazy
1 - datum
"""

import re

regularni_vyraz = re.compile(r"(\d{1,2}[\.|/] ?){2}\d{4}")
vstup = input("Zadej datum:")

hledani = regularni_vyraz.match(vstup)

if hledani:
    print("Datum je v pořádku.")
else:
    print("Nesprávné datum.")

"""
Regularní výrazy
2 - pošta

\d{3} ?\d\d ?\D{1}(\w| |\d){1,}


"""