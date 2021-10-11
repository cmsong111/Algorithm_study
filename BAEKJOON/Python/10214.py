num = int(input())

for i in range(num):
    scoreboard = [0,0]
    for i in range(9):
        Y,K = map(int,input().split())
        scoreboard[0] = scoreboard[0] + Y
        scoreboard[1] = scoreboard[1] + K
    if scoreboard[0] > scoreboard[1]:
        print("Yonsei")
    elif scoreboard[0] < scoreboard[1]:
        print("Korea")
    elif scoreboard[0] == scoreboard[1]:
        print("Draw")
    