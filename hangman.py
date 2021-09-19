import random
from words_list import words
from body_art import body,logo

end_game = False
chosen_words = random.choice(words);
words_len = len(chosen_words);

#Create lives
lives = 6

#Create blanks
display = []
for _ in range (words_len):
    display += "_"

print(logo)

#Loop for the game
while not end_game:
    guess = input('Guess a letter: ').lower();
    
    #Checked guessed letter
    for position in range (words_len):
        letter = chosen_words[position]
        if letter == guess:
            display[position] = letter
    
    #If doesn't guess letter
    if guess not in chosen_words:
        lives -= 1
        if lives == 0:
            end_game = True;
            print(f'You Lose, the word was: {chosen_words.upper()}');
    
    print(f"{' '.join(display)}")
    print(body[lives])     

    #Check if there are no more "_"
    if "_" not in display:
        end_game = True;
        print('You win');   

    
