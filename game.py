import random
q=0
num=random.randint(1,7)
while (True):
    if(q==6):
        print(f"you have failed to guess the answer after {q} attempts")
        break
    inp=int(input("enter your number"))
    if(num==inp):
            print(f"you have guessed the right number i.e, {num} in {q+1} attempt")
            break
    else:
            print("try again")
            q=q+1    