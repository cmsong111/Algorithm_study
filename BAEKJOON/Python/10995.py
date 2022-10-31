standard_input = "6"

target = int(input())

for i in range(target):
    for ii in range(target):

        if i % 2 == 0:
            print("* ", end="")
        else:
            print(" *", end="")

    print()
