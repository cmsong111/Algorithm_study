import sys

# input = sys.stdin.readline

standard_input = """2
1
3
2
3
"""

# 초기 arr 생성
arr = []
arr.append([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])


testCase = int(input())

for i in range(testCase):
    K = int(input())
    N = int(input())

    # 층수를 더 높여
    if (len(arr) < K+1):
        for i in range(K - len(arr) + 2):
            arr.append([1]*14)

    # 조작
    for i in range(1, K+1):
        for ii in range(1, 14):
            if arr[i][ii] == 1:
                arr[i][ii] = arr[i-1][ii] + arr[i][ii-1]

    # 현재 테이블 출력
    for i in range(K+1):
        for ii in range(14):
            print(arr[i][ii], end="\t")
        print()

    # 결과 출력
    print(arr[K][N-1])
