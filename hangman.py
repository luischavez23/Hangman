import random

words = ['eyes', 'glasses', 'pizza','angry', 'fire', 'pineapple', 'baby', 'flower', 'ball'];

chosen_words = random.choice(words);
print(chosen_words)

guess = input('Guess a letter: ').lower()


for letter in chosen_words:
    if letter == guess:
        print('Right')
    else:
        print('Wrong')
