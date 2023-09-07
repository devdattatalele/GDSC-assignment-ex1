import random
choices = ["rock", "paper", "scissors"]

while True:
    inputchoice = input("Enter your choice (rock, paper, scissors): ")
    print(f"You chose: {inputchoice}")
    randomchoice = random.choice(choices)
    print(f"Computer chose: {randomchoice}")

    if inputchoice not in choices:
        print("Invalid choice.")
        continue
    if inputchoice == randomchoice:
        print("It's a tie!")
    elif (
        (inputchoice == "rock" and randomchoice == "scissors")
        or (inputchoice == "paper" and randomchoice == "rock")
        or (inputchoice == "scissors" and randomchoice == "paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")
