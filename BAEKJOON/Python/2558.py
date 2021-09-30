first_number = int(input())
second_number = int(input())

x=len(str(second_number))

for i in range(x,0,-1):
    print(int(str(second_number)[i-1])*first_number)

print(first_number*second_number)