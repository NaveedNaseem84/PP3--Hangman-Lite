import random

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
    words = file.read()
    word_list = words.split("\n")
    file.close()
    choose_word = random.choice(word_list)
    print(f"Random word: {choose_word}")


#---pseudo skeleton for game---

#1. Function for random word
# - import the words from a external file like above?
# - randomly assign to a variable and return the value


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



#display_instructions()
choose_random_word()

