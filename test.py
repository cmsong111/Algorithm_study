import sys

size = int(sys.stdin.readline())
board = []
result = []


#입력받기
for i in range(size):
    temp = sys.stdin.readline().strip()
    tmp=[]
    for i1 in range(len(temp)):
        tmp.append(temp[i1])
    board.append(tmp)

for i in range(size):
    result.append([0]*size)


#작업부
for x in range(size):
    for y in range(size):
        if board[x][y] == ".":
            #가로 줄 
            if "B" in board[x][y:]:
                print(x,y,board[x][y:])
                if "W" in board[x][y:]:
                    result[x][y] += 1
                print(x,y,board[x][:y])
                if "W" in board[x][:y]:
                    result[x][y] += 1
                print(result[x][y])

            #세로 줄 
            if "B" in board[x:][y]:
                print(x,y,board[x:][y])
                if "W" in board[x:][y]:
                    result[x][y] += 1
                print(x,y,board[:x][y])
                if "W" in board[:x][y]:
                    result[x][y] += 1
                print(result[x][y])

            
                


#출력부
for x in range(size):
    for y in range(size):
        print(board[x][y],end="")
    print()    