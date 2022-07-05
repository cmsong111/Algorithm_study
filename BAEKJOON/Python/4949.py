import sys

while(True):
    a = sys.stdin.readline().rstrip()
    errorcount= 0
    arr = []
    if a == ".":
        break

    for i in a:
        if i == '(':
            arr.append('(')
        elif i == '[':
            arr.append('[')
        elif i == ')':
            if arr:
                if arr[-1] == '(':
                    arr.pop()
                else:
                    errorcount+=1
                    break
            else:
                errorcount+=1
                break 
        elif i == ']':
            if arr:
                if arr[-1] == '[':
                    arr.pop()
                else:
                    errorcount+=1
                    break
            else:
                errorcount+=1
                break 
        
    if errorcount == 0 and len(arr)==0:
        print("yes")
    else:
        print("no")


        
        
        
 