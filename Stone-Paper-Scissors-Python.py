import random

options = ("stone", "paper", "scissors")

def play_again():
    choice = input("Do you want to play again? (yes/no): ").lower()
    return choice == "yes"

def play_round():
    player = input("Choose stone, paper, or scissors: ").lower()

    if player not in options:
        print("Invalid choice!")
        return

    computer = random.choice(options)
    print(f"Computer chose: {computer}")

    if player == computer:
        print("It's a tie!")
    elif (
        (player == "stone" and computer == "scissors") or
        (player == "paper" and computer == "stone") or
        (player == "scissors" and computer == "paper")
    ):
        print("You win!")
    else:
        print("You lose!")

print("Welcome to Stone Paper Scissors!")

playing = True
while playing:
    play_round()
    playing = play_again()

print("Thanks for playing!")