from inmemory import InMemoryImpl
while True:
    print("*"*75)
    print("1. Add 2.view all 3.update 4.delete 5.search 6.exit")
    print("*"*75)
    ch = int(input("enter your choice:"))
    if ch == 1:
        InMemoryImpl.addcontact()
    elif ch == 2:
        InMemoryImpl.viewcontact()
    elif ch == 3:
        InMemoryImpl.updatecontact()
    elif ch == 4:
        InMemoryImpl.deletecontact()
    elif ch == 5:
        InMemoryImpl.search()
    else:
        break
    
    