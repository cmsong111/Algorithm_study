n,l,h = map(int,input().split())
scores = list(map(int,input().split()))

scores.sort()

print( sum(scores[l:n-h]) / (n-l-h))