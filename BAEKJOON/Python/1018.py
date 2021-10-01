a, b= map(int,input().split())
board = []

#입력
for i in range(a):
    temp = list(input())
    board.append(temp)

#대조군리스트 생성
compare_list_1 = []
for x in range(25):
        compare_list_1.append(list("WB"*25))
        compare_list_1.append(list("BW"*25))

compare_list_2 = []
for x in range(25):
        compare_list_2.append(list("BW"*25))
        compare_list_2.append(list("WB"*25))

#비교
count1 = 0
count2 = 0
#대조군 1
for x in range(a):
    for y in range(b):
        if str(board[x][y]) != str(compare_list_1[x][y]):
            count1 = count1 +1
        
#대조군 2
for x in range(a):
    for y in range(b):
        if str(board[x][y]) != str(compare_list_2[x][y]):
            count2 = count2 + 1
      
#01로 만든 보드 만들기
if count1 <= count2:
    list01 = []
    temp = []
    for x in range(a):
        for y in range(b):
            if str(board[x][y]) == str(compare_list_1[x][y]):
               temp.append(0)
            if str(board[x][y]) != str(compare_list_1[x][y]):
                temp.append(1)
        list01.append(temp)
        temp = []
elif count1 >= count2:
    list01 = []
    temp = []
    for x in range(a):
        for y in range(b):
            if str(board[x][y]) == str(compare_list_2[x][y]):
               temp.append(0)
            if str(board[x][y]) != str(compare_list_2[x][y]):
                temp.append(1)
        list01.append(temp)
        temp = []
    
smallbox=[]
temp = 0

#그 중에서 다 01들을 더했을때 8*8 사이즈 중에서 작은 파트을 더하기
#몇 회 반복할지
for x in range(a-7):
    for y in range(b-7):
        #내용물 다 더하기
        for i1 in range(8):
            for i2 in range(8):
                temp = temp + list01[x+i1][y+i2]
        smallbox.append(temp)
        temp = 0
        

print(min(smallbox))