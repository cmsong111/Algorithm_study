standard_input = """5"""

a = int(input())

for i in range(a):
    print(" " * (i),end="")
    print("*"*((a-i)*2-1))