standard_input ="""2
4 4
10 1 100 10
1 2
1 3
2 4
3 4
4
8 8
10 20 1 5 8 7 1 43
1 2
1 3
2 4
2 5
3 6
5 7
6 7
7 8
7"""

from collections import deque

import sys

# 백준 제출 시 주석 해제
# input = sys.stdin.readline


def solution():
    # N: 건물의 갯수, K: 건물간의 건설순서규칙의 총 개수
    N,K = map(int,input().split())
    # 건물당 건설에 걸리는 시간
    build_time = [0] + list(map(int,input().split()))
    # 진입 차수
    indegree = [0] * (N+1)
    # 건설순서규칙
    build_rule = [[] for _ in range(N+1)]
    for i in range(K):
        X,Y = map(int,input().split())
        build_rule[X].append(Y)    
        indegree[Y]+=1

    # 건설 하고자 하는 건물
    target = int(input())
    # 각 건물당 건설에 걸리는 시간
    time = [0] * (N+1)


    # 위상 정렬
    queue = deque()

    # 시작 포인트
    for i in range(1,N+1):
        if indegree[i] == 0:
            queue.append(i)
            time[i] = build_time[i]
    
    while queue:
        start = queue.popleft()

        for destination in build_rule[start]:
            time[destination] = max(build_time[destination] + time[start] ,time[destination] )

            indegree[destination] -=1

            if indegree[destination] == 0:
                queue.append(destination)
    

    print(time[target])
    
testCase = int(input())

for _ in range(testCase):
    solution()


