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

def play_hangman():
    attempts_left = 5 # test value for while loop iteration
    selected_word = choose_random_word()
    print(f"Selected word: {selected_word}")

    while attempts_left > 0:
        user_input = get_user_input()
        if user_input == selected_word:
            print(f"Well done. You found: {user_input}")
            print(f"attempts left: {attempts_left}")
            break
        else:
            attempts_left -= 1
            print ("Try again!")
            print(f"attempts left: {attempts_left}")
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


