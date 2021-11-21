#R바위 P보 S가위 
for _ in range(int(input())):
    Ascore = 0 
    Bscore = 0
    for i in range(int(input())):
        a,b = map(str,input().split())
        if a == "R":
            if b == "R":
                Ascore+=1
                Bscore+=1
            elif b == "P":
                Bscore+=1
            elif b =="S":
                Ascore+=1
        elif a == "P":
            if b == "P":
                Ascore+=1
                Bscore+=1
            elif b == "S":
                Bscore+=1
            elif b =="R":
                Ascore+=1
        elif a == "S":
            if b == "S":
                Ascore+=1
                Bscore+=1
            elif b == "R":
                Bscore+=1
            elif b =="P":
                Ascore+=1

    if Ascore > Bscore:
        print("Player 1")
    elif Ascore == Bscore:
        print("TIE")
    elif Ascore < Bscore:
        print("Player 2")