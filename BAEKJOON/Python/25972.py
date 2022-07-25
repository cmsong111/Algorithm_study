import sys

def check(a):
    
    if 6 <= len(a) and len(a) <= 9:
        print("yes")
    else:
        print("no")
    


count = int(sys.stdin.readline().rstrip())

for i in range(count):
    target = sys.stdin.readline().rstrip()
    check(target)