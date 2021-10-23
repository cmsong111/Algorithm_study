def check (a,b):
    for i in range(8):
        if a[i] != b[i]:
            return False
    return True


lis = list(map(int,input().split()))
temp1 = list(lis)
temp2 = list(lis)
temp1.sort()
temp2.sort()
temp2.reverse()


if check(lis,temp1):
    print("ascending")
elif check(lis,temp2):
    print("descending")
else:
    print("mixed")
