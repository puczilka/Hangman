from milestone_2 import word, word_list

def ask_for_input():
    while True:
        guess = input("Select a single letter: ")
        if len(guess) ==1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)


def check_guess(letter):
    letter=letter.lower()
    if letter in word:
        print("Good guess! {} is in the word.".format(letter))
    else:
        print("Sorry, {} is not in the word. Try again.".format(letter))


ask_for_input()    


