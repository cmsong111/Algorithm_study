import sys

#input = sys.stdin.readline

standard_input = """6
10
20
15
25
10
20
"""

# 변수 선언
count = int(input())
arr = []
result = []

# 입력
for i in range(count):
    arr.append(int(input()))

if count < 3:
    print(sum(arr))
else:
    # DP 초기값 제작
    result.append(arr[0])
    result.append(arr[0] + arr[1])
    result.append(max(arr[1] + arr[2], arr[0] + arr[2]))

    # DP 돌리기
    for i in range(3, count):
        result.append(
            max((result[i-3] + arr[i] + arr[i-1]), (result[i-2] + arr[i])))

    # 정답 출력
    print(result[-1])
