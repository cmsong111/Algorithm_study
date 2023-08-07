scoreboard = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}


def get_score(score):
    return scoreboard[score]


score = []
score_sum = 0
score_len = 0

for i in range(20):
    a, b, c = input().split()
    score.append([a, float(b), c])

for i in range(20):
    if score[i][2] == "P":
        continue

    score_sum += score[i][1] * get_score(score[i][2])
    score_len += score[i][1]


print("%.6f" % (score_sum / score_len))
