

import random

passlaenge = int(input("enter the length of password"))

#werte="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

werte="abcdefghjklmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789!#?()" #gut lesbarer code

p = "".join(random.sample(werte,passlaenge ))

print(p)
