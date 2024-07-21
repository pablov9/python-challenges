
import random

computerChoice=random.choice(["rock", "paper", "scissors"])
userChoice=input("Do you want rock, paper or scissors?\n")

print("Computer choice:", computerChoice)

if computerChoice==userChoice:
    print("TIE")
elif userChoice=="rock" and computerChoice=="scissors":
    print("You win!")
elif userChoice=="paper" and computerChoice=="scissors":
    print("You win!")
elif userChoice=="scissors" and computerChoice=="paper":
    print("You win!")
else:
    print("You lose, computer wins")

