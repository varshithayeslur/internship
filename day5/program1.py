try:
    num2 = int(input("enter the num2"))
    num1= int(input("enter the num1"))
    print(num1**num2)
    print(num1/num2)
    print("sum is :" +num1+num2)
except ZeroDivisionError:
    print(f"num2 cannot be zero")
except ValueError:
    print(f"please enter on;y numbers")
except Exception as e:
    print(f"sometthing went wrong {e}")