x = 10

while(x > 5):
    print("ahoj")
    x = x-1 
    if x == 7:
        continue
    print(x)

print("konec\n\n\n")



#podminka na zacatku:
x = 10

while(x > 5):
    print("ahoj")
    x = x-1 
    if x == 7:
        break
    print(x)

print("konec\n\n\n")

#podminka na konci:
while True:
    print("Vyber Moznost: A: napis ahoj, X: konec")
    y = input('Zadej volbu: ')
    if y =="X":
        break
    if y =="A":
        print("\nahoj\n")

print("\nkonec\n\n\n")