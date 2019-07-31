num = int(input("enter the number"))
c = 0
while num !=0:
    r=num%10
    if r in [2,3,5,7]:
        c +=1
    num =num //10
        
print(f"number of prime digit is  {c}")