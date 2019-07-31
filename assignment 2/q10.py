input="How much wood would a woodchuck chuck if the woodchuck could chuck wood?"

lst=input.split(' ')
count=0

dictio=dict()
for ele in lst:
    if ele in dictio:
        dictio[ele]=dictio[ele]+1
    else:
        dictio[ele]=1

for ele in dictio:
    if dictio[ele]==1:
        count=count+1

print(f"Number of Unique words:{count}")

print("Ocuurance of each word is")

for ele in dictio:
    print(f"{ele}:{dictio[ele]} times")
