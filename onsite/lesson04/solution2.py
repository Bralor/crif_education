pismena = ["a", "a", "b", "c", "d", "a", "e", "g", "m"]
print("Začátek:", ", ".join(pismena))

while pismena:
    zadani = input("ktere písmeno chceš vyhodit? ")

    if zadani in pismena:
        pismena.remove(zadani)

        if pismena:
            print(", ".join(pismena))
    else:
        print(zadani, "není součástí písmen!")

else:
    print("Seznam je prázdný!")
