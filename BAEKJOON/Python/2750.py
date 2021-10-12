import sys

a = int(input())
counting = [0]*10001
for i in range(a):
    counting[int(sys.stdin.readline())] +=1

print(counting)

for i,j in enumerate(counting):
    if j != 0:
        for _ in range(j):
            print(i)
            