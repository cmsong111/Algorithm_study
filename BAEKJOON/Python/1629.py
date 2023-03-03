standard_input ="""10 11 12
"""

a,b,c = map(int, input().split())

def cal (a:int,b:int,c:int):
    if b == 0:
        return 1
    elif b == 1:
        return a%c
    
    if b%2 == 0:
        return cal(a,b//2,c)**2%c
    else:
        return cal(a,b//2,c)**2*a%c

print(cal(a,b,c))