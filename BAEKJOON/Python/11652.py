import sys

now = []

for i in range(int(sys.stdin.readline().strip())):
    name, action = map(str,sys.stdin.readline().split())

    if action =="enter":
        now.append(name)
    if action =="leave":
        now.remove(name)

now.sort()
now.reverse()

for i in now:
    print(i)