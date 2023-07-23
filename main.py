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
            break

    return number_of_words


# Get the number of words to guess
num_of_words = get_num_words()
