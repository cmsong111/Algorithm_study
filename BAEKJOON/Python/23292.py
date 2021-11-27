birthday = input()
arrlist = []
result = []

count = int(input())

for i in range(count):
    temp = input()
    arrlist.append(temp)

arrlist.sort()


for i in range(count):
    temp = arrlist[i]
    year = (int(birthday[0])-int(temp[0]))**2 + (int(birthday[1])-int(temp[1]))**2 + (int(birthday[2])-int(temp[2]))**2 + (int(birthday[3])-int(temp[3]))**2
    month = (int(birthday[4])-int(temp[4]))**2 + (int(birthday[5])-int(temp[5]))**2
    day = (int(birthday[6])-int(temp[6]))**2 + (int(birthday[7])-int(temp[7]))**2
    result.append(year*month*day)
    
print(arrlist[result.index(max(result))])