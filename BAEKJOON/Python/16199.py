

standard_input ="""2005 12 31
2007 1 1"""

# input
year, month, day = map(int, input().split())
year2, month2, day2 = map(int, input().split())



# 만 나이
if month2 > month:
    print(year2 - year) 
elif month2 == month:
    if day2 >= day:
        print(year2 - year)
    else:
        print(year2 - year - 1)
else:
    print(year2 - year - 1)

# 세는 나이
print(year2 - year + 1)

# 연 나이
print(year2 - year)