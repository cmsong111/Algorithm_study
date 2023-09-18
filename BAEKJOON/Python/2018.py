standard_input = "15"

N = int(input())

end = 0
sum = 0
count = 0

for i in range(N):
    while end < N and sum < N:
        end += 1
        sum += end
    if sum == N:
        count += 1
    sum -= i + 1

print(count)
    
    