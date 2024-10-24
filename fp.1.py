def mad_libs():
    # Get user input for the Mad Libs
    adjective = input("Enter an adjective: ")
    large_objects_plural = input("Enter a plural noun (large objects): ")
    body_part = input("Enter a body part: ")
    restaurant = input("Enter a restaurant name: ")
    first_food = input("Enter a type of food: ")
    second_food = input("Enter another type of food: ")
    large_object_singular = input("Enter a singular noun (large object): ")

    # Construct the story
    story = f"I've had a very {adjective} day.\n" \
            f"This morning, I dropped a box of {large_objects_plural} on my {body_part}.\n" \
            f"Then, at lunch, I went to {restaurant} for their delicious {first_food},\n" \
            f"But the waiter brought me {second_food}, which I was not hungry for.\n" \
            f"Finally, on my way home, I was cut off by a van with a large {large_object_singular} strapped to the roof."

    # Print the story
    print("\nHere's your Mad Libs story:")
    print(story)

# Run the mad libs function
mad_libs()