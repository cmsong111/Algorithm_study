standard_input = """10 10
1 6 3 2 7 9 8 4 10 5"""

circleCount, targetCount = map(int, input().split())

targetArr = list(map(int, input().split()))


circle = list(range(1, circleCount+1))


result = 0

for target in targetArr:
    #print("타겟: ",target)
    index = circle.index(target)
    #print("타켓의 index: ",index)

    circleLeft = circle[:index]
    circleRight = circle[index+1:]

    #print(circleLeft,target,circleRight)

    #print(index, circleCount-index)

    if (index < circleCount-index):
        circle = circleRight.copy()
        circle.extend(circleLeft)
        result += index
        #print(index,"칸 이동함A")
    else:
        circle = circleRight.copy()
        circle.extend(circleLeft)
        result += circleCount-index
        #print(circleCount-index,"칸 이동함B")

    circleCount -= 1

    #print("현재 큐",circle)
    #print()

print(result)
