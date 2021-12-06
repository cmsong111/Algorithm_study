count = int(input())

for i in range(count):
    print("@"*(count*5))

for i in range(count*3):
    print("@"*(count)," "*(count*3),"@"*(count),sep="")

for i in range(count):
    print("@"*(count*5))