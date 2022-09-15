standard_input = """5 20
99 101 1000 0 97
"""

size, peaple = map(int,input().split())

arr = list(map(int,input().split()))

size *= peaple

for i in arr:
    print(i-size,end= " ")