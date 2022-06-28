import sys
testcase = int(sys.stdin.readline().rstrip())

for i in range(testcase):
    arr = list(map(int, sys.stdin.readline().split()))
    count = arr[0]
    del arr[0]
    arr.sort()
    gap = 0
    for ii in range(count-1):
        if gap < arr[ii+1] - arr[ii]:
            gap = arr[ii+1] - arr[ii]
    print("Class", i+1)
    print("Max ", arr[count-1], ", Min ",
          arr[0], ", Largest gap ", gap, sep="")
