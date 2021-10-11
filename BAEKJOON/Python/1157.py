alpha = input()
alpha = alpha.upper()

how_long = len(alpha)

count =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(how_long):
    count[int(ord(alpha[i]))-64] +=1
print("count",count)

count2 = list(count)
count2.sort()
count2.reverse()


if count2[0] == count2[1]:
    print('?')
else:
   big = max(count)
   count.index(big)
   print(chr(count.index(big)+64))
