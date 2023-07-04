# passgen.py
import random

passwortlaenge = int(input("Bitte die Passwortlänge eingeben: "))

kleinbuchstaben = "abcdefghijklmnopqrstuvwxyz"
grossbuchstaben = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sonderzeichen = "!@#$%^&*()?"
zahlen = "0123456789"

werte = kleinbuchstaben + grossbuchstaben + sonderzeichen + zahlen

passwort = "".join(random.sample(werte, passwortlaenge))

print(passwort)
