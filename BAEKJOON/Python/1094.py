standard_input = "48"

x = int(input())

# x 이진수 변환
x = bin(x)

# 0b 제거
x = x[2:]

# 숫자 다 더하기
result = 0

for i in x:
    result += int(i)

print(result)
