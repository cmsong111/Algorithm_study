def super (a,b):
    if a == 1 or b == 1:
        return 1
    if a < b:
        small = a
    else:
        small = b

    for i in range(int(small),0,-1):
        if a % i == 0:
            if b % i == 0:
                return i
        if i == 1:
            return 1



how = int(input())

for i in range(how):
    #변수 초기화 및 선언
    a,b = map(int,input().split())
    result = a*b
    lis=[]
    #무한 반복~
    while(1):
        num = super(a,b)
        #최소 공배수가 1이면
        if num == 1:
            break
        #아니면
        lis.append(num)
        a = a/num
        b = b/num
    
    for i1 in range(len(lis)):
        result = result // lis[i1]
    
    print(result)