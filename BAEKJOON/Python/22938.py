x1,y1,r1 = map(int,input().split())
x2,y2,r2 = map(int,input().split())

xy = (x1-x2)**2 + (y1-y2)**2
rr = (r1+r2)**2
if xy < rr:
    print("YES")
else:
    print("NO")
