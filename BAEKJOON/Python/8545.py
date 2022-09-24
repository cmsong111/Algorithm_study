standard_input = "abc123"
a = input()

for i in range(len(a), 0, -1):
    print(a[i-1], end="")
