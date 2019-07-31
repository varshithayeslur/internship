paragraph="Comprehensions are a feature of Python which I would really miss if I ever have to leave it. Comprehensions are constructs that allow sequences to be built from other sequences. Several types of comprehensions are supported in both Python 2 and Python 3 ."

lst=paragraph.split(' ')
dictio=dict()
for ele in lst:
    if ele in dictio:
        dictio[ele]=dictio[ele]+1
    else:
        dictio[ele]=1

maxoccur=''
countmax=-9999
minoccur=''
countmin=9999

for ele in dictio:
    if dictio[ele]>countmax:
        countmax=dictio[ele]
        maxoccur=ele

for ele in dictio:
    if dictio[ele]<countmin:
        countmin=dictio[ele]
        minoccur=ele

print(f"Word appearing maximum times: {maxoccur};{countmax} times")
print(f"Word appearing minimum times: {minoccur};{countmin} times")