print("Welcome To My Quiz GAME")
PLAYING=input("Do you Want To Play ? ")
if (PLAYING.lower()!="yes"):
    quit()
print("Let`s begin")
score=0
answer=input('WHAT`S CPU stands For ? ')
if(answer.lower()=="central processing unit"):
    print("correct! ")
    score+=1
else:
    print("Incorrect")
answer=input('WHAT`S GPU stands For ? ')
if(answer.lower()=="Graphic processing unit"):
    print("correct! ")
    score+=1
else:
    print("Incorrect")
answer=input('WHAT`S RAM stands For ? ')
if(answer.lower()=="random access memory"):
    print("correct! ")
    score+=1
else:
    print("Incorrect")
answer=input('WHAT`S PSU stands For ? ')
if(answer.lower()=="power supply unit"):
    print("correct! ")
    score+=1
else:
    print("Incorrect")
print("You got " + str(score) + "Correct Answers")
print("You got " + str((score/4)*100) + "%.")