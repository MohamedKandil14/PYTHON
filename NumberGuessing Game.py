import random
top_of_range=input("Enter A number : ")
if (top_of_range.isdigit()):
    top_of_range=int(top_of_range)
    if(top_of_range<=0):
        print("Enter number Greater Than 0")
        quit()
else:
    print("Please Enter A number : ")
    quit()
random_number=random.randint(0,top_of_range)
attemps=0
while True :
    attemps+=1
    user_guess=input("Guess A Number: ")
    if(user_guess.isdigit()):
        user_guess=int(user_guess)
    else:
        print("Enter A number")
        continue
    if(user_guess==random_number):
        print("You got it")
        break
    else:
        if(user_guess>random_number):
            print("you are Above the Number")
        else:
            print("You Are below The Number")

        
print("you try ",attemps,"to got it successfully")        