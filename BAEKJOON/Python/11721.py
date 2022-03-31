a = input()
len_a=len(a)//10
for i in range(len_a):
    print(a[i*10:i*10+10])
print(a[len_a*10:])