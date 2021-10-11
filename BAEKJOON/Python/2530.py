time, min, second = map(int,input().split())
add_second = int(input())

second = second + add_second

while(second >= 60):
    second = second - 60
    min = min + 1

while(min >= 60):
    min = min - 60
    time = time +1

while(time >= 24):
    time = time - 24
    
print(time,min,second)