import sys

def solution(clothes):
    clothes_len = len(clothes)
    arr_dict = {}
    answer = 1

    for i in range(clothes_len):
        if clothes[i][1] not in arr_dict:
            arr_dict[clothes[i][1]] = 1
        else:
            arr_dict[clothes[i][1]] += 1
        
    arr_dict_len = len(arr_dict)
    

    keyList = arr_dict.keys()

    for item in keyList :
        answer *= (arr_dict[item]+1)

            
    answer -= 1


    return answer

clothes = []
clothes_len = int(sys.stdin.readline().rstrip())

for i in range(clothes_len):
    tmp = (int(sys.stdin.readline().rstrip()))
    temp = []
    for ii in range(tmp):
        temp.append(list(sys.stdin.readline().split()))
    print(solution(temp))

