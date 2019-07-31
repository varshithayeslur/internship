def cast_vote(age):
    assert age >= 18 , f"age shouldn't be < 18, it was : {age}"
    print("Thank you for voting.........")
try:
    age = int(input("enter the age"))
    cast_vote(age)
except AssertionError as a:
    print(a)
else:
    print(f"you entered a valid age : {age}")
finally:
    print("END............")