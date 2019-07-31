num=int(input("Enter the number"))
sum=0

while True:
    if sum>1 and sum<=9:
        break
    else:
        sum=0
        while True:
            if num==0:
                break
            sum=sum+(num%10)
            num=num//10
        print(sum)
        num=sum


'''or

tnum = num =int(input("enter the number"))
while num > 9:
    sum = (num %10 + num //10)
    num = sum
print(f"the sum of digits of {tnum} is :{num}")  '''