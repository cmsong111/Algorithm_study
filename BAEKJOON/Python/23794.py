a = int(input())

print("@"*a,"@@",sep="")

for i in range(a):
    print("@",end="")
    print(" "*a,end="")
    print("@")
    
print("@"*a,"@@",sep="")
