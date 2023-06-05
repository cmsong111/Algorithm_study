standard_input = """6
bitaro
"""

arr = {'a', 'e', 'i', 'o', 'u'}

result_arr = []
a_len = int(input())
a = input()

result = 0

for i in a:

    if i in arr:
        result_arr.append(i)


print(len(result_arr))
