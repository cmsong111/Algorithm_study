count = int(input())

for i in range(1,count+1):
    print("*"*(i)," "*(count-i)," "*(count-i),"*"*(i),end="",sep="")
    print()
    
for i in range(count-1,0,-1):
    print("*"*(i)," "*(count-i)," "*(count-i),"*"*(i),end="",sep="")
    print()
    
