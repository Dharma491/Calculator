num1=int(input("Enter first number: "))
oper=input("Enter operator (+, -, *, /): ")
num2=int(input("Enter second number: "))

if oper == '+':
    result = num1 + num2
    print("Result:", result)
elif oper == '-':
    result = num1 - num2
    print("Result:", result)
elif oper == '*':
    result = num1 * num2
    print("Result:", result)
elif oper == '/':
    result = num1 / num2
    print("Result:", result)
else:
    result = "Invalid operator"
    print(result)