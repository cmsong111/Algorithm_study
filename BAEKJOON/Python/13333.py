standard_input = """6
12 7 6 8 9 10
"""
import sys

#input = sys.stdin.readline
count = int(input())

arr = list(map(int,input().split()))

arr.sort(reverse=True)

while(arr):
    # print("arr: ",arr)
    # print("최소값: ",arr[-1])
    # print("카운트: ",count)
    check = arr.pop()
    if count <= check:
        print(count)
        break
    count-=1
else:
    print(0)

