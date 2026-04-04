Operator=input("enter the operator type : <+,-,*,/>  ")
num1=float(input("Enter First Number "))
num2=float(input("Enter second Number "))

if Operator == '+' : 
    result = num1 + num2 
    print(round(result,3))
elif Operator == '-' : 
    result = num1 - num2 
    print(round(result,3))
elif Operator == '*' : 
    result = num1 * num2 
    print(round(result,3))
elif Operator == '/' : 
    result = num1 / num2 
    print(round(result,3))
else:
    print(f"{Operator} is not valid operator")
