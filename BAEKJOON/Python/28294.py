standard_input = """10 0"""

T, S = map(int, input().split())


# T가 11이하이면 아침 시간,12 이상 16 이하이면 점심 시간, 그렇지 않으면 저녁 시간을 뜻한다.

# S가 1 이면 술과 함께 먹는 것을 의미하며, 0 이면 술 없이 초밥을 먹는 것을 의미한다.

time = "moring"
alcohol = "alcohol"

if T <= 11:
    time = "morning"
elif T >= 12 and T <= 16:
    time = "lunch"
else:
    time = "dinner"

if S == 1:
    alcohol = "alcohol"
else:
    alcohol = "no alcohol"


if alcohol == "alcohol" or time != "lunch":
    print(280)
elif time == "lunch" and alcohol == "no alcohol":
    print(320)