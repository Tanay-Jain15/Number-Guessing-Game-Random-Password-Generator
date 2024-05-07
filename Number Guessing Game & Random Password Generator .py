#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Number Guessing Game

import random

target = random.randrange(1,100)


while True:                                                # we took TRUE here becz we want to run again and again till the condition gets true. True is used for infinite loop.
    user_choice = input("Guess the target or Quit(Q) : ")
    if user_choice == "Q":
        break
        
    user_choice = int(user_choice)
    if user_choice == target:
        print("Success: Correct Guess !! ")
        break
    
    elif user_choice < target:
        print("Your number was too small....take a bigger guess.")
    
    else:
        print("Your number was too big....take a lower guess.")

print("\n-----Game Over-----")
    
    
# IN THIS TARGET NUMBER IS GENERATED ONLY ONCE BY THE COMPUTER... WE HAVE TO GUESS AGAIN AND AGAIN TILL WE TYPE THE CORRECT NUMBER.    


# In[3]:


# Random Password Generator

import random
import string  # all the ascii characters

pass_len = 12
char_values = string.ascii_letters + string.digits + string.punctuation

password = ""
for char in range(pass_len):
    password += random.choice(char_values)
print("your random password is: ", password)    


# In[ ]:




