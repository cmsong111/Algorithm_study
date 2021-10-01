compare_list_1 = []
for x in range(25):
        compare_list_1.append(list("WB"*25))
        compare_list_1.append(list("BW"*25))

compare_list_2 = []
for x in range(25):
        compare_list_2.append(list("BW"*25))
        compare_list_2.append(list("WB"*25))

count1 = 0
count2 = 0

for x in range(50):
    for y in range(50):
        if compare_list_2[x][y] == compare_list_1[x][y]:
            count1 = count1 +1
        elif compare_list_2[x][y] != compare_list_1[x][y]:
            count2 = count2 +1
print(count1)
print(count2)