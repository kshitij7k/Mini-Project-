import random
n= random.randint(1,100)
a= -1
guess =0
while(a !=n):
    a=int(input("Enter the number:"))
    guess +=1
    if(a>n):
        print("Enter the lower number!")
    else:
        print("Enter the higher number!")
print(f"you guessed correct and the gusses you took was {guess} the no is {n}")