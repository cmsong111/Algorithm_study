import sys

count = int(sys.stdin.readline().strip())

result = {}
best_book = []

for i in range(count):
    temp = sys.stdin.readline().strip()
    if temp in result:
        result[temp] += 1
    else:
        result[temp] = 1

max_num = max(result.values())

for bookname, value in result.items():
    if value == max_num:
        best_book.append(bookname)

best_book.sort()

print(best_book[0])   