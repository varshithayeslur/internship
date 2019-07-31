num=int(input("Enter the number"))
new=0
count=1
while True:
    if num==0:
        break
    temp=num%10
    num=num//10
    if temp==9:
        temp=0
        new=new+(temp*count)
        count=count*10
    else:
        temp=temp+1
        new=new+(temp*count)
        count=count*10

print(new)