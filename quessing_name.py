from random import randint as ri
from time import sleep




print("Wanna play a game?")

choice = input("CHOICE (y/n): ")

if choice != "y":
    quit()

while True:
    print("Choice a number to which you wanna guess: ")
    number = int(input("NUMBER: "))

    if number <= 0:
        print("Pleas choice a number higher then 0")
    else:
        break

random_n = ri(0, number+1)

tr = 1

print(random_n)

while True:
    tr += 1
    guess_u = int(input("Give me your best shot: "))
    if guess_u == random_n:
        print("Great you guest right in: ",tr," shots!")
        sleep(10)
        quit()
        
    elif guess_u < random_n:
        print("TRY HIGHER\n"
            "Its your: ",tr," SHOT!")
        
    elif guess_u > random_n:
        print("Try lower\n"
              "Its your: ",tr," SHOT!!")
        
    

