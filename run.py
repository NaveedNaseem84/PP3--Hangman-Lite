import random

words_won = 0
words_lost = 0

# code to import from file adapted from the CI love sandwiches project
# and will be referenced accordingly in readme.md
# used in display_instructions and choose_random_word functions below

def display_instructions():
    """
    Instructions for the game read in from the
    instructions file and displayed
    """
    file = open("instructions.txt", 'r')
    instructions = file.read()
    print(instructions)
    file.close()

def choose_random_word():
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

def get_user_input():
    """
    Recieve and return user input
    """
    user_input = input("Your choice: \n").lower()   
    return user_input

def input_validation(user_input):
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

def mask_selected_word(selected_word):
    """
    replace all the letters in the selected word
    with _ ready to be guessed.
    """
    word_mask = []
    for letter in selected_word:
        letter = letter.replace(letter, '_')   
        word_mask.append(letter)   
    return word_mask

def letter_found(user_input, selected_word, masked_word, invalid_input):
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
        print(f"Nice, you found {letter_count} '{user_input}'s in the word!\n")
    else:
        print(f"Well done, you found '{user_input}'\n")            
    print(f"incorrect guesses: {invalid_input}") 
                                           
def letter_not_found(user_input, attempts_left, invalid_input):
    """
    If the input doesn't match the masked word, deduct an attempt.
    Also make a note of the letters tried to let the user know.
    """
    attempts_left -= 1
    print ("Try again!")
    print(f"attempts left: {attempts_left}")
    invalid_input.append(user_input)
    print(f"incorrect guesses: {invalid_input}")      
    return attempts_left


def game_over(selected_word, words_won, words_lost):
    """
    notify user game is over
    """    
    print("===============================")
    print("       G A M E  O V E R        ")
    print("        Attempts left: 0")
    print(f"   The word was: {selected_word}")
    print(f"           Won: {words_won} ")
    print(f"          Lost: {words_lost} ")     
    print("===============================\n")
    

def game_won(selected_word, attempts_left, words_won, words_lost):
    """
    Summary of when the word has been guessed
    """
    
    print("===============================")
    print("      W E L L  D O N E !")
    print(f"       Attempts left: {attempts_left}")
    print(f"  The word was: {selected_word}")
    print(f"          Won: {words_won} ")
    print(f"         Lost: {words_lost} ")
    print("==============================\n")
   

def reset_game():
    global words_won
    global words_lost
    words_won =0
    words_lost = 0
    print("\n"*10)
    print("game reset in progress...")    
    print("loading...")    
    print("New game loaded")
    print("========================")
    play_hangman()

def set_difficulty():
    """
    Take input 1, 2, 3 and set the difficulty which 
    sets the number of attempts for the game:

    1 = easy ( 12 attempts)
    2 = medium (8 attempts)
    3 = hard (4 attempts)
    """
    print("Choose your difficulty:")
    print("1 = easy")
    print("2 = medium") 
    print("3 = hard\n")
    user_confirm = get_user_input() 
    
    while True:           
        if user_confirm =="1":
            attempts_left = 12
            break        
        elif user_confirm =="2":
            attempts_left = 8
            break
        elif user_confirm =="3":
            attempts_left = 4   
            break              
        else:
            print("Invalid, choose:")
            print("1 = easy")
            print("2 = medium") 
            print("3 = hard\n")
            user_confirm = input("Your choice:").lower()
            
            continue
    return attempts_left 
    
def play_again():
    """
    Ask the user if they continue playing the current game.
    If yes, carry on otherwise
    """
    # reset place holder for now. Come back to this.
    
    print("Carry on playing? y = yes n = no\n")
    user_confirm = get_user_input() 
    
    while True:           
        if user_confirm =="y":
            print("loading...")
            print("========================")
            print("\n"*10)
            play_hangman()
        elif user_confirm =="n":
           
            reset_game()
            break     
        else:
             user_confirm = input("Invalid, Carry on playing? y = yes, n = no \n").lower()
             continue

def play_hangman():
    attempts_left = set_difficulty() # test value for while loop iteration
    selected_word, hint = choose_random_word().split(":")    
    masked_word = mask_selected_word(selected_word) 
    duplicate_input = []
    invalid_input = []
    global words_won
    global words_lost
    
    print("========================")
   # print("Welcome to Hangman Lite")
    #print("========================\n")
    print("When you are ready, enter a letter.\n")
    print("Rules can be seen by typing 'help'.\n")
    print(f"Word: {selected_word}\n")
    print(f"Attempts: {attempts_left}")

    while attempts_left > 0:
        print(f"letters: {len(selected_word)}")
        print(f"hint: {hint}")
        
        print(" ".join(masked_word)+"\n")
        user_input = get_user_input()

        if user_input =="help":
            display_instructions()
            continue
        elif input_validation(user_input):
            if user_input in duplicate_input:
                print(f"'{user_input}' has already been tried")                               
                continue            
            duplicate_input.append(user_input)
            if user_input in selected_word:
                letter_found(user_input, selected_word, masked_word, invalid_input)
                if masked_word.count('_') == 0:
                    words_won +=1                                       
                    game_won(selected_word, attempts_left, words_won, words_lost)                                                             
                    play_again()
                    break
            else:
               attempts_left = letter_not_found(user_input, attempts_left, invalid_input)                 
    if attempts_left == 0:  
        words_lost += 1              
        game_over(selected_word, words_won, words_lost)
        play_again()

#---pseudo skeleton for game---

#2. function to take input from user
# - validate so it is only a single letter 

#3. play game function
# - take the input from the user
# - compare this to the selected word which has the characters replaced as _ or * till guessed - done
# - if the input matches a letter in the word, replace that */_ with input - done. (decide if _ works better or *)
# - if input doesn't match, reduce an attempt and let the user know the input isn't in the word - done
# - If a repeat input is tried, store this to check and let user know this has already been tried.- done
# - If all attempts used up, game over - done
# - if word guessed, game won.- done
# - run on loop till either word guessed or attempts over - done

#4. option to play again on game won or game over.

#5. option to set difficulty
print("========================")
print("Welcome to Hangman Lite")
print("========================\n")
play_hangman()
#display_instructions()


