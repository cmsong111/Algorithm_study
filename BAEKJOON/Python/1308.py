import datetime


standard_input = """1 1 1
1001 1 1
"""

day1_input = list(map(int, input().split()) )
day2_input =  list(map(int, input().split()) )


day1 = datetime.datetime(year=day1_input[0], month=day1_input[1], day=day1_input[2])

day2 = datetime.datetime(year=day2_input[0], month=day2_input[1], day=day2_input[2])


if (day2 - day1).days >= 365243:
    print("gg")

else:
    print("D-%d" % (day2 - day1).days)

    