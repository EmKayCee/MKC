import random

antal_kerner = 1000

count = 0

while antal_kerner > 0:

    henfald_1 = []

    while antal_kerner > 0:
        henfald_random = random.randint(1, 6)
        if henfald_random == 6:
            antal_kerner -= 1
        else:
            list.append(henfald_1, henfald_random)
            antal_kerner -= 1

    count += 1
    print(list.__len__(henfald_1))

    antal_kerner = list.__len__(henfald_1)

    list.clear(henfald_1)

print("Det har taget",count,"tidsenheder at henfalde")
quit()