from collections import deque
import sys

#input = sys.stdin.readline

standard_input = """4
4 2
2 1 4 3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
"""

testCase = int(input())

for _ in range(testCase):
    count, target = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = deque(arr)
    arr_check = [0]*count
    arr_check[target] = 1
    arr_check = deque(arr_check)

    result = 0
    maxnum = max(arr)
    while (arr != ([])):
        print("arr", arr)
        print("arr", arr_check)
        temp = arr.popleft()
        temp2 = arr_check.popleft()
        print("maxnum :", maxnum, "temp :", temp)

        if temp == maxnum and temp2 == 1:
            result += 1
            print("answer: ", result)
            print(result)
            break

        elif temp == maxnum:
            result += 1
            print("프린트 됨", result)
            maxnum = max(arr)
        else:
            print("큐 밀림")
            arr.append(temp)
            arr_check.append(temp2)
        print()
    print("\n\n")
