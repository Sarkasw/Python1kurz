
"""
Regularní výrazy

"""
import re

reg_vyraz_jmeno = re.compile(r"\w{6}\w{0,4}")
jmeno = input("Zadej přihlašovací jméno:")
hledani = reg_vyraz_jmeno.match(jmeno)
if hledani:
    print("Přihlašovací jméno je v pořádku.")
else:
    print("Nesprávné přihlašovací jméno.")

reg_vyraz_mail = re.compile(r"(\w|\d|-|\"){1,}\.{0,1}(\w|\d|-|\+|=|\"){1,}@\[?|\d{3}\.\d{3}\.\d{3}\.\d{3}\]?|(\w)(\w|\d|-){1,}\.\w{1,}\.?\w{1,}")
mail = input("Zadej e-mailovou adresu:")
hledani = reg_vyraz_mail.match(mail)
if hledani:
    print("E-mailová adresa je v pořádku.")
else:
    print("Nesprávná e-mailová adresa.")

reg_vyraz_heslo = re.compile(r"(\w|-|\.|\+|\=){12,30}")
heslo = input("Zadej přihlašovací heslo:")
hledani = reg_vyraz_heslo.match(heslo)
if hledani:
    print("Heslo je v pořádku.")
else:
    print("Nesprávné heslo.")
