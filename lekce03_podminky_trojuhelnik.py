a = int(input("\n\nZadej delku strany A v trojuhelniku ABC:\n"))
b = int(input("Zadej delku strany B v trojuhelniku ABC:\n"))
c = int(input("Zadej delku strany C v trojuhelniku ABC:\n"))

if a + b > c and a + c > b and c + b > a:
    print("\nTrojuhelnik lze zkonstruovat :D")
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Trojůhelník je pravoůhlý :DDDDDDD")
elif a + b == c and a + c == b and c + b == a:
    print("mas lajnu debile")
else:
    print("\nJsi debil blehehehe.\n")

print("\n")
