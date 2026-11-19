#ulokha 1 vytvorte list o libovolnych 5 cislech a pomoci for cyklu spočítejte součet čísel v listu
#součet nakonec vypišteč

muj_list = [1, 2, 3, 4, 5]

soucet = 0

for i in range(len(muj_list)):
    soucet += muj_list[i]

print(soucet)

print("\n\n\n")

#ulokha 2 vytvorte list o libovolnych 5 cislech 
# seznam pomoci for cyklu vypište v opačném pořadí

for i in range(len(muj_list) - 1, -1, -1):
    print(muj_list[i])


#uloha 3 vytvořte list 5 libovolnych cisel a spocttejte pomoci for cyklu jejich aritmetický prumer

soucet = 0
for i in range(len(muj_list)):
    soucet += muj_list[i]

prumer = soucet / len(muj_list)
print(prumer)


#uloha 4 vytvořte list 5 libovolnych cisel a vypiste nejvyssi cislo ze seznamu
max = muj_list[0]

for i in range(1, len(muj_list)):
    if muj_list[i] > max:
        max = muj_list[i]


print(f"\nmaximum je {max}")


for item in muj_list:
    print(item)



#uloha 5 vytvořte list 5 libovolnych cisel a vypiste 2 nejvyssi cisla ze seznamu

muj_list = [50, 25, 2, 3, 4, 5, 27, 6, 7, 7, 8]

if muj_list[0] > muj_list[1]:
    nejvetsi = muj_list[0]
    druhy_nejvetsi = muj_list[1]
else:
    nejvetsi = muj_list[1]
    druhy_nejvetsi = muj_list[0]


for i in range(2, len(muj_list)):
    if muj_list[i] > nejvetsi:
        druhy_nejvetsi = nejvetsi
        nejvetsi = muj_list[i]
    elif muj_list[i] > druhy_nejvetsi:
        druhy_nejvetsi = muj_list[i]


print(f"Nejvetsi cislo je: {nejvetsi} \na druhy nejvetsi cislo je: {druhy_nejvetsi}")

