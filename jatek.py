import random

print("Ez egy egyszerű játék")
print("Egy véletlenszerűen generált számot kell eltalálnod")
print("Hajrá! :)")
random = random.randint(1, 100)
tipp = int(input("Ide írd a tipped: "))
while tipp is not random:
    if tipp > random:
        print("Sajnos nem talált. Tippelj kisebbet!")
    else:
        print("Sajnos nem talált. Tippelj nagyobbat!")
    tipp = int(input("Fuss neki újra: "))
print("Eltaláltad! A szám %d volt" % random)
