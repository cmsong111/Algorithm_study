standard_input = """3
3 4 12"""


N = int(input())
arr = list(map(int, input().split()))

max_num = max(arr)

score = [0] * (max_num + 1)


# 카드 여부 확인
card_bool = [False] * (max_num + 1)
for i in arr:
    card_bool[i] = True


# 에라스토스 응요한 카드 점수 계산
for i in arr:
    for j in range(i*2, max_num + 1, i):
        if card_bool[j]:
            score[i] += 1
            score[j] -= 1


for i in arr:
    print(score[i], end=' ')
