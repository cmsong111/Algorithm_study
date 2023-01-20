standard_input = "4 2"

from itertools import combinations_with_replacement

a,b = map(int,input().split())

arr = list(combinations_with_replacement(range(1,a+1),b))

for i in arr:
    for j in i:
        print(j,end=" ")
    print()