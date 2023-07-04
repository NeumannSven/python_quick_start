# python_quick_start
Python Schnelleinstieg


## Installation

https://thonny.org/

# Hallo Welt!

```python

# hallo.py

# Kommentar
print("Hallo Welt!")

```

## Variablen

```python

# variablen.py

# Text oder Zeichen (char oder string)
zeichen = "Dies ist ein Text"

print(zeichen)

# Ganzzahlen (integer)
ganzzahl = 42

print("ganzzahl = " + str(ganzzahl))

# Fließkommazahlen (float)
fliesskommazahl = 3.14

print("fliesskommanzahl = " + str(fliesskommazahl))

```

## Listen

```python

# listen.py

# Tuple
t = (1, 'Arthur', 17.23)

print(t)
print(t[1])

# geht nicht
#t[0] = 2
#del(t[0])
print(t.index('Arthur'))
print(len(t))
del(t)

# Listen
l = [1, 'Arthur', 17.23]

print(l)
print(l[1])

# das funktioniert
l[0] = 2
print(l)

# hinzufügen von items
l.append(5)
print(l)

l.insert(2, "insert 2")
print(l)

del(l[0])
print(l)

```

## Programmfluß

```python

# progfluss.py

# For Schleife
for number in range(10):
    print(number)

# While Schleife
number = 10
while number > 0:
    number -= 1
    print(number)

# If Statement
value1 = False
if value1:
    print("value1 = True")
else:
    print("value1 = False")

variable = 42
if variable == 12:
    print("variable = 12")
elif variable > 15 and variable <= 20:
    print("variable > 12 <= 20")
else:
    print("variable = " + str(variable))
    

```

## Programm Struktur

```python

# progstrukt.py

def funktionname(parameter1, parameter2):
    print(parameter1, parameter2)
    

def maxvalue(value1, value2):
    if value1 > value2:
        return value1
    return value2


funktionname(34, "Hallo")

print(maxvalue(42, 55))
print(maxvalue(42, 42))
print(maxvalue(42, 17))

```

Auslagern von Funktionen in ein Modul

```python

# mymodul.py

def funktionname(parameter1, parameter2):
    print(parameter1, parameter2)
    

def maxvalue(value1, value2):
    if value1 > value2:
        return value1
    return value2

```

Einbinden eines Moduls in ein Programm


```python

# prog.py
import mymodul

mymodul.funktionname(34, "Hallo")

print(mymodul.maxvalue(42, 55))
print(mymodul.maxvalue(42, 42))
print(mymodul.maxvalue(42, 17))

```

## Applikation
```python

# passgen.py
import random

passwortlaenge = int(input("Bitte die Passwortlänge eingeben: "))

kleinbuchstaben = "abcdefghijklmnopqrstuvwxyz"
grossbuchstaben = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sonderzeichen = "!@#$%^&*()?"
zahlen = "0123456789"

werte = kleinbuchstaben + grossbuchstaben + sonderzeichen + zahlen

# gut lesbare werte
# werte="abcdefghjklmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789!#?()" 

print(random.sample(werte, passwortlaenge))

passwort = "".join(random.sample(werte, passwortlaenge))

print(passwort)

```

## Dateien
```python

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


```

```python

# dateilesen.py

filecontent = ""

with open("passwoerter.txt", "r") as file:
    filecontent = file.read()

print(filecontent)


```