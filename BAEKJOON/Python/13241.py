standard_input = """121 199
"""

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


a,b= map(int,input().split())

print(int(a*b/gcd(a,b)))