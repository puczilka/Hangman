import random as rand

class Hangman():

    def __init__(self, word_list, num_lives=5):
        
        self.word = rand.choice(word_list)
        self.word_guessed = []
        self.num_letters = 0
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []


    def check_guess(self, guess):
        guess_lower= guess.lower()
        if guess_lower in self.word:
            print("Good guess! {} is in the word.".format(guess_lower))
            for letter in word:
                if letter == guess:
                    letter = self.word_guessed[letter]
                else:
                    num_lives=-1
                    print("Sorry, {} is not in the word.".format(letter))
                    print("You have {} lives left.".format(num_lives))

            num_letters=-1

            
    
    




    def ask_for_input(self):

        while True:
            guess = input("Select a single letter: ")

            if len(guess) != 1 and guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
                
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

  
p = Hangman(["peach", "lol"])    
p.ask_for_input()
    
