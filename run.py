import random
import sys
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hagman_lite_words')

get_words = SHEET.worksheet('words')

#code to configure, connect and retrieve data from google sheet
# taken from the CI love sandwiches project
# and will be referenced accordingly in readme.md

class Hangman():
    """
    Main Hangman class
    """
    def __init__(self):
        print("="*32)
        print("Welcome to Hangman Lite")
        print("="*32)
        self.words_won = 0
        self.words_lost = 0
        

# code to import from file adapted from the CI love sandwiches project
# and will be referenced accordingly in readme.md
# used in display_instructions

    def display_instructions(self):
        """
        Instructions for the game read in from the
        instructions file and displayed
        """
        file = open("instructions.txt", 'r')
        instructions = file.read()
        print(instructions)
        file.close()

    def choose_random_word(self):
        """
        Read in words from google sheet externally, 
        assigned to a string so it can be formatted to seperate
        word and hint from : in the play game function
        """       
        
        try:
            print("loading data, please wait ...\n")
            words = get_words.get_all_values()           
            choose_random_word = random.choice(words)        
            choose_word = choose_random_word[0]
        except:
            print("Unable to load data...")    
        return choose_word

    def get_user_input(self):
        """
        Recieve and return user input
        """
        user_input = input("Your choice: \n").lower()
        return user_input

    def input_validation(self, user_input):
        """
        Validate user input to not allow 
        empty or non characters.
        """
        if len(user_input) == 1 and user_input.isalpha():
            return True
        else:
            print("Oops, that's not right.")
            print("You can only enter 1 alphabetical letter!")
            print("Try again below.\n")
            return False

    def mask_selected_word(self):
        """
        replace all the letters in the selected word
        with _ ready to be guessed.
        """
        word_mask = []
        for letter in self.selected_word:
            letter = letter.replace(letter, '_')
            word_mask.append(letter)
        self.masked_word = word_mask
        
    '''
    def letter_found(self, user_input):
        """
        loop the update the masked word with the correct one if the 
        input is matched at that point. notify user that one/more letters
        was found
        """
        letter_count = 0
        for letter in range(len(self.selected_word)):
            if self.selected_word[letter] == user_input:
                self.masked_word[letter] = user_input
                letter_count+=1
        if letter_count > 1:
            print("="*32)
            print(f"You found {letter_count} '{user_input}'s in the word!\n")
        else:
            print("="*32)
            print(f"Well done, you found '{user_input}'\n")
            print(f"incorrect guesses: {self.invalid_input}")
                                           
    def letter_not_found(self, user_input):
        """
        If the input doesn't match the masked word, deduct an attempt.
        Also make a note of the letters tried to let the user know.
        """
        self.attempts_left -= 1
        print("="*32)
        print (f"Try again,'{user_input}' isn't in the word.\n")
        print(f"attempts left: {self.attempts_left}")
        self.invalid_input.append(user_input)
        print(f"incorrect guesses: {self.invalid_input}\n")
        return self.attempts_left
    '''
    def process_input_letter(self, user_input):
        letter_count = 0
        print("="*32)
        for letter in range(len(self.selected_word)):
            if self.selected_word[letter] == user_input:
                self.masked_word[letter] = user_input
                letter_count+=1                                    
        if letter_count > 0:
            if letter_count > 1:               
                print(f"You found {letter_count} '{user_input}'s in the word!\n")
            else:                
                print(f"Well done, you found '{user_input}'\n")
                print(f"incorrect guesses: {self.invalid_input}")
        else:
            self.attempts_left -= 1            
            print (f"Try again,'{user_input}' isn't in the word.\n")
            print(f"attempts left: {self.attempts_left}")
            self.invalid_input.append(user_input)
            print(f"incorrect guesses: {self.invalid_input}\n")     
        return self.attempts_left


    def game_over(self):
        """
        notify user game is over and recording the 
        game loss and letting them know the word
        """        
        self.words_lost += 1
        print("="*32)
        print("       G A M E  O V E R        ")
        print("        Attempts left: 0")
        print(f"   The word was: {self.selected_word}")
        print(f"           Won: {self.words_won}")
        print(f"          Lost: {self.words_lost}")     
        print("="*32)
    

    def game_won(self):
        """
        Summary of when the word has been guessed and
        recording the game win
        """        
        self.words_won +=1
        print("="*32)
        print("      W E L L  D O N E !")
        print(f"       Attempts left: {self.attempts_left}")
        print(f"  The word was: {self.selected_word}")
        print(f"          Won: {self.words_won}")
        print(f"         Lost: {self.words_lost}")
        print("="*32)
   

    def reset_game(self):
        """
        Reset games won/lost variables. let the user know
        that the reset is in progress and finally call the 
        play game function
        """    
        self.words_won = 0
        self.words_lost = 0
        print("game reset in progress...\n")
        print("loading...\n")
        print("New game loaded\n")
        print("="*32)
        print("Welcome to Hangman Lite")
        print("="*32)        
        self.play_hangman()

    def quit_game(self):
        """
        quit/terminate the application
        """
        print("Exiting program...\n")
        sys.exit(0)

    def set_difficulty(self):
        """
        Take input 1, 2, 3 and set the difficulty which 
        sets the number of attempts for the game:
        1 = easy ( 12 attempts)
        2 = medium (8 attempts)
        3 = hard (4 attempts)
        """
        difficulty_levels = {"1": 12, "2": 8, "3": 4}
        print("Choose your difficulty:")
        print("1 = easy 2 = medium 3 = hard\n") 
        user_confirm = self.get_user_input()
        while True:
            if user_confirm not in difficulty_levels:
                print("Invalid, choose: 1 = easy 2 = medium 3 = hard\n")      
                user_confirm = input("Your choice:\n").lower()
            else:
                self.attempts_left = difficulty_levels[user_confirm]
                break           
        return self.attempts_left
    
    def play_again(self):
        """
        Ask the user if they want continue playing the current game.
        Provides the option to play again, reset or quit respectively
        """
        # reset place holder for now. Come back to this.
        print("Game complete.\n")
        print("Please choose:\ny = carry on playing \nr = reset \nq = quit\n")               
        while True:
            user_confirm = self.get_user_input()
            if user_confirm =="y":
                print("loading next round...")
                print("="*32)                
                self.play_hangman()
            elif user_confirm =="r":
                self.reset_game()
                break
            elif user_confirm =="q":
                self.quit_game()
                break
            else:
                print("Invalid input.")
                print("Choose:\ny = carry on playing \nr = reset \nq = quit\n") 
        

    def setup_game_info(self):
        """
        Quick instructions for the user, letting them know
        the total attempts they have and how to access other 
        information/functionality
        """
        print("="*32)
        print("When you are ready, enter a letter.\n")
        print("Rules: type 'help'.")
        print("Quit the program: type 'quit'.\n")
        #print(f"Word: {selected_word}\n")
        print(f"Attempts: {self.attempts_left}\n")


    def game_status(self):
        """
        Status of the current game till the game is over or
        won
        """
        print(f"letters: {len(self.selected_word)}")
        print(f"hint: {self.hint}\n")
        print(" ".join(self.masked_word)+"\n")

    def special_inputs(self, user_input):
        """ 
        Allows the option to view help or quit 
        the game on demand
        """
        if user_input =="help":
            self.display_instructions()
            return True
        elif user_input =="quit":
            self.quit_game()
            return True
        return False

    def game_setup(self):
        """
        retrieve the difficulty, word, hint and masked word
        ready to be initialised in the play_hangman function
        below
        """
        self.attempts_left = self.set_difficulty()
        self.selected_word, self.hint = self.choose_random_word().split(":")
        self.mask_selected_word()
        self.invalid_input = []
        self.duplicate_input = []   
        self.setup_game_info()


    def play_hangman(self):
        
        self.game_setup()    
        while self.attempts_left > 0:
            self.game_status()            
            user_input = self.get_user_input()
            if self.special_inputs(user_input):
                continue
            elif self.input_validation(user_input):
                if user_input in self.duplicate_input:
                    print(f"'{user_input}' has already been tried\n")
                    continue
                self.duplicate_input.append(user_input)
                self.process_input_letter(user_input)
                #if user_input in self.selected_word:
                    #self.letter_found(user_input)
                if self.masked_word.count('_') == 0:
                    self.game_won()                 
                    self.play_again()
                    break
                #else:
                    #self.attempts_left = self.letter_not_found(user_input)
        else:
            self.game_over()
            self.play_again()

game = Hangman()
game.play_hangman()
