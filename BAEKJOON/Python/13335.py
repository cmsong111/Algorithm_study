def solution(bridge_length, weight, truck_weights):
    answer = 0 
    now_bridge_weights = [0]*bridge_length
    #상황을 보기 위해서 넣은 리스트 clear_car임 제출시 삭제
    clear_car = []
    while(now_bridge_weights):
        temp = now_bridge_weights.pop(0)
        #제출시 아래 if 절삭제
        if temp != 0: 
            clear_car.append(temp)

        if truck_weights:
            if sum(now_bridge_weights)+truck_weights[0] <= weight:
                if truck_weights:
                    now_bridge_weights.append(truck_weights.pop(0))
            else:
                now_bridge_weights.append(0)
        answer += 1
        
    
    return answer

x1,x2,x3 = map(int,input().split())
temp = list(map(int, input().split()))


bridge_length = x2
weight = x3
truck_weights = temp
print(solution(bridge_length, weight, truck_weights))


