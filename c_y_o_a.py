name = input("Type your name: ")
print("WELCOME ",name," to this ADVENTURE!")

answer = input("You are on a dirt road, it come to an end and you can go lest or right. \n "
               "Which way would you like to go?: ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across?\n"
                   "What would you choice (swim/walk): ")
    if answer == "swim":
        print("You swim across and got eaten by an alligator")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and DIED.")
    else:
        print("Not valid option")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back? \ n"
                   "Type cross or back: ").lower()
    if answer == "back":
        print("You found magic lamp that transported you back home.")
    elif answer == "cross":
        print("You fin magical carpet laying on a floor and decided to fly it to Hawaii")
    else:
        print("Not valid option")
else:
    print("Not valid option")
