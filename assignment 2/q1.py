mport random

while True:
    first=random.randint(0,10)
    second=random.randint(0,10)
    third=random.randint(0,10)
    fourth=random.randint(0,10)
    if first + second + third + fourth == 12:
        if first>second:
            diff=first-second
        else:
            diff=second-first
        if third==diff and fourth == (first+third):
            num=(first*1000)+(second*100)+(third*10)+(fourth*1)
            break

print(num)