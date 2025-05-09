import random
options = ("rock", "paper", "scissors")
running = True

while running:
    bot_guess = random.choice (options)
    player = None

    while player not in options:
        player = input("Rock, paper, scissors? ").lower()

    print(f"Your guess: {player}")
    print(f"Bot guess: {bot_guess}")

    if player == "rock" and bot_guess == "scissors":
        print ("YOU WIN!!")
    elif player == "paper" and bot_guess == "rock":
        print ("YOU WIN!!")
    elif player == "scissors" and bot_guess == "paper":
        print ("YOU WIN!!")
    elif player == bot_guess:
        print ("TIE!!!")
    else: print ("YOU LOSE!!")

    if not input("Play again? (y/n): ").lower() == "y":
        running == False



