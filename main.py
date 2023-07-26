import random
import os

# Stores the users native words as keys and non native as values
flashcards = {}


def display_flashcards(flashcards):
    print("\n======= FLASHCARD DISPLAY =======")
    for native, non_native in flashcards.items():
        print(f"Native Word: {native} | Non-Native: {non_native } ")
    print("===================================\n")


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


def create_flashcards():
    '''
    Function allows a user to create their own flashcards
    '''
    num_words = get_num_words()
    for _ in range(num_words):
        native_language = get_native_word()
        non_native_language = get_non_native_word()

        # Checks to see if the native language is already the key, and makes sure there is not duplicate words
        if native_language in flashcards:
            print("Word already in the selection")
        else:
            flashcards[native_language] = non_native_language

    print("Flashcards has successfully been created!!")


def generate_random_word():
    native_word = random.choice(list(flashcards.keys()))
    return native_word


def quiz_mode():
    print("\n ======== BEGINNING OF QUIZ ============ \n")
    input("If you are ready to enter the quiz please press Enter....")
    score = 0

    for i in range(len(flashcards)):
        os.system("cls")
        print(f"Question: {i + 1} out of {len(flashcards)}")
        word = generate_random_word()
        guess = input(
            f"What is the non-native word for {word}: (Or press q to quit)").lower()

        if not guess.lower() == "q":
            if guess.strip() == flashcards[word]:
                score = score + 1
        else:
            break

    print(
        f"You have finished the quiz, and have scored {score} out of {len(flashcards)}")


def main():
    while True:
        print("\n======== FLASHCARD PROGRAM ========\n")
        print("1.Create your Flashcards")
        print("2.Display your Flashcards")
        print("3.Quiz")
        print("5. Quit Program")

        user_choice = input("Please select an option: ")

        if user_choice == "5":
            break
        elif user_choice == "1":
            create_flashcards()
        elif user_choice == "2":
            display_flashcards(flashcards)
        elif user_choice == "3":
            quiz_mode()


main()


# Implements the quiz mode to allow users to be able to study, and practice. Keep score as well
