import sys

total = int(sys.stdin.readline().rstrip())
count = int(sys.stdin.readline().rstrip())

result = 0

for i in range(count):
    a,b = map(int,sys.stdin.readline().split()) 
    result +=  a*b

if total == result:
    print("Yes")
else:
    print("No")