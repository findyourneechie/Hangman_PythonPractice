msg = 'Hello World'
print(msg)

    # Get a random word : List of words that will be picked for the player


import random 

    # Small sample list of words for the game: array
words = ['general, assembly, developer, engineer, immersive, fifteen, washington, ']

#lives remaining
lives_left = ''
#letters guessed
letters_guessed = ''

def chooseWord () :
    letter = random.randint(0, len(words)-1)
    return words(letter)

print(chooseWord())

