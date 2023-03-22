import random

secret_number = random.randint(1, 100)

while True:
    guess = int(input("Guess the number between 1 and 100: "))
    
    if guess == secret_number:
        print("Congratulations. You guessed right")
        break
    elif guess < secret_number:
        print("Guess too low")
    else:
        print("Guess too high")