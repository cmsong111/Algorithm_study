n = int(input())

def sums(n):
    if n == 1:
        return(1)
    elif n == 2:
        return(2)
    elif n == 3:
        return(4)
    else:
        return sums(n-1) + sums(n-2) + sums(n-3) #규칙을 찾아내는게 중요!
        
for i in range(n):
    a = int(input())
    print(sums(a))