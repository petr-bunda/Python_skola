vek = int(input("\n\n\nNapište svůj věk: \n"))


x = 18 - vek

if x == 1:
    roky = "rok"

elif x > 1 and x < 5:
    roky = "roky"

else:
    roky = "let"


if vek >= 18:
    print(f"Jste dospělý, běžte chlastat.\nJe Vám {vek}let.")

else:
    print(f"67, bez chlastat s rodici :DDDD.\nDo dospělosti ti zbývá {18 - vek} {roky}.\n\n\n\n")

