import sys
#N은 사야하는 줄의 갯수, M은 브랜드 갯수
N, M = map(int,sys.stdin.readline().split())

result = 0
L_6 = 1001
L_1 = 1001

for i in range(M):
    temp1, temp2 = map(int,sys.stdin.readline().split())
    L_6 = (min(temp1,L_6))
    L_1 = (min(temp2,L_1))


#낱개가격이 더 쌀때
if L_1*6 < L_6:
    result = L_1 * N

#묶음이 더 쌀때
else:
    temp = L_6 * (N//6)
    
    if N%6 * L_1 < L_6: 
        temp = temp + (N%6 * L_1)
    else:
        temp = temp + L_6
    result=temp

print(result)
