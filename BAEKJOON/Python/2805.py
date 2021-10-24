n,m = map(int, input().split())
tree = list(map(int,input().split()))

l = 0
r = max(tree)

mid = (l+r+1)//2

while l != r:
    sum = 0
    for t in tree:
        tmp = t - mid
        if tmp > 0:
            sum += (t-mid)
    if sum >= m:
        l = mid
    else:
        r = mid-1
    mid = (l+r+1)//2
    
print(mid)
