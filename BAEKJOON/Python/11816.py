a = input()

if a.startswith('0x'):
    print(int(a, 16))

elif a.startswith('0'):
    print(int(a, 8))
else:
    print(int(a, 10))
