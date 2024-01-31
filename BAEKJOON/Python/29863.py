standard_input = """0
7"""

night = int(input())
awaik = int(input())


if 19 < night and night < 24:
    print(awaik + 24 - night)
else:
    print(awaik - night)
