N,K = map(int, input().split())


# 올림픽 점수 입력
# 1: 국가번호, 2: 금메달, 3: 은메달, 4: 동메달, 5: 순위
score = []
for i in range(N):
    score.append(list(map(int, input().split())))


# 정렬
score.sort(key=lambda x: (x[1],x[2],x[3]) ,reverse=True)


idx = [score[i][0] for i in range(N)].index(K)

# K국가의 순위 출력
for i in range(N):
    if score[idx][1:] == score[i][1:]:
        print(i+1)
        break

