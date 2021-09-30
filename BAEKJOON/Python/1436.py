def countup(name):
    name= name+1
    while(str(666) not in str(name)):
        name = name+1
    return(name)


a= int(input())

name = 1


for i in range(a):
    name = countup(name)



print(name)
    
