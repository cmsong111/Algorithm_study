standard_input ="14"

N = int(input())

answer = 0

while N > 0:
    if N % 5 == 0:
        answer += N // 5
        break
    else:
        N -= 2
        answer += 1

if N < 0:
    answer = -1

print(answer)