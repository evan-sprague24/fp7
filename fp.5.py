def redText(text):
    return f"\033[91m{text}\033[0m"

def blueText(text):
    return f"\033[94m{text}\033[0m"

def greenText(text):
    return f"\033[92m{text}\033[0m"

def yellowText(text):
    return f"\033[93m{text}\033[0m"

def brownText(text):
    return f"\033[33m{text}\033[0m"

def main():
    # Display example texts in different colors
    print(redText("This text is red."))
    print(blueText("This text is blue."))
    print(greenText("This text is green."))
    print(yellowText("This text is yellow."))
    print(brownText("This text is brown."))

    # User input prompt for color choice and text
    color_choice = input("Choose a color (red, blue, green, yellow, brown): ").strip().lower()
    user_text = input("Enter the text you want to display: ")

    # Color mapping
    color_functions = {
        "red": redText,
        "blue": blueText,
        "green": greenText,
        "yellow": yellowText,
        "brown": brownText
    }

    # Display text in the chosen color if valid
    if color_choice in color_functions:
        print(color_functions[color_choice](user_text))
    else:
        print("Invalid color choice.")

# Run the main function
main()