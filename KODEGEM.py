pwd = input("Hvad er den hemmelige kode? ")
while pwd != "mmkc9551":
    print("Ikke det rigtige kodeord. Prøv igen!")
    continue



def tilføje(): #dette er funktioner, som man kan tilføje til koden. Man laver dem med at skrive def foran f.eks. et svar
    name = input("Kontonavn: ")
    kode = input("Kode: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + kode + "\n") #laver en ny linje

#når man bruge with skal man ikke manuelt lukke vinduer
#a er en mode at åbne filer.
#w er at den laver en ny eller overwriter allerede eksisterende
#r er readmode man læser den bare og kan ikke andet
#a man kan lave en ny fil og hvis den allerede eksiterer, kan man skrive i slutningen af filen

def se ():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            nav, kod = data.split("|") #vi sepererer navne og kode og skaber en liste
            print("Navn:", nav, ",", "Kode:", kod)


            print(line.rstrip()) #fjerne den ekstra linje der kommer, når man vælger se


while True:
    mode = input("Vil du gerne TILFØJE et nyt kodeord eller SE de eksisterende koder? Skriv q for at afslutte ").lower()
    if mode == "tilføje":
        tilføje()
    elif mode == "se":
        se()
    elif mode == "q":
        break
    else:
        print("Ikke en mulighed")
        continue