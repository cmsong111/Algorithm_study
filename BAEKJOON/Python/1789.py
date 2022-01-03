import sys

target = int(sys.stdin.readline().strip())
value = 0

for i in range(1,100000):
    value +=i
    if value > target:
        print(i-1)
        break

print(value)
