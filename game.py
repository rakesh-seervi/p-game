import random

def gamewin(comp,you):
    if comp == you :
        return None
    elif comp =='r':
        if you =='p':
            return True
        elif you =='s':
            return False
    elif comp =='p':
        if you =='s':
            return True
        elif you =='r':
            return False       
    elif comp =='s':
        if you =='r':
            return True
        elif you =='p':
            return False

print("comp turn: rock(r) paper(p) or scissor(s)? ")
ran = random.randint(1, 3)
if ran == 1:
    comp ='r'
if ran == 2:
    comp ='p'       
if ran == 3:
    comp ='s'

you = input("your turn: rock(r) paper(p) or scissor(s)? ")
a = gamewin(comp, you)

print(f"computer choose {comp}")
print(f"you choose {you}")

if a == None:
    print("game is tie!")
elif a:
    print("you won!")
else :
    print("you lose")


        