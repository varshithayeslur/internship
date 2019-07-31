from functools import reduce



ls=[1,2,3,4,5,6,7,8,9]

sum=reduce(lambda x,y:x+y,ls)

print(sum)