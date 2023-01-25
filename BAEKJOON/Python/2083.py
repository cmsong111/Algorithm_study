standard_input = """Joe 16 34
Bill 18 65
Billy 17 65
Sam 17 85
# 0 0"""

while(True):
    name, age, weight = input().split()
    if name == "#":
        break
    if int(age) > 17 or int(weight) >= 80:
        print(name + " Senior")
    else:
        print(name + " Junior")