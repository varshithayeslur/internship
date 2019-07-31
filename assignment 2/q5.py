name=input('Enter the name')

ls=['a','e','i','o','u']
vow_lis=list(filter(lambda x:x in ls,name))
count=len(vow_lis)
print(count)
print(vow_lis)