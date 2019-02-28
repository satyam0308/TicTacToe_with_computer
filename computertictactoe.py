from os import system,name
def clear():
    if name=='nt':
        _ = system('cls')
def checkwin(a):
    if a[0]=='X' and a[1]=='X' and a[2]=='X':
        return 1
    elif a[0]=='X' and a[3]=='X' and a[6]=='X':
        return 1
    elif a[0]=='X' and a[4]=='X' and a[8]=='X':
        return 1
    elif a[2]=='X' and a[4]=='X' and a[6]=='X':
        return 1
    elif a[2]=='X' and a[5]=='X' and a[8]=='X':
        return 1
    elif a[6]=='X' and a[7]=='X' and a[8]=='X':
        return 1
    elif a[3]=='X' and a[4]=='X' and a[5]=='X':
        return 1
    elif a[1]=='X' and a[7]=='X' and a[4]=='X':
        return 1

    if a[0]=='O' and a[1]=='O' and a[2]=='O':
        return 2
    elif a[0]=='O' and a[3]=='O' and a[6]=='O':
        return 2
    elif a[0]=='O' and a[4]=='O' and a[8]=='O':
        return 2
    elif a[2]=='O' and a[4]=='O' and a[6]=='O':
        return 2
    elif a[2]=='O' and a[5]=='O' and a[8]=='O':
        return 2
    elif a[6]=='O' and a[7]=='O' and a[8]=='O':
        return 2
    elif a[3]=='O' and a[4]=='O' and a[5]=='O':
        return 2
    elif a[1]=='O' and a[7]=='O' and a[4]=='O':
        return 2
     
    return 0

def printposition(a):
    k=0
    for i in range(3):
        for j in range(3):
            if a[k]=='0':
              print("  " ,end='')
            else:
                print(" %c" %a[k],end='')
            if (k==0 or k==1 or k==3 or k==4 or k==6 or k==7):
                print('  |',end='')
            k=k+1
        if i!=2:
            print()
            print('--------------')
    print("\n")

def fillposition(a,ki):
    if positionavailable(a,ki):
            a[ki-1]='X'
            return 1
        
    else:
        return 0
              

def positionavailable(a,ki):
    if a[ki-1]=='0':
        return 1
    else:
        return 0

    
def gamestart(a):
    k=0
    for i in range(3):
        for j in range(3):
            print("  " ,end='')
            if (k==0 or k==1 or k==3 or k==4 or k==6 or k==7):
                print('  |',end='')
            k=k+1
        if i!=2:
            print()
            print('--------------')
def draw(a):
    L=0
    for i in a:
        if i=='0':
            L=1
    if L==1:
        return 0
    else:
        return 1
def availablespace(a):
    k=[]
    l=[]
    j=0
    for i in a:
        if i=='0':
            k+=[j]
        j+=1   
    if k!=l:
       return k
    else:
        return 1
def computerchance(a):
    import random
    l=availablespace(a)
    if l!=1:
        s=random.sample(l,1)
        s=s.pop()
        a[s]='O'
        clear()
        print("Player1-'X' \nComputer-'O'")
        print("Use numpad for playing")
        print("player1-%d Computer-%d Draw-%d" %(player1_score,Computer,Draw))
        print("\n\n")
        printposition(a)


player1_score=0
Computer=0
Draw=0
while True:
    clear()
    a=['0','0','0','0','0','0','0','0','0']
    print("Player1-'X' \nComputer-'O'")
    print("Use numpad for playing")
    print("player1-%d Computer-%d Draw-%d" %(player1_score,Computer,Draw))
    print("\n\n")
    gamestart(a)
    while True:
        try:
            var1=0
            while var1==0:
                    ki=int(input("\nPlayer1 "))
                    if ki>=1 and ki<10:
                        if fillposition(a,ki):
                            clear()
                            var1=1
                            print("Player1-'X' \nComputer-'O'")
                            print("Use numpad for playing")
                            print("player1-%d Computer-%d Draw-%d" %(player1_score,Computer,Draw))
                            print("\n\n")
                            printposition(a)
                            
                            
                        else:
                            print("The position is already taken,Choose another one")
                    
            S=checkwin(a)
            if S==1:
                print("\nplayer1 won")
                player1_score=player1_score+1
                break
            elif S==2:
                print("\ncomputer won")
                Computer=Computer+1
                break
            if draw(a):
                print("\nMatch Drawn")
                Draw=Draw+1
                break

            computerchance(a)
            S=checkwin(a)
            if S==1:
                print("\nplayer1 won")
                player1_score=player1_score+1
                break
            elif S==2:
                print("\ncomputer won")
                Computer=Computer+1
                break
            if draw(a):
                print("\nMatch Drawn")
                Draw=Draw+1
                break
                
        except:
            pass

    input("Next Match-Press enter")


    
        
