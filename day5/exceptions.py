try:
    num = 100/0
except ZeroDivisionError as e:
    print("Except block")
    print(f"{e}")
finally:
    print("Finally block")