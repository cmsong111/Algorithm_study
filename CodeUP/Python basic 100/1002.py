import sys

num = int(input())

for i in range(num):
    #변수선언
    x1 = 0;y1 = 0;r1 = 0;x2 = 0;y2 = 0;r2 = 0

    x1,y1,r1,x2,y2,r2 = map(int, sys.stdin.readline().split())
   
    #원이 일치 할때
    if x1 == x2 and y1 == y2 and r1==r2:
        print("-1")
    #점이 하나일때
    elif ((x2-x1)**2+(y2-y1)**2)==(r1+r2)**2:
        print("1")
    #점이 내접하는데 점이 하나일때
    elif ((x2-x1)**2+(y2-y1)**2) == (max(r1,r2)-min(r1,r2))**2 :
        print("1")
    #점두 원이 서로 떨어져 있고 만나지 않을 때, 답은 0
    elif ((x2-x1)**2+(y2-y1)**2) > (r1+r2)**2:
        print("0")
    #한 원이 다른 원의 내부에 있고 두 원이 만나지 않을 때, 답은 0. 꼭 두 원의 중심이 같을 필요는 없습니다!
    elif ((x2-x1)**2+(y2-y1)**2) < (max(r1,r2)-min(r1,r2))**2 :
        print("0")
    #나머지는 전부 2임
    else:
        print("2")