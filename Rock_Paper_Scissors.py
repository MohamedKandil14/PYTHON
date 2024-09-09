import random
user_score=0
comp_score=0
options=["paper","rock","scissors"]
while True:
    user_input=input("type paper / rock / scissors or Q to quit: ").lower()
    if (user_input=="q"):
        break
    if (user_input not in options):
        continue
    random_number=random.randint(0,2)
    computer_pick=options[random_number]
    print("computer pick",computer_pick +".")
    if (user_input=="rock" and computer_pick=="paper"):
        print("you win")
        user_score+=1
    elif (user_input=="paper" and computer_pick=="scissors"):
         print("you win")
         user_score +=1
    elif (user_input=="scissors" and computer_pick=="rock"):
        print("you win")
        user_score+=1
    else:
        print("You Lost")
        comp_score+=1


print('You Win ',user_score  ,'times')
print('computer Win ', comp_score , 'times')
print("Goodbye")