try:
  a=float(input("Enter first number:"))
  oper=input("Enter operator (+,-,*,/)")
  b=float(input("Enter second number:"))
  
  match oper:
    case "+":
      c=a+b
    case "-":
      c=a-b
    case "*":
      c=a*b
    case "/":
      c=a/b
    case _:
      print("Invalid operator")
      c=None
  
except ZeroDivisionError:
  print("cannot divide by zero")

except ValueError:
  print("please enter valid number")

else:
  if c is not None:
    print(c)