'''
A program kérjen be egy számot, 
majd írja ki a kis szorzótáblát erre a számra (1-től 5-ig).
 A program a beolvasás után hagyjon ki egy üres sort. 

'''
print("This program will show you the 'mini-multiplication' table of the number you will give us!")

print("")

num1 = int(input("Give me a number: "))

print("")

n = 1
m = 1
for i in range(5):
    print(str(m) + " x " + str(num1) + " = " + str(num1 *n))
    n += 1
    m += 1



