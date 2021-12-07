import sys
count = int(input())

stringarr = sys.stdin.readline().strip()
score = [0,0]
for i in range(count):
    if stringarr[i] == "A":
        score[0] +=1
    elif stringarr[i] == "B":
        score[1] +=1
    

if score[0] == score[1]:
    print("Tie")
elif score[0] > score[1]:
    print("A")
elif score[0] < score[1]:
    print("B")
