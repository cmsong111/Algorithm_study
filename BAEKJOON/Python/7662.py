import heapq
import sys

input = sys.stdin.readline


for testcase in range(int(input())):

    count = int(input())
    visited = [False] * count

    max_arr = []
    min_arr = []

    for ii in range(count):
        a, b = map(str, input().split())
        b = int(b)
        flag = 0
        #print(ii, "번째")
        if a == "I":
            heapq.heappush(max_arr, (-b, ii))
            heapq.heappush(min_arr, (b, ii))
            visited[ii] = True
            #print("추가됨",b,"\nvisited[",ii,"] =",visited[ii])


        #최소힙 뺴기
        elif a == "D" and b == -1 and min_arr:
            #print(-1)
            target = heapq.heappop(min_arr)
            #print("이거 나옴",target,visited[target[1]])
            if visited[target[1]] == False:
                #print("아니네요")
                while(visited[target[1]]==False and min_arr):
                    target = heapq.heappop(min_arr)
                    #print("한번더!",target)

            
          
            visited[target[1]] = False
            #print("최소 힙 제거됨,",target,"\nvisited[",target[1],"] =",visited[target[1]])
           


        #최대힙 뺴기
        elif a == "D" and b == 1 and max_arr:
            #print(1)
            target = heapq.heappop(max_arr)
            #print("이거 나옴",target,visited[target[1]])
            if visited[target[1]] == False:
                #print("아니네요")
                while(visited[target[1]]==False and max_arr):
                    target = heapq.heappop(max_arr)
                    #print("한번더!",target)

            
            visited[target[1]] = False
            #print("최대 힙제거됨,",target,"\nvisited[",target[1],"] =",visited[target[1]])


        #진짜 만약에 리스트가 비어버린다면..? 다 삭제
        if not max_arr or not min_arr:
            max_arr = []
            min_arr = []



        # print("최대 힙:", max_arr)
        # print("최소 힙:", min_arr)
        # print("\n")

    result_arr = []
    for ii in max_arr:
        if visited[ii[1]] == True:
            result_arr.append(-ii[0])
    
    for ii in min_arr:
        if visited[ii[1]] == True:
            result_arr.append(ii[0])

    #print(result_arr)
    if not result_arr:
        print("EMPTY")
    else:
        print(max(result_arr),min(result_arr))

