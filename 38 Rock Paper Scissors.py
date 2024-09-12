import random
while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("Rock, Paper, or Scissors?: ").lower()

    if player == computer:
        print("Computer: ",str(computer).capitalize())
        print("Player: ",str(player).capitalize())
        print("Tie!")

    elif player == "rock":
        print("Computer: ",str(computer).capitalize())
        print("Player: ",str(player).capitalize())
        if computer == "paper":
            print("You Lose!")
        elif computer == "scissors":
            print("You Win!")

    elif player == "paper":
        print("Computer: ",str(computer).capitalize())
        print("Player: ",str(player).capitalize())
        if computer == "rock":
            print("You Win!")
        elif computer == "scissors":
            print("You Lose!")

    elif player == "scissors":
        print("Computer: ",str(computer).capitalize())
        print("Player: ",str(player).capitalize())
        if computer == "rock":
            print("You Lose!")
        elif computer == "paper":
            print("You Win!")
    
    play_again = input("Play Again? (yes/no): ".lower())
    
    if play_again != "yes":
        break
print("Bye!")

   


