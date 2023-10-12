standard_input = """5
-1 0 0 1 1
2"""


node_len = int(input())
node_list = list(map(int, input().split()))
delete_node = int(input())


graph = [[] for _ in range(node_len)]

for i in range(node_len):
    if node_list[i] == -1:
        continue
    graph[node_list[i]].append(i)

# find root
start = 0
for i in range(node_len):
    if node_list[i] == -1:
        start = i
        break



#delete node
for i in range(node_len):
    if delete_node in graph[i]:
        graph[i].remove(delete_node)
    
graph[delete_node] = []


result = 0
visited = [False] * node_len

def dfs(start, graph):
    visited[start] = True
    global result

    for i in graph[start]:
        if not visited[i]:
            dfs(i, graph)
    
    if len(graph[start]) == 0:
        result += 1


dfs(start, graph)

if delete_node == start:
    result = 0



print(result)

