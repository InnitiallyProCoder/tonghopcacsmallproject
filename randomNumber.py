import random

max_number = 100
min_number = 1
guesses = 0
answer = random.randint(min_number, max_number)
is_running = True

while is_running:
    guess = input ("Guess a number: ")
    if guess.isdigit():
        guess = int (guess)
        guesses += 1
        if guess == answer:
            print (f"CONGRATULATION!! The answer is: {answer}")
            print (f"You guessed {guesses} times")
            break
        else:
            if guess < answer:
                print ("Your number is too low")
                print ("Try again")
            elif guess > answer:
                print ("Your number is too high")
                print ("Try again")

    elif guess < min_number or guess > max_number:
        print ("Invalid number, please enter a digit between {min_number} and {max_number}")

    else:
        print ("Number invalid!!")
        print (f'Please enter a digit between {min_number} and {max_number}')


