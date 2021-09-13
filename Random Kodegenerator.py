#Kodegenerator
import random

længde = input("Hvor sikker skal din kode være? (Vælg antal af karakterer, jo flere jo sikre): ")

x = 1
kode = []

alfabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","æ","ø","å",0,1,2,3,4,5,6,7,8,9,
           "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","Æ","Ø","Å"]

while x <= int(længde):
    list.append(kode,alfabet[random.randint(0,67)])
    x += 1

print(*kode,sep="")





