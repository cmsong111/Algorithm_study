#import sys

#input = sys.stdin.readline

standard_input = """3
-4000
0
4000
"""

arr = []
count = int(input())
for i in range(count):
    arr.append(int(input()))

# 산술평균
# print("\n산술평균")
print(round(sum(arr)/count))

# 중앙값
# print("\n중앙값")
arr.sort()
print(arr[round(count/2)])

# 최빈값
# print("\n최빈값")

count_arr = {}
for i in arr:
    if i not in count_arr:
        count_arr[i] = 1
    else:
        count_arr[i] += 1
test = sorted(count_arr.items(), key=lambda x: x[1], reverse=True)


if len(test) >= 2 and test[0][1] == test[1][1]:
    print(test[1][0])
else:
    print(test[0][0])

#범위
# print("\n범위")
print(arr[count-1] - arr[0])



