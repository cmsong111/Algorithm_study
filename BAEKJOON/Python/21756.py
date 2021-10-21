def go (array):
    if len(array)==1:
        return array[0]
    else:
        count = 0
        for i in range(0,len(array),2):
            array[i]=0
            count +=1

        for i in range(count):
            array.remove(0)
                
        return go(array)

    

lis = list(range(1,int(input())+1,1))

print(go(lis))
