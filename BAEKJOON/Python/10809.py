S = input()

num = len(S)

count = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]

for i in range(num-1,-1,-1):
    a = ord(S[i])-97
    count[a] = i

for i in range(26):
    print(count[i],end=" ")

    
