#Find ud af om dit tal er et primtal

tal = input("Skriv et tal, som du er usikker på er et primtal: ")

if tal.isdigit():
    tal = int(tal) #vi tjekker om det er et tal

    if tal <= 0: #tjekker om tallet er større end nul
        print("Skriv gerne et tal, der er større end 0 næste gang. ")
        quit()
else:
    print("Skriv gerne et tal næste gang. ")
    quit()

print("\n""Du har valgt tallet:", tal, "\n" )

x = 2
y = 0

while x < 1000000:
    if tal == x:
        break
    elif tal % x != 0:
        x += 1
    elif tal % x == 0:
        print("Dit tal har", x, "som faktor")
        x += 1
        y += 1


print("\n""Dit tal har", y, "faktorer. Hvis tallet er 0, er det et primtal")

