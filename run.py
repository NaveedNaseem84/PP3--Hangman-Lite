import random
import sys

class Hangman:
    """
    Main Hangman class
    """
    def __init__(self):
        print("========================")
        print("Welcome to Hangman Lite")
        print("========================\n")
        self.words_won = 0
        self.words_lost = 0
        

# code to import from file adapted from the CI love sandwiches project
# and will be referenced accordingly in readme.md
# used in display_instructions and choose_random_word functions below

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
        Read in words from words file and assign to list
        using the new line as the value seperator. Randomly
        select and return a word from this list.
        """
        #source for words: 
        # https://www.thegamegal.com/wp-content/uploads/2011/11/Pictionary-Words-Medium.pdf
    
        file = open("words.txt", 'r')
        words = file.read().lower()
        word_list = words.split("\n")
        file.close()
        choose_word = random.choice(word_list)
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
        #to do: add in check for more than one character!
    
        if len(user_input) == 0:
            print("You need to enter something!")
            return False
        elif not user_input.isalpha():
            print("Invalid: a - z characters only allowed")
            return False
        return True

    def mask_selected_word(self, selected_word):
        """
        replace all the letters in the selected word
        with _ ready to be guessed.
        """
        word_mask = []
        for letter in selected_word:
            letter = letter.replace(letter, '_')
            word_mask.append(letter)
        return word_mask
        

    def letter_found(self, user_input, selected_word, masked_word, invalid_input):
        """
        loop the update the masked word with the correct one if the 
        input is matched at that point. notify user that one/more letters
        was found
        """
        letter_count = 0
        for letter in range(len(selected_word)):
            if selected_word[letter] == user_input:
                masked_word[letter] = user_input
                letter_count+=1
        if letter_count > 1:
            print("===============================")
            print(f"Nice, you found {letter_count} '{user_input}'s in the word!\n")
        else:
            print("===============================")
            print(f"Well done, you found '{user_input}'\n")
            print(f"incorrect guesses: {invalid_input}")
                                           
    def letter_not_found(self, user_input, attempts_left, invalid_input):
        """
        If the input doesn't match the masked word, deduct an attempt.
        Also make a note of the letters tried to let the user know.
        """
        attempts_left -= 1
        print("===============================")
        print (f"Try again,'{user_input}' isn't in the word.\n")
        print(f"attempts left: {attempts_left}")
        invalid_input.append(user_input)
        print(f"incorrect guesses: {invalid_input}\n")
        return attempts_left


    def game_over(self, selected_word):
        """
        notify user game is over and record the 
        game loss
        """        
        self.words_lost += 1
        print("===============================")
        print("       G A M E  O V E R        ")
        print("        Attempts left: 0")
        print(f"   The word was: {selected_word}")
        print(f"           Won: {self.words_won}")
        print(f"          Lost: {self.words_lost}")     
        print("===============================\n")
    

    def game_won(self, selected_word, attempts_left):
        """
        Summary of when the word has been guessed and
        record the game win
        """        
        self.words_won +=1
        print("===============================")
        print("      W E L L  D O N E !")
        print(f"       Attempts left: {attempts_left}")
        print(f"  The word was: {selected_word}")
        print(f"          Won: {self.words_won}")
        print(f"         Lost: {self.words_lost}")
        print("==============================\n")
   

    def reset_game(self):
        """
        Reset games won/lost and call the play game function
        """    
        self.words_won = 0
        self.words_lost = 0
        print("game reset in progress...\n")
        print("loading...\n")
        print("New game loaded\n")
        print("========================")
        print("Welcome to Hangman Lite")
        print("========================")
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
                user_confirm = input("Your choice:").lower()
            else:
                attempts_left = difficulty_levels[user_confirm]
                break           
        return attempts_left
    
    def play_again(self):
        """
        Ask the user if they continue playing the current game.
        If yes, carry on otherwise
        """
        # reset place holder for now. Come back to this.
        print("Game complete.\n")
        print("Please choose:\ny = carry on playing \nr = reset \nq = quit\n")               
        while True:
            user_confirm = self.get_user_input()
            if user_confirm =="y":
                print("loading next round...")
                print("========================\n")
                self.play_hangman()
            elif user_confirm =="r":
                self.reset_game()
                break
            elif user_confirm =="q":
                self.quit_game()
                break
            else:
                print("Invalid, please choose:\ny = carry on playing \nr = reset \nq = quit\n") 

    def play_hangman(self):
        
        attempts_left = self.set_difficulty()
        selected_word, hint = self.choose_random_word().split(":")
        masked_word = self.mask_selected_word(selected_word)
        invalid_input = []
        duplicate_input = []        
        print("========================\n")
        print("When you are ready, enter a letter.\n")
        print("Rules can be seen by typing 'help'.\n")
        print(f"Word: {selected_word}\n")
        print(f"Attempts: {attempts_left}\n")

        while attempts_left > 0:
            print(f"letters: {len(selected_word)}")
            print(f"hint: {hint}")
            print(" ".join(masked_word)+"\n")
            user_input = self.get_user_input()
            if user_input =="help":
                self.display_instructions()
                continue
            elif self.input_validation(user_input):
                if user_input in duplicate_input:
                    print(f"'{user_input}' has already been tried")
                    continue
                duplicate_input.append(user_input)
                if user_input in selected_word:
                    self.letter_found(user_input, selected_word, masked_word, invalid_input)
                    if masked_word.count('_') == 0:
                        self.game_won(selected_word, attempts_left)                 
                        self.play_again()
                        break
                else:
                    attempts_left = self.letter_not_found(user_input, attempts_left, invalid_input)
        self.game_over(selected_word)
        self.play_again()

game = Hangman()
game.play_hangman()
