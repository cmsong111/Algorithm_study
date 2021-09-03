a,b,c = map(int, input().split())

#while에 or 여러개 쓸때 괄호 안쓰면 적용 되는듯.
#i=1
#while(i%a!=0 or i%b!=0 or i%b!=0):
#    i +=1
#
#print(i)


d = 1
while d%a!=0 or d%b!=0 or d%c!=0 :
  d += 1
print(d)
