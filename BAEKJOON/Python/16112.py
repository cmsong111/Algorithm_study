import sys

excount, maxactive = map(int,sys.stdin.readline().split())

exparr = list(map(int,sys.stdin.readline().split()))
exparr.sort()
#경험치 합계
expsum = 0
nowactiva = 0

for i in range(excount):
    
    expsum += (nowactiva)*exparr[i]
    if nowactiva != maxactive:
        nowactiva+=1

    
print(expsum)