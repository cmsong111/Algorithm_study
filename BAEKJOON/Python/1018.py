a, b= map(int,input().split())
board = []

#�Է�
for i in range(a):
    temp = list(input())
    board.append(temp)

#����������Ʈ ����
compare_list_1 = []
for x in range(25):
        compare_list_1.append(list("WB"*25))
        compare_list_1.append(list("BW"*25))

compare_list_2 = []
for x in range(25):
        compare_list_2.append(list("BW"*25))
        compare_list_2.append(list("WB"*25))

#��
count1 = 0
count2 = 0
#������ 1
for x in range(a):
    for y in range(b):
        if str(board[x][y]) != str(compare_list_1[x][y]):
            count1 = count1 +1
        
#������ 2
for x in range(a):
    for y in range(b):
        if str(board[x][y]) != str(compare_list_2[x][y]):
            count2 = count2 + 1
      
#01�� ���� ���� �����
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

#�� �߿��� �� 01���� �������� 8*8 ������ �߿��� ���� ��Ʈ�� ���ϱ�
#�� ȸ �ݺ�����
for x in range(a-7):
    for y in range(b-7):
        #���빰 �� ���ϱ�
        for i1 in range(8):
            for i2 in range(8):
                temp = temp + list01[x+i1][y+i2]
        smallbox.append(temp)
        temp = 0
        

print(min(smallbox))