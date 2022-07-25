str = input()

# str = "11101101"

target0 = 0
target1 = 0


zerosplit = str.split("0")
onesplit = str.split("1")

while("" in zerosplit):
    zerosplit.remove("")

while("" in onesplit):
    onesplit.remove("")

target0 = len(zerosplit)
target1 = len(onesplit)

print(min(target0,target1))