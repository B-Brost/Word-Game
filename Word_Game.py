"""
Word_Game.py
Brianna Brost
1/17/23
A word game where the user guesses a 5 letter word and the computer gives feedback on the guess.
G means the letter is in the correct place, Y means the letter is in the word but not in the correct place, and B means the letter is not in the word.
"""
from random import randint
words=[]
# reads file and makes list of 5 letter words
with open("usaWords.txt", "r") as file:
     for line in file:
         word = line.rstrip()
         if len(word)==5:
            words.append(word)
# gets random index for the word and chooses the word
index=randint(0,len(words))
word=words[index]
# print(word)
# turns the word into letters
print_answer_letters=[letter for letter in word]
answer_letters=print_answer_letters
guesses=[]
answers=[]
count=0
# repeats the code 6x
for i in range(6):
    count +=1
    # asks user for guess
    guess=input(str("What is your guess? "))
    # makes it lower case and adds guess to list of guesses
    guess=guess.lower()
    guesses.append(guess)
    # checks that word is 5 letter
    if len(guess)!=5:
        print("Must guess a 5 letter word.")
        answers.append("Invalid Guess")
    else:
        # checks that word is in dictionary
        if guess not in words:
            print("Word is not in dictionary")
            answers.append("Invalid Guess")
        else:
            # turns the guess into list of letters
            letters=[letter for letter in guess]
            # sets all answer letters to B
            response_colors=['B','B','B','B','B']
            # resets answer letters 
            for i in range(len(word)):
                answer_letters[i]=word[i]
            for i in range(len(letters)):
                # checks if letter is in correct place
                if letters[i] == answer_letters[i]:
                    answer_letters[i]='0'
                    response_colors[i]='G'
            # checks if letter is in word and not guessed yet
            for i in range(len(letters)):
                if letters[i] in answer_letters and response_colors[i]!='G':
                    the_index=answer_letters.index(letters[i])
                    answer_letters[the_index]='1'
                    response_colors[i]='Y'
            print()
            # adds answer colors to list
            answers.append(response_colors)
            for i in range(len(answers)):
                # prints Guess #: guess , answer colors
                print(f'Guess {i+1}: {guesses[i]} , {answers[i]}')
            # if answer in 1 shot gets special message
            if response_colors==['G','G','G','G','G'] and count==1:
                print(f"Hole in one! It took 1 try to get the correct answer! ")
                quit()
            # answer message for correct guess
            elif response_colors==['G','G','G','G','G']:
                print(f"Correct! You took {count} tries to get the correct answer!")
                quit()
# you lose message
if count>=6:
    print(f"You lose! You ran out of tries! The correct answer was {word}.")
    quit()

