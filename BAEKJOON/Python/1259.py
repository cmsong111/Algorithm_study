while(1):
    num = input()
    if num == "0":
        break
    else:
        count = len(num)
        temp = 0
        for i in range(count//2):
            if num[i] != num[count-i-1]:
                print("no")
                break
            else:
                temp += 1
        if temp == count//2:
            print("yes")
