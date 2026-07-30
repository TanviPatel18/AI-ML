# print("tanvi")
import random

def get_choices():
    list=['rock','paper','scissors']
    player_choice=input("enter the choice (rock,paper,scissors)")
    comuter_choice=random.choice(list);
    choices={"player":player_choice,"computer":comuter_choice}
    
    return choices

def check_win(plyer,computer):
    # print("you chose : "+plyer+" , computer chose: "+computer)
    
    print(f"you chose {plyer} , computer chose {computer}")
    if plyer == computer:
        print("try agian")
    elif plyer=="rock" and computer=="scissors":
        print("plyer win the game")
    elif plyer=="scissors" and computer=="paper":
            print("player win the game!")
    elif plyer=="paper" and computer=="scissors":
        print("computer win the game!")
    elif plyer=="scissors" and computer=="rock":
        print("computer win the game!")
    elif plyer=="rock" and computer=="paper":
        print("computer win the game!")
    elif plyer=="paper" and computer=="rock":
            print("computer win the game!")

choice=get_choices()
result=check_win(choice["player"],choice["computer"])
