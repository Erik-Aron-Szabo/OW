'''
A program kérjen be egy pénzösszeget, majd határozza meg,
 és írja ki, hogy hogyan fizethetjük ki a 
lehető legkevesebb 10, 5, 2 és 1 koronás érmével 
(használjuk a maradékos osztás % és egész osztás // műveleteket)! 

'''
print("Meg fogom mondani, a megadott osszeget, mennyi koronaval todja felvaltani 10esekben, 5osokben, 2esekben, es 1esekben!")

print("")

sum = int(input("Adjon meg egy osszeget: "))

# i = maradek
m10 = sum // 10
i10 = sum % 10
m5 = (i10) // 5
i5 = i10 % 5
m2 =  i5 // 2
i2 = i5 % 2
m1 = i2 // 1
i1 = i2 % 1

print("Ennyi 10-es kell: ")
print(m10)

print("Ennyi 5-os kell: ")
print(m5)

print("Ennyi 2-es kell: ")
print(m2)

print("Ennyi 1-es kell: ")
print(m1)



