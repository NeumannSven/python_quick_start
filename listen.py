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





