while(1):
    temp = input()
    if temp == "END":
        break
    else:
        for i in range(len(temp)-1,-1,-1):
            print(temp[i],end="")
        print()