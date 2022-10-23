import datetime

standard_input = "3 14"


days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
month, day = map(int, input().split())
result = days[datetime.date(year=2007, month=month, day=day).weekday()]
print(result)
