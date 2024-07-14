#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
def get_input(prompt, valid_options):
    while True:
        response = input(prompt).lower()
        if response in valid_options:
            return response
        else:
            print(f"Invalid option. Please choose from {valid_options}.")

def random_event():
    events = ["find a treasure", "fall into a trap", "meet a friendly creature", "get lost"]
    return random.choice(events)

score = 0

answer = get_input("Do you want to play this text adventure game? (yes/no) ", ["yes", "no"])

if answer == "yes":
    print("That's great!\n")
    answer = get_input("Do you want to explore a cave or jungle? (cave/jungle) ", ["cave", "jungle"])
    
    if answer == "cave":
        print("You go into the cave and see a lion\n")
        answer = get_input("Do you want to fight or run? (fight/run) ", ["fight", "run"])
        
        if answer == "fight":
            print("Lion is dangerous! You lose!")
            score -= 10
        
        elif answer == "run":
            print("You ran away! You win!")
            score += 10

        event = random_event()
        if event == "find a treasure":
            print("You find a hidden treasure! Your score increases.")
            score += 20
        elif event == "fall into a trap":
            print("You fall into a trap! Your score decreases.")
            score -= 15
        elif event == "meet a friendly creature":
            print("You meet a friendly creature who helps you. Your score increases.")
            score += 10
        elif event == "get lost":
            print("You get lost in the cave. Your score decreases.")
            score -= 5
        
    elif answer == "jungle":
        print("You meet a tiger and you get eaten! You lose!")
        score -= 10
        
    else:
        print("Invalid option, you lose!")
        score -= 5
        
else:
    print("But this is a really awesome game!")
    score -= 1

print(f"Your final score is: {score}")

