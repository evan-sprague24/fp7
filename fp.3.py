import random

def guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    while True:
        # Ask the user if they want to play
        play = input("Would you like to play? (yes/no): ").strip().lower()
        
        if play == "yes":
            # Generate a random number between 1 and 10
            number_to_guess = random.randint(1, 10)
            attempts = 0
            
            while True:
                try:
                    guess = int(input("Guess a number between 1 and 10: "))
                    attempts += 1
                    
                    if guess < 1 or guess > 10:
                        print("Please guess a number within the range 1-10.")
                    elif guess < number_to_guess:
                        print("Too low! Try again.")
                    elif guess > number_to_guess:
                        print("Too high! Try again.")
                    else:
                        print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                        break  # Exit the guessing loop
                except ValueError:
                    print("Please enter a valid integer.")
        
        elif play == "no":
            print("Goodbye! Thanks for playing.")
            break  # Exit the main loop
        
        else:
            print("Invalid input. Please answer with 'yes' or 'no'.")

# Run the guessing game function
guessing_game()