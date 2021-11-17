import sys

a = int(sys.stdin.readline())
result = 0

while(a>=5):
    a -= 5
    result +=1

while(a>=3):
    a -= 3
    result +=1

if a==0:
    print(result)
else:
    print("-1")




