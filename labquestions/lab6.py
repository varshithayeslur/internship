str = input("enter the string")
for ch in str:
    if ch in ['a','e','i','o']:
        str = str.replace(ch, ' *')
print(str)