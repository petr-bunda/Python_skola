#uzivatel zada cele cislo a program zada cele cislo a program napise slovo "ahoj" tolikrat.

a = int(input("Cislo, vole: \n"))
print("\n")

for i in range(a):
    print("ahoj")
print("\n")


#uloha 2: uzivatel  zada ciso a program vypise odpocet od zadaneho cisla do nuly (včetně)

for i in range(a, -1, -1):
    print(i)
print("\n")


for i in range(a + 1):
    print(a - i)
print("\n")


# uloha 3: uzivatel zada cislo a program vypise cisla od nuly do zadaneho cisla (vcetne)
# ale jen cisla suda (nula je suda)

for i in range(0, a + 1, 2):
    print(i)
print("\n")


for i in range(a+1):
    if i % 2 == 0:
        print(i)
print("\n")

for i in range(int(a/2) + 1):
    print(2*i)
print("\n")


# uloha 4: uzivatel zada cislo a program vypise cisla od nuly do zadaneho cisla (vcetne)
#a k tomu vypise, zda je aktualni cislo sude nebo liche

for i in range(a + 1):
    if i % 2 == 0:
        print(f"{i} je sude")
    else:
        print(f"{i} je liche")
print("\n")

