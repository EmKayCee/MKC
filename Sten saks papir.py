import random

user_wins = 0
computer_wins = 0

options = ["sten", "saks", "papir"]

while True:
    user_input = input("Skriv sten/saks/papir eller q for at afslutte: ").lower()
    if user_input == "q": #så man kan afslutte
        break

    if user_input not in options: #vi laver en liste for at tjekke flere muligheder på en gang
        continue

    random_number = random.randint(0,2)
    # 0 = sten, 1 = saks, 2 = papir
    computer_pick = options[random_number]
    print("Computeren valgte", computer_pick + ".")

    if user_input == "sten" and computer_pick == "saks": #med and skal begge være ens
        print("Du vandt!")
        user_wins += 1

    elif user_input == "papir" and computer_pick == "sten":
        print("Du vandt!")
        user_wins += 1

    elif user_input == "saks" and computer_pick == "papir":
        print("Du vandt!")
        user_wins += 1

    elif user_input == computer_pick: #hvis begge svarer det samme
        print("Ingen får point")

    else:
        print("Du tabte!")
        computer_wins += 1


print("Du vandt", user_wins, "gange")
print("Computeren vandt", computer_wins, "gange")
print("Farvel!")