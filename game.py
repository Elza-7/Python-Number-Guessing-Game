
import random
play_again = "yes"
while play_again == "yes":
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    guess = 0
    print("==============================")
    print("WELCOME TO THE GUESSING GAME")
    print("==============================")
    while attempts < max_attempts:
        guess = int(input("Guess a number (1-100): "))
        attempts += 1
        if guess == secret_number:
            print("Correct! You won!")
            print("Total attempts:", attempts)
            break
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Too low!")
    if attempts == max_attempts and guess != secret_number:
        print("Game Over!")
        print("The secret number was:", secret_number)
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
print("Thanks for playing! Goodbye!")
