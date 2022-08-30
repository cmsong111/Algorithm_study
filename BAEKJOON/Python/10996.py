standard_input = """3"""

a = int(input())
num = 0

for i in range(a*2):
    for ii in range(a):
        if num % 2 == 0:
            print("*", end="")
        else:
            print(" ", end="")
        num += 1
    if ii % 2 == 1:
        num += 1
    
    print()
