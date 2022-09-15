import sys
standard_input = """11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14"""


#input = sys.stdin.readline

count = int(input())
arr = []

for i in range(count):
    arr.append(list(map(int, input().split())))


arr.sort()

result_arr = []

for i in arr:
    flag = 0
    print("추가할 시간: ", i)

    for ii in range(len(result_arr)):
        #빈 시간대가 있을 때
        print(result_arr[ii])
        if i[0] >= result_arr[ii][0]:
            print("Okay")
            result_arr[ii][0] = i[1]
            result_arr[ii][1] += 1
            flag += 1
            break
    #빈 시간대가 없을 때
    if flag == 0:
        result_arr.append([i[1], 1])
        print("회의실 추가")
    
    result_arr = sorted(result_arr, key= lambda x:x[1], reverse= True)

    #내 생각이 맞는지 확인
    print("result_arr")
    for i in result_arr:
        print(i, end="\t")
    print()
    print("\n\n\n")




print(result_arr[0][1])