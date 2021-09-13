import random

top_of_range = input("Skriv et nummer: ") #husk at input() altid giver str()

if top_of_range.isdigit():
    top_of_range = int(top_of_range) #vi tjekker om det er et tal

    if top_of_range <= 0: #tjekker om tallet er større end nul
        print("Skriv gerne et tal, der er større end 0 næste gang. ")
        quit()
else:
    print("Skriv gerne et tal næste gang. ")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True: #man kunne også skrive: "while user_guess != random_number:"
    guesses += 1 #hver gang loppet starter lægges der +1 til gæt
    user_guess = input("Kom med et gæt: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)  # vi tjekker om det er et tal (kopi af tidligere kode). Vi tjekker ikke om det er 0 mere
    else:
        print("Skriv gerne et tal næste gang. ")
        continue #bringer også tilbage til toppen af loopet

    if user_guess == random_number:
        print("Du gættede det!")
        break #stopper loopet
    elif user_guess > random_number: #tjek om det er over
        print("Du er over nummeret")
    else:
        print("Du er under nummerert")


print("Du fik det i", guesses, "forsøg")