from random import choice
from math import inf




# 
def random_select_word(minl: int, maxl: int) -> str:
    with open("words.txt", "rt") as infile:
        words = [w for w in infile if minl <= len(w) <= maxl]
        return choice(words)
"""
# open the file to get its contents
def read_words():
    with open("words.txt", "rt") as infile:
        # Create an empty list to hold the lines of the file
        listx = []
        # loop through the lines of the file
        for words in infile:
            # add the line to the output list
            listx.append(words) 

        # return the output list
        return listx

def filter_by_lengths(wordlist: list, minlen: int, maxlen: int) -> list:
   #Return a new list created from the elements of wordlist
        whose length is no less than minlen and no greater than maxlen.
    
    # Create a list to store the elements we want to keep from wordlist
    listy = []
    # Loop through the input list
    for words in wordlist:
            if minlen <= len(words) <= maxlen:
                listy.append(words) 

    return listy 
 """   

def get_desired_difficulty() -> str:
    """ Prompt the user to enter 'easy',
        'medium', or 'hard'. If the user
        enters any other value, let them know
        this is not a valid option, and prompt
        them to guess again. Once the user
        has entered a valid option, return
        the user input. (while and input loop)
    ."""
    while True:
        msg = input("Enter: easy, normal, hard")
        msg = msg.lower()
        
        if msg not in ("easy", "normal", "hard"):
            print("please choose anactual game difficulty available")
        else:
            return msg
 

def get_user_guess():
    guess = input("Guess a letter ")
    # this print statement is not necessary but you could use it to help confirm what's happening
    print(f"You guessed {guess}")
    return guess  # when this function is called, we want to get back what the user guessed


def show_blanks_or_letters(word):
    # we will have to alter this:
    # if the letter has been guessed, we should show letters instead of blanks
    output = ''
    for letter in word:
        output += (" _ ")
    print(output)



def play_game():
    #pick difficulty
    difficulty = get_desired_difficulty()

    #  'easy' => minlen = 4, maxlen = 6
    if difficulty == "easy":
        minlen = 4
        maxlen = 6

    elif difficulty == "normal":
        minlen = 6
        maxlen = 8
    
    # assert: the value of difficulty is "hard"
    else: 
        minlen = 8
        maxlen = inf

    word = random_select_word(minlen, maxlen)    
    
    # show the user blanks for each letter in the word
    show_blanks_or_letters(word)
    # have some way for the user to make a guess
    # let's put it in a function!
    guess = get_user_guess()

    # record the guesses
    # possible implementation: set up a list to store the user guess in
    # where and when do we need access to this? Consider where you might store this information and how you will access it and change it
    guesses = []
    guesses.append(guess)  # add the guess to the list

    # record the number of tries (wrong guesses) -> maybe do this later

    # compare the guess to the letters in the word.
    # this is definitely a tricky part. Can you think of how you could do this?
    # is the user's guess one of the letters?
    # restated: is the users's guess (letter) in the word?
    # if the letter is in the word
    # show the letter instead of a blank
    # if the letter is not in the word
    # show the blank
    # and subtract one try
    # show the blanks/filled-in-letters to the user again
    # Ask user for a guess again...

def run_tests():
    print("running tests!")
    print("Testing random_select_word")
    word = random_select_word(4, 12)
    print(word)


if __name__ == "__main__":
    import sys
    
    if "-t" in sys.argv or "--test" in sys.argv:
        run_tests()

    else:
        play_game()