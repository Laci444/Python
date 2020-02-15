
# Nubers, String, Boolean, List, Tuple, Dictionary, user defined

# number
szam0 = 10
szam1 = 3.14
szam2 = 12.35e6
szam3 = .234j

# string
str0 = "valami"
str1 = 'valami'

# boolean
igaz = True
hamis = False

# list
lista = []

# tuple
mytuple = ()

# dictionary
mydict = {}

print(type(mydict))


# + - * / // ** %

x = 5
y = 10

print(x+y)
print(x-y)
print(x*y)
print(y/x)
print(y//x)
print(x**10)
print(y%x)


# = += -= *= /* //= %= **=
# < > <= >= != ==
# and or not


# listák

list1 = [123, 'asd']
print(list1)
list1.append("alma")
list1.append(100)
print(list1)
list1.remove(123) # az összes 123-at törli
print(list1)
list1.clear()
print(list1)
list1.append('Anikó')
list1.append('Enikő')
list1.append('Bözsi')
list1.append('Margaréta')
list1.insert(2, 'Boglárka')
print(list1)
list1.reverse()
print(list1)
list2 = [12, 32, 65, 38, 62, 82, 10, 6, 74]
list2.sort()
print(list2)
print(len(list2))
print(list2[2]) # indexelés
print(list2[0:2]) # szeletelés
print(list2[2:]) # 3. elemtől a végéig
print(list2[-1]) # hátulról az elő
list3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list3[1][2])
tartomany = range(100)
print(list(tartomany))

# for ciklus
for i in range(10):
    print('hello word %d ')
print("a")
x = 4
for x in range(1, 11):
    for y in range(1, 11):
        print('%d * %d = %d' % (x, y, x*y))
