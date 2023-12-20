import random as rand

class Hangman():
    """
    A class to represent a game.

    ...

    Attributes
    ----------
    word : str
        The word to be guessed, picked randomly from the word_list.
    word_guessed : list
        A list of the letters of the word, with _ for each letter not yet guessed. For example, if the word is 'apple',
        the word_guessed list would be ['_', '_', '_', '_', '_']. If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters : int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives : int
        The number of lives the player has at the start of the game.
    word_list : list 
        A list of words
    list_of_guesses : list
        A list of the guesses that have already been tried. Set this to an empty list initially


    Methods
    -------
    check_guess(guess):
        Checks if guessed letter is in the word and updates the word_guessed. If the guess is not in the word, subtracts number of lives.
    ask_for_input():
        Asks for user input and checks if it is a single letter or if it had already been used.
    """
    def __init__(self, word_list, num_lives=5):
        """
        Constructs all the necessary attributes for the game object.

        Parameters
        ----------
            word_list : list 
                A list of words
        """
        
        self.word = rand.choice(word_list)
        self.word_guessed = ["_" for i in self.word]
        self.num_letters = len(self.word_guessed)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        '''
    Checks if guessed letter is in the word and updates the word_guessed. If the guess is not in the word, subtracts number of lives.

            Parameters:
                    guess (str): A single letter
    '''
           
        guess_lower= guess.lower()
        if guess_lower in self.word:
            print("Good guess! {} is in the word.".format(guess_lower))
            for index, letter in enumerate(self.word):
                if letter == guess_lower:
                    self.word_guessed[index] = letter
                    self.num_letters-=1
                    

                  
        else:
            
            print("Sorry, {} is not in the word.".format(guess_lower))
            
            self.num_lives-=1
            print("You have {} lives left.".format(self.num_lives))
                 
        print(self.word_guessed)
            
def ask_for_input(self):
        '''
    Asks for user input and checks if it is a single letter or if it had already been used.

    '''

        while self.num_lives >0 and self.num_letters != 0:
            guess = input("Select a single letter: ")

            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
                
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
    
def play_game(word_list):
    '''
    Executes one round of the Hangman game until the user either wins the game or runs out of lives.

    '''
    num_lives = 5
    game = Hangman(word_list, num_lives)
    
   
    while True:
        if game.num_lives == 0:
            print("You lost! The word was {}".format(game.word))
            break
            
        elif game.num_letters > 0:
            game.ask_for_input()
           
            
        elif game.num_lives != 0 and game.num_letters == 0:
            print("Congratulations. You won the game! The word was {}".format(game.word))
            break
            

play_game(["apple", "mango", "strawberry", "watermelon", "lemon"])
