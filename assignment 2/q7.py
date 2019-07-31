from functools import reduce



ls=[1,2,3,4,5,6,7,8,9]

even=list(filter(lambda x:x%2==0,ls))
list1=list(map(lambda x:x*x,even))
sums=reduce(lambda x,y:x+y,list1)

print(sums)