#팩토리얼 재귀함수
def factorial(num):
    if num >= 1:
        return (num * factorial(num-1))
    elif num == 0:
        return (1)
#메인함수
first_number = int(input())
result = factorial(first_number)
print(result)
