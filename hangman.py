import random

words = ['eyes', 'glasses', 'pizza','angry', 'fire', 'pineapple', 'baby', 'flower', 'ball'];
chosen_words = random.choice(words);
words_len = len(chosen_words);

#Create blanks
display = []
for _ in range (words_len):
    display += "_"

end_game = False

while not end_game:
    guess = input('Guess a letter: ').lower();
    
    #Checked guessed letter
    for position in range (words_len):
        letter = chosen_words[position]
        if letter == guess:
            display[position] = letter
    
    print(display)

    #Check if there are no more "_"
    if "_" not in display:
        end_game = True 
        print('You win')        
    
