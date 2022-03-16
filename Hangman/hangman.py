# importing packages from my local drive
# i would rather suggest you to import your own images
import random
import hangman_words 
import logo
import hangman_art 
from replit import clear

print(f"Welcome to the game: {logo.hangman}")





chosen_word = random.choice(hangman_words.word_list)


word_length = len(chosen_word)


# creating blank space
display = []
for _ in range(word_length):
  display+= "_"



end_of_game = False

lives = 6


while not end_of_game:
  # getting seperate letters
  guess = input("Enter a letter: ").lower()

  clear()

  if guess in display:
    print(f"You have already guessed the letter '{guess}', choose another letter")
  
  # code for the game
  
  
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter


  if guess not in chosen_word:
    lives-=1
    print(f"The letter you guessed {guess} is not in the word, You lose a life")
    if lives ==0:
      end_of_game = True
      print("You lose")
      
  
  print(display)    
  if "_" not in display:
    end_of_game = True
    print("You Win")

    

  print(hangman_art.hangman_pic[lives])
