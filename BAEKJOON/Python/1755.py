

a,b = map(int,input().split())
arr = list(range(a,b+1,1))
temp= []
for i in arr:
    string = ""
    tmp = str(i)
    for ii in range(len(tmp)):
        if tmp[ii] == "1":
            string = string + "one "
        elif tmp[ii] == "2":
            string = string + "two "
        elif tmp[ii] == "3":
            string = string + "three "
        elif tmp[ii] == "4":
            string = string + "four "
        elif tmp[ii] == "5":
            string = string + "five "
        elif tmp[ii] == "6":
            string = string + "six "
        elif tmp[ii] == "7":
            string = string + "seven "
        elif tmp[ii] == "8":
            string = string + "eight "
        elif tmp[ii] == "9":
            string = string + "nine "
        elif tmp[ii] == "0":
            string = string + "zero "
            
    temp.append(string)

temp.sort()
result = []

for i in range(len(temp)):
    listtemp = list(map(str, temp[i].split()))
    temp2 = ""
    for ii in range(len(listtemp)):
        if listtemp[ii] == "zero":
            temp2 += "0"
        elif listtemp[ii] == "one":
            temp2 += "1"
        elif listtemp[ii] == "two":
            temp2 += "2"
        elif listtemp[ii] == "three":
            temp2 += "3"
        elif listtemp[ii] == "four":
            temp2 += "4"
        elif listtemp[ii] == "five":
            temp2 += "5"
        elif listtemp[ii] == "six":
            temp2 += "6"
        elif listtemp[ii] == "seven":
            temp2 += "7"
        elif listtemp[ii] == "eight":
            temp2 += "8"
        elif listtemp[ii] == "nine":
            temp2 += "9"

    result.append(temp2)

count = 0
for i in range(len(result)):
    
    print(result[i],end=" ")
    count +=1
    if count == 10:
        print()
        count = 0