standard_input = "((((("

# () : 2
# [] : 3
# (X) : 2 * X
# [X] : 3 * X

str = input()

stack = []

for i in str:
    try:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if stack[-1] == "(":
                stack.pop()
                stack.append(2)
            else:
                temp = 0
                while stack[-1] != "(":
                    temp += stack.pop()
                stack.pop()
                stack.append(temp * 2)
        elif i == "]":
            if stack[-1] == "[":
                stack.pop()
                stack.append(3)
            else:
                temp = 0
                while stack[-1] != "[":
                    temp += stack.pop()
                stack.pop()
                stack.append(temp * 3)

    except:
        print(0)
        exit()


if "(" in stack or "[" in stack or ")" in stack or "]" in stack:
    print(0)

else:
    print(sum(stack))
