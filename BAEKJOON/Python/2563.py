standard_input = """3
3 7
15 7
5 2
"""

a = []


for i in range(100):
    a.append([0]*100)

paper_count = int(input())

for i in range(paper_count):
    x, y = map(int, input().split())
    for ii in range(x, x+10):
        for iii in range(y, y+10):
            a[ii][iii] = 1


print(sum(a, []).count(1))
