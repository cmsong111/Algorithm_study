import sys

count = int(input())

arr = []

for i in range(count):
    temp_name,temp_day,temp_month,temp_year = map(str,sys.stdin.readline().split())
    arr.append([int(temp_year),int(temp_month),int(temp_day),temp_name])


arr.sort()

print(arr[count-1][3])

print(arr[0][3])
