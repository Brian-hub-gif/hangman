import random
import secret_words
secret_word = random.choice(secret_words.secret_words_list)
word_lenght = len(secret_word)
hidden_word = []
guess_count = 0
guess_limit = 6

def display_gallows(guess_count):
    gallows = [
    	"""
       -------
       
       |    |
       |
       |
       |
       |
       -
       """    
       ,
       """
 	      -------
       |      |
       |      O
       |
       |
       |
       -  
 	     """
 	     ,
 	     """
 	      -------
       |      |
       |      O
       |      |
       |      |
       |
       -  
 	     """
 	     ,
 	     """
 	      -------
       |      |
       |      O
       |    / |
       |      |
       |
       -  
 	     """
 	     ,
 	     """
 	      -------
       |      |
       |      O
       |    / | \\
       |      |
       |
       -  
 	     """
 	     ,
 	     """
 	      -------
       |      |
       |      O
       |    / | \\
       |      |
       |     /
       -  
 	     """
 	     ,
 	     """
 	      -------
       |      |
       |      O
       |    / | \\
       |      |
       |     / \\
       -  
 	     """
 	   ]
    return gallows[guess_count]	
 	                                  
print(display_gallows(guess_count))

def hidden_word_func(word_lenght):
    i = 0
    while i < word_lenght:
        hidden_word.append("_")
        i = i + 1
    return hidden_word


hidden_word = hidden_word_func(word_lenght)
print(hidden_word)
#print(word_lenght)
x = 0
mySeparator = ""
guess_word = False
answer = ""
while guess_count < guess_limit and answer != secret_word:
    guess_input = input("Enter guess:")
    times_guess_appear = secret_word.count(guess_input)
    if times_guess_appear < 1:
        print(guess_input + " is not a letter or word")
        guess_count = guess_count + 1
        print(display_gallows(guess_count))
        print("number of guesses used:{}".format(guess_count))
        print(hidden_word)
    elif times_guess_appear >= 1:
        for index in range(len(secret_word)):
            if secret_word[index] == guess_input:
                hidden_word[index] = guess_input
                print(display_gallows(guess_count))
                print(hidden_word)
                answer = mySeparator.join(hidden_word)
    #else:
    #      guess_word = True
    #      print("You Won!!")
if answer == secret_word:
    print("You Win!!")
    print("answer is :{}".format(secret_word))
elif guess_count == guess_limit:
     print("Out of guesses .You lose!!answer is:{}".format(secret_word))
      
   
 

