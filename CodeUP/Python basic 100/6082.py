def clab(a):
    if a == 3:
        return True
    elif a == 6:
        return True
    elif a == 9:
        return True
    else:
        return False
            
x= int(input())

for i in range(1,x+1):
    if clab(i // 10):
        if clab(i % 10):
            print("XX",end=" ")
        print("X",end=" ")
    elif clab(i % 10):
        print("X",end=" ")
    else:
        print(i,end =" ")
            
