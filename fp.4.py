def trivia_quiz():
    # Define a dictionary with trivia questions and answers
    questions = {
        "What is the capital of France?": "Paris",
        "Who wrote 'Hamlet'?": "Shakespeare",
        "What is the largest planet in our solar system?": "Jupiter",
        "What year did the Titanic sink?": "1912",
        "What is the chemical symbol for water?": "H2O"
    }

    # Loop through each question in the dictionary
    for question, answer in questions.items():
        print(question)  # Display the question
        user_answer = input("Your answer: ").strip()  # Prompt for user input

        # Check if the user's answer matches the correct answer
        if user_answer.lower() == answer.lower():
            print("Correct! Well done.\n")
        else:
            print(f"Incorrect. The correct answer is: {answer}\n")

# Run the trivia quiz function
trivia_quiz()