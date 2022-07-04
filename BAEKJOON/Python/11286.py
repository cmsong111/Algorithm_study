import sys
import heapq

a = int(sys.stdin.readline().rstrip())

arrPlus = []
arrMinus = []

for i in range(a):
    temp = int(sys.stdin.readline().rstrip())
    if temp == 0: #출력

        if arrPlus and arrMinus:
            if arrPlus[0] < arrMinus[0]:
                print(heapq.heappop(arrPlus))
            else:
                print(-heapq.heappop(arrMinus))
        elif arrPlus:
            print(heapq.heappop(arrPlus))
        elif arrMinus:
            print(-heapq.heappop(arrMinus))
        else:
            print(0)

    else: #삽입
        if temp > 0:
            heapq.heappush(arrPlus, temp)
        else:
            heapq.heappush(arrMinus, -temp)