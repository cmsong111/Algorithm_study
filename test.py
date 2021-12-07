import sys
from typing import List

for i in range(int(sys.stdin.readline().strip())):
    a,b = map(str,sys.stdin.readline().split())
    a_arr = []
    b_arr = []
    for i in range(len(a)):
        a_arr.append(a[i])
    for i in range(len(b)):
        b_arr.append(b[i])
    
    a_arr.sort()
    b_arr.sort()


    if a_arr == b_arr:
        print(a,"&",b,"are anagrams.")
    else:
        print(a,"&",b,"are NOT anagrams.")