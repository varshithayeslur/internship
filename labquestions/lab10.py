def sum (my_list):
    sum = 0 
    for i in my_list:
        sum=sum + i
    return sum
lst = [1,2,3,4,5]
s= sum(lst)
print(f"the sum is{s}")