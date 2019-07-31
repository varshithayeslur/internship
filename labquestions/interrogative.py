while(True):
    inp = input("enter the string")
    if inp =='done':
        break
    elif inp.endswith ("?"):
        print(f"the string{inp} is interrogative")
    else:
        print(f"the string{inp} is assertive")