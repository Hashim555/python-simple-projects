import random

top_of_range = input("Type a range of number you want to guess: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()

random_number= random.randint(0,top_of_range)      
guesses=0
while True:
    guesses+=1
    guess= input("gass a number ")
    if guess.isdigit():
        guess=int(guess)
    else:
        print("plz type a value next time")
    
    if guess== random_number:
        print("you got it")
        break
    elif guess>random_number:
        print("you are above the number")
    elif guess<random_number:
        print("you are blow the number")
print("You got it in", guesses, "guesses")