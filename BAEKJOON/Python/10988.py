a = input()
count = len(a)

if count % 2 == 0:
    front = a[:count//2]
    back = a[count//2:]
else:
    front = a[:count//2]
    back = a[count//2+1:]


if(front == back[::-1]):
    print("1")
else:
    print("0")