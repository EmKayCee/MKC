def primtal(tal):
    a = tal - 1
    faktorer = []

    while a > 1:
        if tal % a == 0:
            print(tal, "har", a ,"som faktor")
            a -= 1
        elif tal % a != 0:
            a -= 1


print(primtal(92))
