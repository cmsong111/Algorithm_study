standard_input = """4
3
10
21
10
3
20
10
10
3
10
10
10
4
15
15
15
45"""

import sys

# input = sys.stdin.readline

T = int(input())

for _ in range(T):

    N = int(input())
    votes = []
    for _ in range(N):
        votes.append(int(input()))

    max_vote = max(votes)
    if votes.count(max_vote) > 1:
        print("no winner")
    else:
        if max_vote > sum(votes) // 2:
            print("majority winner", votes.index(max_vote) + 1)
        else:
            print("minority winner", votes.index(max_vote) + 1)