a = int(input())
result = 0
for i in range(a):
    check = input()
    check_len = len(check)
    check_list = []
    count = 0
    
    for i in range(check_len):
        if check[i] not in check_list:
            check_list.append(check[i])
            count += 1
        elif check[i] in check_list:
            if check[i] != check_list[count-1]:
                break
        
        if i == (check_len-1):
            result = result + 1
    
print(result)

         