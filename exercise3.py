'''
Írjunk programot, amely beolvas két természetes számot,
 majd kiírja a két szám hányadosát és 
maradékát az alábbi formában. 
A program az adatok beolvasása után hagyjon ki egy üres sort. 

'''

num1 = int(input("Give me an integer: "))
num2 = int(input("Give me a 2nd integer: "))

#empty line
print("")


#answer
print("The quotient is: " + str(num1 // num2))
print("The remainder is: " + str(num1 % num2))


