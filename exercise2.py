''' Kérjünk be két, egy napon belüli, időpontot 
(először az órát, aztán a percet, végül a másodpercet). 
Számítsuk ki a két időpont közti különbséget másodpercekben 
és írassuk ki! '''

print("You're gonna give me 2 times in a day! \n (First the hour, then the minute, then the second)...")

print("We're going to calculate the difference, between your 1st given time - your 2nd given time, and will give you the answer in seconds...")

h1 = float(input("Give me the hour: "))
m1 = float(input("Give me the minute: "))
s1 = float(input("Give me the second: "))

h2 = float(input("Give me the 2nd hour: "))
m2 = float(input("Give me the 2nd minute: "))
s2 = float(input("Give me the 2nd second: "))



h1 += m1 * 60
s1 = round(h1 * 3600, 1)

h2 += m2 * 60
s2 = round(h2 * 3600, 1)

print("The difference is: " + str((s1 - s2)))
