standard_input = "A+B"

input_str = input()

stack = []

# 후위 표기식으로 변환

# +, -, *, /, (, ) 6개의 경우가 있음



for i in input_str:
    if i.isalpha():
        print(i, end='')
    elif i == '(':
        stack.append(i)
    elif i == ')':
        while stack and stack[-1] != '(':
            print(stack.pop(), end='')
        stack.pop()
    
    elif i == '*' or i == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            print(stack.pop(), end='')
        stack.append(i)

    elif i == '+' or i == '-':
        while stack and stack[-1] != '(':
            print(stack.pop(), end='')
        stack.append(i)
    
    
    

while stack:
    print(stack.pop(), end='')