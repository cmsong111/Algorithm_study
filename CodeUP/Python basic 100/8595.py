import re

count = int(input())
lis = input()

numbers = re.findall("\d+", lis)

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

print(sum(numbers))