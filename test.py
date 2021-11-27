import sys
import numpy as np
count = int(sys.stdin.readline().strip())
arr = np.array(list(map(int,sys.stdin.readline().split())))
result = 0

mid = int((count+1)/2)-1
arr = np.sort(arr,kind='quick sort')
arr1 = np.array(list(arr[:mid+1]))

count1 = len(arr1)-1
while(arr1[count1]!=0):
    arr1 = np.sort(arr1,kind='quick sort')
    arr1[count1] = int(arr1[count1]/2)
    result +=1

print(result)