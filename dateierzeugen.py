# dateierzeugen.py
import random

passwortlaenge = 8

# gut lesbare werte
werte="abcdefghjklmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789!#?()" 

filecontent = ""

for zeile in range(10):
    for spalte in range(4):
        filecontent += "".join(random.sample(werte, passwortlaenge)) + "  "
    filecontent += "\n"

with open("passwoerter.txt", "w") as file:
    file.write(filecontent)
