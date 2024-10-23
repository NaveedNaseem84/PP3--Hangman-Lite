def display_instructions():
    """
    Instructions for the game read in from the
    instructions file and displayed
    """
    file = open("instructions.txt", 'r')
    instructions = file.read()
    print(instructions)
    file.close()

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



display_instructions()

