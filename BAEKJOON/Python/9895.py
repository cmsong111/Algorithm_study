a = int(input())
for i in range(a):
    string = input()
    long = len(string)
    score = []

    for i in range(long):
        if string[i] == "O":
            score.append(int(1))
        elif string[i] == "X":
            score.append(int(0))
        
    
    for i in range(1,long):
        if score[i] != 0:
            if score[i-1] != 0:
                score[i] = score[i-1]+1

    print(sum(score))