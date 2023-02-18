# guess2.py
# Author: Kealan McGuinness
# Week 04 program tells the user if there guess is too high or too low, each time they guess

number_to_guess = 30

guess = int(input('Please guess a number: '))
while guess != number_to_guess:
    if guess < number_to_guess:
        print ("too low")
    else: 
        print ("too high")
    guess = int(input("Please guess again: "))

print ("Well done! Yes the number was", number_to_guess)
