arr = list(input())
answer = 0
stack = []

for i in range(len(arr)):
    if arr[i] == '(':
        stack.append('(')
        
    else:
        if arr[i-1] == '(':
            stack.pop()
            answer += len(stack)
            
        else:
            stack.pop() 
            answer += 1 

print(answer)