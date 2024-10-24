import random

def powerball_game():
    # Greeting the user
    print("Welcome to the Powerball Number Generator!")
    print("This program will generate six random numbers for you,")
    print("with the first five numbers being between 1 and 69, and the last number being between 1 and 26.\n")

    # Generating the first five numbers
    first_five_numbers = random.sample(range(1, 70), 5)
    # Generating the Powerball number
    powerball_number = random.randint(1, 26)

    # Sorting the first five numbers for better readability
    first_five_numbers.sort()

    # Formatting the output
    formatted_numbers = ' '.join(map(str, first_five_numbers)) + '   ' + str(powerball_number)

    # Displaying the generated numbers
    print("Your Powerball numbers are:")
    print(formatted_numbers)

    # Farewell message
    print("\nThank you for using the Powerball Number Generator! Good luck!")

# Run the Powerball game function
powerball_game()