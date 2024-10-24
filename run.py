import random

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
    user_input = input("Enter choice: \n").lower()   
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


def play_hangman():
    attempts_left = 5 # test value for while loop iteration
    selected_word = choose_random_word()
    duplicate_input = []
    invalid_input = []
    print(f"Selected word: {selected_word}") #check original word correct against masked word   
    masked_word = mask_selected_word(selected_word)    

    while attempts_left > 0:
        print(f"masked word: {masked_word}")
        user_input = get_user_input()

        if input_validation(user_input):
            if user_input in duplicate_input:
                print(f"'{user_input}' has already been tried")                               
                continue            
            duplicate_input.append(user_input)

            if user_input in selected_word:
                for letter in range(len(selected_word)):
                    if selected_word[letter] == user_input:
                        masked_word[letter] = user_input                      
                if masked_word.count('_') == 0:
                    print("Game won, word found")                                  
                    break                                                
            else:
                attempts_left -= 1
                print ("Try again!")
                print(f"attempts left: {attempts_left}")           
                invalid_input.append(user_input)
                print(f"incorrect guesses: {invalid_input}")
           
    if attempts_left == 0:
            print("Game Over!")
        

   

#---pseudo skeleton for game---

#2. function to take input from user
# - validate so it is only a single letter 

#3. play game function
# - take the input from the user
# - compare this to the selected word which has the characters replaced as _ or * till guessed
# - if the input matches a letter in the word, replace that */_ with input
# - if input doesn't match, reduce an attempt and let the user know the input isn't in the word
# - If a repeat input is tried, store this to check and let user know this has already been tried.
# - If all attempts used up, game over
# - if word guessed, game won.
# - run on loop till either word guessed or attempts over

#4. option to play again on game won or game over.

#5. option to set difficulty

play_hangman()
#display_instructions()


