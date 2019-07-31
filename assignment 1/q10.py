space=5
for i in range(1,6):
    for j in range(1,space):
        print(' ',end='')
    for k in range(1,i+1):
        print(k,end='')
    for l in range(i-1,0,-1):
        print(l,end='')
    print('')
    space=space-1