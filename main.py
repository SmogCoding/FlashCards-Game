# Stores the users native words as keys and non native as values
flashcards = {}


def get_num_words():
    '''
    Function asks the user to enter how many words they want to guess
    '''
    while True:
        number_of_words = input("How many words do you want to guess? \n")

        if not number_of_words.isdigit():
            print("Please enter a valid number")
        else:
            number_of_words = int(number_of_words)
            break

    return number_of_words


def get_native_word():
    while True:
        native_word = input(
            "Please enter the native word for the flashcard: \n").lower()

        if native_word.strip():
            return native_word
        else:
            print("Please enter a valid word")


def get_non_native_word():
    while True:
        non_native_word = input(
            "Please enter the non-native language word: \n").lower()

        if non_native_word.strip():
            return non_native_word
        else:
            print("Please enter a valid word")


def get_flashcards_words(num_words):
    '''
    Function gets the native and non-native languages from the user to be stored in the
    flashcard data structure.
    '''
    for _ in range(num_words):
        native_language = get_native_word()
        non_native_language = get_non_native_word()

        # Checks to see if the native language is already the key, and makes sure there is not duplicate words
        if native_language in flashcards:
            print("Word already in the selection")
        else:
            flashcards[native_language] = non_native_language


def main():
    # Get the number of words to guess
    num_of_words = get_num_words()
    get_flashcards_words(num_of_words)
    print("Flashcards Successfully Created")


main()


# Implements the quiz mode to allow users to be able to study, and practice. Keep score as well
