print("WELCOME TO MY COMPUTER QUIZ")

start=input("Do you want to play this quiz game? ")

score=0
if start.lower() !="yes" :
    quit()

answer=input(" what is cpu ")
if answer.lower()== "central processing unit":
    print("correct")
    score=1+score
else: 
    print("incorrect")

answer=input("2*3= ")
if answer== "6":
    print("correct")
    score=1+score

else: 
    print("incorrect")
answer=input("2+5= ")
if answer== "7":
    print("correct")
    score=1+score
else: 
    print("incorrect")


answer=input("10+2= ")
if answer== "12":
    print("correct")
    score=1+score
else: 
    print("incorrect")        


print("you got " + str(score) + " questions correct")
print("you got "+ str((score/4*100)) + " %")