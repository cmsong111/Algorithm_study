standard_input = """12
1 2
1 3
2 4
3 5
3 6
4 7
4 8
5 9
5 10
6 11
6 12
"""

import sys
sys.setrecursionlimit(10**6)
#input = sys.stdin.readline

node_count = int(input())
visited = [False] * (node_count+1)
result = [0] * (node_count+1)

tree = [[] for _ in range(node_count+1)]

for i in range(node_count-1):
    start, end = map(int, input().split())
    tree[start].append(end)
    tree[end].append(start)

def DFS(start):
    visited[start] = True
    for i in tree[start]:
        if not visited[i]:
            result[i] = start
            DFS(i)
        
DFS(1)

for i in result[2:]:
    print(i)



