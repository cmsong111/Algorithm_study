standard_input ="""5
Lionel Cosgrove
Alice
Columbus and Tallahassee
Shaun and Ed
Fido
"""

testCase = int(input())

for i in range(testCase):
    temp = input()
    print(i+1,". ",temp,sep="")