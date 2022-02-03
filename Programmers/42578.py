def solution(clothes):
    clothes_len = len(clothes)
    arr_dict = {}
    for i in range(clothes_len):
        if clothes[i][1] not in arr_dict:
            arr_dict[clothes[i][1]] = 1
        else:
            arr_dict[clothes[i][1]] += 1
        
    arr_dict_len = len(arr_dict)
    
    answer = 0

    keyList = arr_dict.keys()
    for i in range(arr_dict_len):
        temp = 1
        for item in keyList :
            print("값",arr_dict[item])
            temp *= arr_dict[item]
        print("차",temp)
        answer += temp
   
    return answer



print("정답:",solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print("정답:",solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))