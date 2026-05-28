import random
options = ["Rock", "Sciccor", "Paper"]

user_choice = input("Choose rock, paper or scissor : ")
computer_choice = random.choice(options)

print("You chose : ",user_choice)
print("Computer chose : ",computer_choice)

if user_choice == computer_choice:
    print("It's tie")
elif user_choice == "Rock" and computer_choice == "Scissor":
    print("You win")
elif user_choice == "Scissor" and computer_choice == "Paper":
    print("You win")
elif user_choice == "Paper" and computer_choice == "Rock":
    print("You win")
else:
    print("You lose")