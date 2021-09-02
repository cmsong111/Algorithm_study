#3,6,9 입력시 참
def clab(a):
    if a == 3:
        return True
    elif a == 6:
        return True
    elif a == 9:
        return True
    else:
        return False
            
x= int(input())

for i in range(1,x+1):
    if clab(i // 10): 
        if clab(i % 10): #10, 1의 자리수가 참이면
            print("XX",end=" ")
        print("X",end=" ") #10의자리수만 참이면 X
    elif clab(i % 10):# 1의 자리수가 참이면 X
        print("X",end=" ")
    else:
        print(i,end =" ")# 나머지 숫자 출력
            
