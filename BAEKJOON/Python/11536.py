import sys
count = int(sys.stdin.readline().strip())

list_arr = []

for i in range(count):
    temp = sys.stdin.readline().strip()
    list_arr.append(temp)

DECREASING = list(list_arr)
INCREASING = list(list_arr)

DECREASING.sort(reverse=True)
INCREASING.sort()

if list_arr == DECREASING:
    print("DECREASING")
elif list_arr == INCREASING:
    print("INCREASING")
else:
    print("NEITHER")    
