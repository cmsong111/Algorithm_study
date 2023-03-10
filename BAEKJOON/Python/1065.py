standard_input = """210"""

a = int(input())

def check(a:int):
    arr = []
    while a > 0:
        arr.append(a%10)
        a = a//10
    
    if len(arr) == 1:
        return True
    
    gap = arr[0] - arr[1]
    
    for i in range(len(arr)-1):
        if arr[i] - arr[i+1] != gap:
            return False
    return True


result = 0
for i in range(1, a+1):
    if check(i):
        result += 1


print(result)

