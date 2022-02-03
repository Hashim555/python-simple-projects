import random
options=["scissor","rock","paper"]


computer_score=0
user_score=0

while True:
    user_choice=input("your choice rock/scissor/paper or Q to quit:" ).lower()
    if user_choice=="q":
        break
    elif user_choice not in options:
        continue
    
    random_value=random.randint(0,2)
    computer_choice=options[random_value]
    print("computer choice is ",computer_choice)

    if user_choice==computer_choice:
        print("tie")
        continue



    elif user_choice=="scissor" and computer_choice== "paper":
        print("user won!")
        user_score+=1
        continue
    
    elif user_choice=="rock" and computer_choice== "scissor":
        print("user won!")
        user_score+=1
        continue    
    
    elif user_choice=="paper" and computer_choice== "rock":
        print("you won!")
        user_score+=1
        continue

    else:
        print("computer won!")
        computer_score+=1
print("computer score",computer_score )
print("user score is: ",user_score)    
  





