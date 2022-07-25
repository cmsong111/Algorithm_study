import sys

students = int(sys.stdin.readline().strip())
arr = []
for i in range(students):
    arr.append(sys.stdin.readline().strip())

result = 1
numlen = len(arr[0])
#print("len",students)

for i in range(1,numlen+1):
    temp = []
    for ii in arr:
        temp.append(ii[numlen-i:])
    check = set(temp)
    #print(temp,check,i)

    if len(check) == students:
        print(result)
        break
    result +=1

