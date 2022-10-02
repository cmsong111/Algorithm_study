standard_input = """3
5 10
7 23
42 56
"""

def gcd(a:int, b:int):
    big = max(a,b)
    small = min(a,b)
    
    while(small > 0):
        temp = big
        big = small
        small = temp%small

    return big

testCase = int(input())

for i in range(testCase):
    a,b = map(int,input().split())
    temp = gcd(a,b)
    print(a*b//temp,temp)