import random
import word_file
import hangman_stages

word_list = word_file.words
lives = 6
word = random.choice(word_list)
display = []

for letter in word:
    display += '_'

print(display)
game_over=False

while not game_over:
    guess_letter = input("Guess a letter: ").lower()
    for position in range(len(word)):
        if guess_letter == word[position]:
            display[position] = guess_letter
    print(display)
    if guess_letter not in word:
        lives -=1
        if lives == 0:
            game_over = True
            print("You lose!!")
    if '_' not in display:
        game_over = True
        print("You win!!")
    print(hangman_stages.stages[lives])



