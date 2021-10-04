#처음 값 저장 및 변수 설정
a= int(input())
temp = a
count = 1

while(True):
    #0 예외 처리
    if a == 0:
        print("1")
        break

    #합 구하기
    if temp < 10:
        sum = temp
    elif temp >= 10:
        sum = temp//10 + temp%10

    #같으면 함수 종료
    if a == sum:
        print(count)
        break

     #카운트 증가
    count = count + 1
     #숫자 변경
    if temp < 10:
        temp = temp*10 + temp
    elif temp >= 10:
        temp = ((temp%10)*10 + (sum%10)) 


    if count > 1000000:
        print("ERROR")
        break