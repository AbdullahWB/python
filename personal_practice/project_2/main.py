import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    
    # Initialize guess counter
    guesses = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it.")
    
    while True:
        try:
            # Take the player's guess
            guess = int(input("Enter your guess: "))
            guesses += 1  # Increment the guess counter
            
            # Check if the guess is correct
            if guess < number:
                print("Higher number please.")
            elif guess > number:
                print("Lower number please.")
            else:
                print(f"Congratulations! You've guessed the number {number} correctly.")
                print(f"It took you {guesses} guesses.")
                break  # Exit the loop when the correct guess is made
        except ValueError:
            print("Please enter a valid number.")
            
# Call the function to play the game
guess_the_number()
