import sys
answer = 0
for i in range(4):
    answer+= int(sys.stdin.readline().rstrip())

print(answer//60)
print(answer%60)