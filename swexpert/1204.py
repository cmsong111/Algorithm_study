T = int(input())

for testCase in range(1, T+1):
    case = int(input())
    print(f"#{testCase}", end=" ")
    result = {}
    arr = list(map(int, input().split()))

    for i in arr:
        if i not in result:
            result[i] = 1
        else:
            result[i] += 1

    # 정렬 후 최고값 출력
    print(sorted(result.items(), key=lambda x: x[1], reverse=True)[0][0])
