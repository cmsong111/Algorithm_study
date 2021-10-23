def go (a,b):
    temp = a%b
    while(temp !=0):
        a = b
        b = temp
        temp = a%b
    return b

a,b = map(int,input().split())

gbc = go(max(a,b),min(a,b))

print(gbc)
print(a*b//gbc)
