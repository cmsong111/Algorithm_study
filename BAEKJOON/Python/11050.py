def fac(a):
    if (a > 1):
        return a * fac(a - 1)
    else:
        return 1

x,y = map(int,input().split())

ans = int(fac(x) / (fac(y)*fac(x-y)))


print(ans)