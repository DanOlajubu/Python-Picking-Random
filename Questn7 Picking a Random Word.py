#Project 7 - Pick a random word	out of	a word list
#Won’t need user input,	but will need to either	create a word list from	code,
#or  scratch (simple text file)
#Remember how to open files for	reading
#Will need some	randomness in there somehow – (import	random)

# importing nescessary modules

import random 
 
random_word_list = ["Rehoboth","me","you","my-past","my-present","charity"] 
 
# method 1 to generate a random word from the list

random_word = random.choice(random_word_list) 
print(random_word) 
 
# method 2 to generate a random word 
# this method will generate a random index, 
# lying inside the list indices, then get the word at the index 
random_word = random_word_list[random.randint(0,len(random_word_list))] 
print(random_word)
print("\n")


print("----------------------------------------------------------------")
# read all the list of words
words = []
with open('wordlist.txt', 'r') as file:
    line = file.readline().strip()
    words.append(line)
    while line:
        line = file.readline().strip()
        words.append(line)

random_index = random.randint(0, len(words))
  
print("Your random word is:", words[random_index])


###  OR  ###

import random

print(random.choice(open("wordlist.txt").read().split()))
