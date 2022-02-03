
name=input("type yor name: ")
print("welcome to an adventure game",name+"!")

answer=input("\nDo you want to play this game: ")


if answer!="yes":
    quit()   

user_input=input("\nyou are walking on a straight road and the road is came to end. you can go left or right.which way would you like to go left/right: ").lower()
if user_input=="left":
    user_input=input("\nyou reached along a river. you can walk arount to it or swim. type walk to walk and swim to swim: ").lower()
    if user_input=="walk":
        print("You walked for many miles, ran out of water and you lost the game")
    elif user_input=="swim":
        user_input= input("\nwater is so cold and destination is so far. if you want ship. wave the ship by typing wave and type swim to swim: ").lower()
        if user_input=="wave":
            print("you got the ship! so you won")

        elif user_input=="swim":
            print("you swim alot now you get tried and the destination is so far so you lost the game")

        else:
            print("you choose wrong option so you lose the game")         


    else:
        print("you choose wrong option so you lose the game")       

elif user_input=="right":
    user_input=input("\nYou come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)?: " ).lower()
    if user_input=="cross":
        print("You talk to the stanger and they give you gold. You WIN!")
    elif user_input=="back":
        print("You ignore the stranger and they are offended and you lose.")
    else:
            print("you choose wrong option so you lose the game") 


else:
    print("\nyou choose wrong option so you lose the game")        

print("Thanks for playing",name)