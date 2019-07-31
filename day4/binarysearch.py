def binarySearch(lst,key):
    l=0
    h=len(lst)-1
    while l <= h:
        mid =(l+h) // 2
        if lst [mid] ==key:
            return mid
        elif key > lst[mid] :
            l= mid+1
        else:
            h = mid -1
    return -1

ele =6
res = binarySearch([1,2,3,4,5,6,7],ele)
if res == -1:
    print("element not found")
else:
    print(f"element {ele} found at {res}")



















'''recursive binary function
def binarySearch(lst,l,h,key)":
    if l <= h:
        mid =(l+h) // 2
        if lst [mid] ==key:
            return mid
        elif lst[mid] >key:
            return binarySearch(lst,mid+1,h,key)
        else:
            return binarySearch(lst,l,h,key)
    return -1 

    '''
