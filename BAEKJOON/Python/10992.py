import sys

# input = sys.stdin.readline

standard_input = """6"""

count = int(input())

print(" "*(count-1), end="")
print("*")

for i in range(2, count):
    print(" "*(count-i), end="")
    print("*", end="")
    print(" "*(i*2-3), end="")
    print("*")

if count != 1:
    print("*"*(count*2-1))
