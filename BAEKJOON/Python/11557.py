test_case = int(input())
for i in range(test_case):
    num = int(input())
    lis = []
    score = []
    for i in range(num):
        lis.append(list(map(str,input().split())))
    for i in range(num):
        score.append(int(lis[i][1]))
    print(lis[(score.index(max(score)))][0])