import sys

lis = []
for i in range(int(sys.stdin.readline().strip())):
    a,b = sys.stdin.readline().split()
    a = int(a)
    lis.append([i,a,b])


c = sorted(lis, key = lambda x : (x[1] , x[0]))

for i in range(len(c)):
    
    print(c[i][1],c[i][2])
