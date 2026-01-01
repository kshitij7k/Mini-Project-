"""
Rock =1
Paper=0
scissor =-1
"""
import random
Computer=random.choice([1,0,-1])
User=input("Enter your choice :")
youDict={"r":1,"p":0,"s":-1}
#reverseDict={1:"Rock",0:"Paper",-1:"Scissor"}
you=youDict[User]

print(f"Computer chose {Computer}")

if(Computer==you):
    print("Its a Draw")

else:
    if(Computer==0 and you==1):
        print("You Lose")
    elif(Computer==0 and you==-1):
        print("You Win")
    elif(Computer==1 and you==0):
        print("You Win")
    elif(Computer==1 and you==-1):
        print("You Lose")
    elif(Computer==-1 and you==1):
        print("You Win")
    elif(Computer==-1 and you==0):
        print("You Lose")
    else:
        print("something went wrong!")