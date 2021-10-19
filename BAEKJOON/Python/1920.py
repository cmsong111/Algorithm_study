import sys

def search (array,target,first,end):
    if first > end:
        return "0"
    mid = (first+end) // 2
    if array[mid] == target:
        return "1"
    elif array[mid] > target:
        return search(array,target,first,mid-1)
    else:
        return search(array,target,mid+1,end)

N1 = int(input())
N = list(map(int,sys.stdin.readline().split()))
M1 = int(input())
M = list(map(int,sys.stdin.readline().split()))
N.sort()

for i in range(M1):
    print(search(N,M[i],0,N1-1))
