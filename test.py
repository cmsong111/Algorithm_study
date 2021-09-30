a,b= map(int,input().split())

board = []

#입력
for i in range(a):
    temp = list(input())
    board.append(temp)

#출력( 잘 받았는지)
for x in range(a):
    for y in range(b):
        print(board[x][y],sep="",end="")
    print()



#처리(비교하는 부분)

#board[0][0]번이 B일때
count1 = 0
check = 0
if b % 2 == 1:
    for x in range(a):
        for y in range(b):
            check +=1
            if check % 2 == 0:
                word = "B"
            else:
                word = "W"
            if board[x][y] != "B" :
                

print(count1)
    
#board[0][0]번이 W일때
count2 = 1


#비교하기

print(min(count1,count2))
