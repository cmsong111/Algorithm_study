a,b = map(int,input().split())

if b >= 45:
    print(a,b-45)
else:
    if a == 0:
        print(int(23), b+15)
    else:
        print(a-1,b+15)
