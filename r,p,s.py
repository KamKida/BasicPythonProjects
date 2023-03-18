import random

user_wins = 0
computer_wins = 0 

options = ["rock", "paper", "scissors"]


while True:
    user_input = input("TYPE :ROCK, PAPER ,SCISSORS\n"
                       "OR 'Q' TO QUIT\n"
                       "Impute:").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue
    
    random_number = random.randint(0,2)
    # rock :0, paper:1 , scissors:2
    computer_choice = options[random_number]
    print("Computer picked: ", computer_choice)

    if user_input == "rock " and computer_choice == "scissors":
        print("you win")
        user_wins += 1
        
    elif user_input == "paper " and computer_choice == "rock":
        print("you win")
        user_wins += 1
        
    elif user_input == "scissors " and computer_choice == "paper":
        print("you win")
        user_wins += 1
        

    else:
        print("Computer wins")
        computer_wins =+1
        continue

print("The user won: ",user_wins," and computer won: ",computer_wins," .")
print("Good bye")

    

