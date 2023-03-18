print("welcome to my game!")

player = input("DO you wanna play my game (y/n): ")

if player.lower() != "y":
    quit()

print("ok lets play :)")

score = 0

answer = input("what does gpu stand for?: ").lower()

if answer == "central graphics processing unit":
    print('Correct!')
    score +=1
elif answer != "central processing unit":
    print("incorect! ")

answer = input("what does ram stand for?: ").lower()

if answer == "random access memory":
    print('Correct!')
    score +=1
elif answer != "central processing unit":
    print("incorect! try again")

answer = input("what does cpu stand for?: ").lower()

if answer == "central processing unit":
    print('Correct!')
    score +=1
elif answer != "central processing unit":
    print("incorect! try again")

answer = input("what does psu stand for?: ").lower()

if answer == "power supply":
    print('Correct!')
    score +=1
elif answer != "central processing unit":
    print("incorect! try again")


print("Caongrats you got: ",score," points!")