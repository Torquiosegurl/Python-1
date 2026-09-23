#1. This a game that gives you six tries to guess a five letter word. The letters change colour if its the the right place (green), wrong place (yellow), not in the word (grey)
#2. Make the program randomly select a five letter word from a dictionary and print it out.
#3. The player gets six tries to guess the word.
#4. Success if correct (immediately after guess). Print out word if wrong (after six guesses)

#DICTIONARY SECTION - SECURE A RANDOM WORD

# Load the words from 5letterWords.txt file (personal file)
with open("5letterWords.txt") as f: #ALERT! I wonder if i can get an actual dictionary and filter out words..?
    WORDS = [w.strip().lower() for w in f if len(w.strip()) == 5]

import random
secret = random.choice(WORDS)

#EVALUATION SECTION - TESTS YOUR GUESS

def evaluate_guess(guess, secret): #Tests your guess and returns colours
    guess = guess.upper() #makes all letters uppercase
    secret = secret.upper()

    result = ["gray"] * 5 #the colour gray is actually black but ignore that. This x5 (5 letter word)
    secret_counts = {}

    for ch in secret: #for character in secrets
        secret_counts[ch] = secret_counts.get(ch, 0) + 1

    for i in range(5):
        if guess[i] == secret[i]:
            result[i] = "green"
            secret_counts[guess[i]] -= 1

    for i in range(5):
        if result[i] == "green":
            continue
        ch = guess[i]
        if ch in secret_counts and secret_counts[ch] > 0:
            result[i] = "yellow"
            secret_counts[ch] -= 1

    return result


#KEYBOARD SECTION - COLOURED KEYS + GRID

KEYBOARD_ROWS = [ #prints the keyboard of words
    list("QWERTYUIOP"),
    list("ASDFGHJKL"),
    list("ZXCVBNM")
]
letter_state = {chr(c): "unused" for c in range(ord('A'), ord('Z')+1)} #keeps track of which letters are doing what

COLORS = { #all colours used for wordle
    "green": "\033[1;42m",
    "yellow": "\033[1;43m",
    "gray": "\033[1;40m",
    "reset": "\033[0m"
}

def update_keyboard(guess, result, letter_state): #updates keyboard colours based on guess
    for ch, state in zip(guess.upper(), result):

        if state == "green":
            letter_state[ch] = "green"

        elif state == "yellow":
            if letter_state[ch] != "green":
                letter_state[ch] = "yellow"

        else:  # gray
            if letter_state[ch] == "unused":
                letter_state[ch] = "gray"

def print_keyboard(letter_state): #prints the keyboard, defines the colour of the letters
    for row in KEYBOARD_ROWS:
        line = ""
        for ch in row:
            state = letter_state[ch]
            if state == "unused":
                line += f" {ch} "
            else:
                color = COLORS[state]
                line += f"{color} {ch} {COLORS['reset']}"
        print(line)
    print()

grid = [None] * 6
def print_colored_guess(guess, result): #pute the guess into the grid
    output = ""
    for ch, state in zip(guess.upper(), result):
        color = COLORS[state]
        output += f"{color} {ch} {COLORS['reset']} "
    print(output)

def print_grid(grid): #prints the wordle grid
    for row in grid:
        if row is None:
            # empty row: print 5 blank tiles
            print(" _   _   _   _   _ ")
        else:
            guess, result = row
            print_colored_guess(guess, result)
    print()

#WORDLE BOT (yes i added it are you happy now?)

def analyse_guesses(words, grid): 
    candidates = []

    for word in words:
        valid = True

        for row in grid:
            if row is None:
                continue 
            guess, result = row

            if word == guess: #eliminate all previous guesses 
                valid = False
                break

            for i, (gch, r) in enumerate(zip(guess, result)):
                if r == "gray":
                    appeared_elsewhere = any(
                        (gch == guess[j] and result[j] in ("green", "yellow"))
                        for j in range(len(guess))
                    )
                    if not appeared_elsewhere and gch in word:
                        valid = False
                        break

                elif r == "yellow": #which letters are yellow?
                    if gch not in word or word[i] == gch:
                        valid = False
                        break

                elif r == "gray":
                    # Check if this letter was green/yellow elsewhere in this guess
                    appeared_elsewhere = any(
                        (gch == guess[j] and result[j] in ("green", "yellow"))
                        for j in range(len(guess))
                    )

                    # If it never appeared as green/yellow, gray means "not in the word"
                    if not appeared_elsewhere and gch in word:
                        valid = False
                        break

            if not valid:
                break

        if valid: #reccomends a next best guess
            candidates.append(word)

    return candidates

from collections import Counter

def recommend_guess(candidates): #recommends a next best guess for u
    if not candidates: #no next best guess (bc ur smart like that)
        return None

    # Score words by letter frequency
    letter_counts = Counter("".join(candidates))

    def score(word):
        return sum(letter_counts[ch] for ch in set(word))

    return max(candidates, key=score)

#OTHER STUFF

import os #operating system
def clear_terminal(): #Clears terminal before
    # Check the operating system name
    if os.name == 'nt':  # 'nt' is for Windows
        _ = os.system('cls')
    else:  # 'posix' is for Linux/macOS/Unix
        _ = os.system('clear')

def show_instructions(): #prints a page of instructions bc there's too many atp
    print("""
WELCOME TO WORDLE 

HOW TO PLAY:
- You have 6 tries to guess a secret 5-letter word.
- There are NO PLURAL WORDS included in the guesses.
- After each guess, the tiles will change colour:

  GREEN  = correct letter in the correct spot
  YELLOW = correct letter in the wrong spot
  BLACK  = letter not in the word (you have to turn up your brightness to see it)

- Type 'hint' at any time to get a recommended next guess (this does not count as an attempt)

Press ENTER to begin! (if u fail that's a skill issue for u don't kill me pls)
""")
    input()  # waits for user to press Enter

#GUESS SECTION - KEEPS TRACKS OF GUESSES - Need to fix so that only valid words counts as a guess
clear_terminal() #i don't know why there's so many clear terminals but it only works like this sooooo

attempt = 0 #start of with zero attemps
grid = [None] * 6 #6 guesses. None = no words. 6 empty guesses

clear_terminal() #yes i know there's two clear terminals. No it doesn't work if i take one away. If it aint broke don't fix it
show_instructions()
clear_terminal()

print_grid(grid)
print_keyboard(letter_state)

while attempt < 6: #as long as you have less than six attempts, you can keep guessing.
    guess = input("Enter a 5-letter word (no plurals): ").lower().strip()

    if guess == "hint":
        candidates = analyse_guesses(WORDS, grid) 
        suggestion = recommend_guess(candidates) 
        if suggestion:
            print(f"Suggested guess: {suggestion.upper()}")
        else:
            print("No valid suggestions left.") #if this happens.. well it shouldn't ever happen
        continue

    if guess not in WORDS:
        input("Not in the word list. Press Enter to continue") #there's more then 500k 5 letter words and im not putting all of them on a file.
        clear_terminal()
        print_grid(grid)
        print_keyboard(letter_state)

        continue

    result = evaluate_guess(guess, secret)
    grid[attempt] = (guess, result)
    update_keyboard(guess, result, letter_state)
    clear_terminal()
    attempt += 1
    clear_terminal()

    print_grid(grid)
    print_keyboard(letter_state)

    if guess == secret:
        print("You win! 🥳 ")
        break
else:
    print("You lose! The word was:", secret)
    