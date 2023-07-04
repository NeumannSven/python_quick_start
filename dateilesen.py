# dateilesen.py

filecontent = ""

with open("passwoerter.txt", "r") as file:
    filecontent = file.read()

print(filecontent)