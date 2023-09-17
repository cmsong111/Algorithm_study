standard_input = """ababababa
ababa"""


entire_str = input()
sub_str = input()

cnt = 0

while(sub_str in entire_str):
    cnt += 1
    entire_str = entire_str[entire_str.find(sub_str)+len(sub_str):]

print(cnt)