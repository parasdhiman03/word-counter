# word_counter.py

def count_words(text):
    """
    Function to count the number of words in the given text.
    The input is expected to be a non-empty string.
    """
    # Split the input string by whitespace and return the length of the resulting list
    words = text.split()
    return len(words)


def get_user_input():
    """
    Function to get valid input from the user.
    Ensures that the input is not empty.
    """
    while True:
        user_input = input("Enter a sentence or paragraph: ").strip()

        # Check if the input is empty
        if not user_input:
            print("Error: The input cannot be empty. Please try again.")
        else:
            return user_input


def main():
    """
    Main function to run the Word Counter program.
    Handles user input, word counting, and displaying the result.
    """
    print("Welcome to the Word Counter program!")

    # Get valid user input
    text = get_user_input()

    # Count the number of words in the input text
    word_count = count_words(text)

    # Display the word count to the user
    print(f"The number of words in your input is: {word_count}")


# Run the program
if __name__ == "__main__":
    main()
