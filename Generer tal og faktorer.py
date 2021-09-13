antal = 1000

tal = 3
while tal < antal:
    x = 2
    y = 0

    while x < antal:
        if tal == x:
            break
        elif tal % x != 0:
            x += 1
        elif tal % x == 0:
            print(tal,"har", x, "som faktor")
            x += 1
            y += 1


    print("\n""Tallet", tal, "har", y, "faktorer", "\n")
    tal += 1

