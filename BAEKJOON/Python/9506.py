while(1):
    a = int(input())
    if a == -1:
        break
    else:
        lis = []
        for i in range(1,a,1):
            if a % i == 0:
                lis.append(i)
        if sum(lis) == a:
            print(a,"= ",end="")
            for i in range (len(lis)):
                print(lis[i],end="")
                if i != (len(lis)-1):
                    print(" + ",end="")
            print()
        if sum(lis) != a:
            print(a,"is NOT perfect.")
