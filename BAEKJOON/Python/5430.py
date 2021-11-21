import sys

for _ in range(int(sys.stdin.readline().strip())):
    #RDD
    temp = sys.stdin.readline().strip()
    todolist = []
    for i in range(len(temp)):
        todolist.append(temp[i])
    #4 배열의 개수 입력
    count = int(sys.stdin.readline().strip())
    #[1,2,3,4]
    arrlist = []
    temp = sys.stdin.readline().rstrip()[1:-1].split(",")
    


    Rcount = 0
    Rpop = 0
    Lpop = 0
    errorcount = 0

    for i in todolist:
        if i == "D":
            if count == 0:
                print("error")
                errorcount+=1
                break
            else:
                if Rcount%2 == 0:
                    Lpop+=1
                    count -=1
                else:
                    Rpop+=1   
                    count -=1
        elif i =="R":
            Rcount +=1

    
    if Rcount%2 ==1:
        if Rpop == 0:
            temp[Lpop:]
            temp.reverse()
        else:
            temp = temp[Lpop:-Rpop]
            temp.reverse()
    else:
        if Rpop == 0:
            temp = temp[Lpop:]
        else:
            temp = temp[Lpop:-Rpop]

    if count != 0:
        print("[",end="")
        for i in range(count-1):
            print(temp[i],end=",")
        print(temp[count-1],"]",sep="")
    elif errorcount == 0:
        print("[]")