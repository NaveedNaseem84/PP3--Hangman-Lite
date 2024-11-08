import random
import sys
import gspread
from google.oauth2.service_account import Credentials

"""
Code to configure, connect and retrieve data from google sheet
(below) taken from the CI love sandwiches project, Used
in choose random word function and below. Lines 12 to 22.
Referenced in "credits"section in readme.md
"""
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

MASK_CHAR = '_'

DECOR_LINE = "=" * 35

VALIDATION_ERROR = """Oops, that's not right.
You can only enter 1 alphabetical letter!
Try again below.\n"""

GAME_INFO = f"""{DECOR_LINE}
When you are ready, enter a letter.\n
Rules: type 'help'.
Quit the program: type 'quit'.\n"""

RESET_INFO = f"""{DECOR_LINE}
game reset in progress...\n
loading...\n
New game loaded.
{DECOR_LINE}
Welcome to Hangman Lite
{DECOR_LINE}"""


class Hangman():
    """
    Main Hangman class.
    """
    def __init__(self):
        print(DECOR_LINE)
        print("Welcome to Hangman Lite")
        print(DECOR_LINE)
        self.words_won = 0
        self.words_lost = 0
        self.difficulty_levels = {"1": 12, "2": 8, "3": 4}

    def display_instructions(self):
        """
        Instructions for the game read in from the
        instructions file and displayed.
        Code to import from file adapted from the
        CI love sandwiches project.Referenced in "credits"
        section in readme.md.
        """
        file = open("instructions.txt", 'r')
        print(file.read())
        file.close()

    def choose_random_word(self):
        """
        Read in words from google sheet externally,
        assigned to a string so it can be formatted to seperate
        word and hint from : in the play game function.

        Code to retrieve data from google sheet
        taken from the CI love sandwiches project, (line 82)
        Referenced in "credits" section in readme.md.
        """
        try:
            print("loading data, please wait ...\n")
            words = get_words.get_all_values()
            choose_random_word = random.choice(words)
            choose_word = choose_random_word[0]
            return choose_word
        except Exception as e:
            print("Unable to load data....")
            print("Please try again later...")
            sys.exit(0)

    def get_user_input(self):
        """
        Recieve and return player input as a lower letter.
        """
        user_input = input("Your choice: \n").lower()
        return user_input

    def input_validation(self, user_input):
        """
        Validate player input to only accept 1 letter.
        """
        if len(user_input) == 1 and user_input.isalpha():
            return True
        else:
            print(VALIDATION_ERROR)
            return False

    def mask_selected_word(self):
        """
        Replace all the letters in the selected word
        with _ ready to be guessed.
        """
        word_mask = []
        for letter in self.selected_word:
            letter = letter.replace(letter, MASK_CHAR)
            word_mask.append(letter)
        self.masked_word = word_mask

    def process_input_letter(self, user_input):
        """
        Loop the word and if:
         - the input matches the word, update with letter
         - let the player know what they have found
         - if no match, reduce an attempt.
         - let the player know how many attempts are left
         - record the letters that have been used and not
         in the word.
        """
        letter_count = 0
        print(DECOR_LINE)
        for letter in range(len(self.selected_word)):
            if self.selected_word[letter] == user_input:
                self.masked_word[letter] = user_input
                letter_count += 1
        if letter_count > 0:
            if letter_count > 1:
                print(f"You found {letter_count} '{user_input}'s!\n")
            else:
                print(f"Well done, you found '{user_input}'\n")
                print(f"incorrect guesses: {self.invalid_input}")
        else:
            self.attempts_left -= 1
            print(f"Try again,'{user_input}' isn't in the word.\n")
            print(f"attempts left: {self.attempts_left}")
            self.invalid_input.append(user_input)
            print(f"incorrect guesses: {self.invalid_input}\n")
        return self.attempts_left

    def game_over(self):
        """
        Notify player game is over and record the
        game loss and let them know the word.
        """
        self.words_lost += 1
        print(DECOR_LINE)
        print("       G A M E  O V E R        ")
        print("        Attempts left: 0")
        print(f"   The word was: {self.selected_word}")
        print(f"           Won: {self.words_won}")
        print(f"          Lost: {self.words_lost}")
        print(DECOR_LINE)

    def game_won(self):
        """
        Summary of when the word has been guessed and
        recording the game win.
        """
        self.words_won += 1
        print(DECOR_LINE)
        print("      W E L L  D O N E !")
        print(f"       Attempts left: {self.attempts_left}")
        print(f"  The word was: {self.selected_word}")
        print(f"          Won: {self.words_won}")
        print(f"         Lost: {self.words_lost}")
        print(DECOR_LINE)

    def reset_game(self):
        """
        Reset games won/lost variables. let the player know
        that the reset is in progress and finally call the
        play game function.
        """
        self.words_won = 0
        self.words_lost = 0
        print(RESET_INFO)
        self.play_hangman()

    def quit_game(self):
        """
        Quit/terminate the application.
        Code to exit below implemented by following the
        tutorial by Shittu Olumide on Free Code Camp.
        Referenced in "credits" section in readme.md.
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
        print("Choose your difficulty:")
        print("1 = easy 2 = medium 3 = hard\n")
        user_confirm = self.get_user_input()
        while True:
            if user_confirm not in self.difficulty_levels:
                print("Invalid, choose: 1 = easy 2 = medium 3 = hard\n")
                user_confirm = input("Your choice:\n").lower()
            else:
                self.attempts_left = self.difficulty_levels[user_confirm]
                break
        return self.attempts_left

    def play_again(self):
        """
        Ask the player if they want continue playing the current game.
        Provides the option to play again, reset or quit respectively.
        """
        print("Game complete.\n")
        print("Please choose:\ny = carry on playing \nr = reset \nq = quit\n")
        while True:
            user_confirm = self.get_user_input()
            if user_confirm == "y":
                print("loading next round...")
                print(DECOR_LINE)
                self.play_hangman()
            elif user_confirm == "r":
                self.reset_game()
                break
            elif user_confirm == "q":
                self.quit_game()
                break
            else:
                print("Invalid input.")
                print("Choose:\ny = carry on playing \nr = reset \nq = quit\n")

    def setup_game_info(self):
        """
        Quick instructions for the player, letting them know
        the total attempts they have and how to access other
        information/functionality.
        """
        print(GAME_INFO)
        print(f"Attempts: {self.attempts_left}\n")

    def game_status(self):
        """
        Status of the current game till the game is over or
        won. The number of letters in the word and the hint
        are shown.
        """
        print(f"letters: {len(self.selected_word)}")
        print(f"hint: {self.hint}\n")
        print(" ".join(self.masked_word)+"\n")

    def special_inputs(self, user_input):
        """
        Allows the option to view help or quit
        the game on demand.
        """
        if user_input == "help":
            self.display_instructions()
            return True
        elif user_input == "quit":
            self.quit_game()
            return True
        return False

    def game_setup(self):
        """
        Retrieve the difficulty, word, hint and masked word
        ready to be initialised in the play_hangman function
        below.
        """
        self.attempts_left = self.set_difficulty()
        self.selected_word, self.hint = self.choose_random_word().split(":")
        self.mask_selected_word()
        self.invalid_input = []
        self.duplicate_input = []
        self.setup_game_info()

    def play_hangman(self):
        """
        Retrieve the initials values from game setup. Whilst the
        game is not complete ( word not found or attempts used up)
        - check the input against the word and record the input
        - call process input which either updates the letter(s)
        or reduces an attempt and declares game won or game over
        respectively.
        If word guessed call the game won function
        If attempts up, call the game over function.
        Give the option to play again on game won or over.
        """
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
                if self.masked_word.count(MASK_CHAR) == 0:
                    self.game_won()
                    self.play_again()
                    break
        else:
            self.game_over()
            self.play_again()


if __name__ == "__main__":
    game = Hangman()
    game.play_hangman()
    
