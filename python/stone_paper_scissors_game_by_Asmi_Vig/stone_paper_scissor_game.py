import random

def gameWin(comp, you):
    if comp==you:
        return None

    elif comp=='s':
        if you=='p':
            return True
        elif you=='sc':
            return False

    elif comp=='p':
        if you=='sc':
            return True
        elif you=='s':
            return False

    elif comp=='sc':
        if you=='s':
            return True
        elif you=='p':
            return False

RandNo=random.randint(1,3)

if RandNo==1:
    comp='s'
elif RandNo==2:
    comp='p'
elif RandNo==3:
    comp='sc'

print("computer choses stone(s), paper(p), scissor(sc):")
you=input("your choice is stone(s), paper(p), scissor(sc): ")

a=gameWin(comp, you)

print(f"computer choses {comp}")
print(f"you choses {you}")

if a==None:
    print("it's a tie!")

elif a:
    print("you win!")

else:
    print("you lose!")