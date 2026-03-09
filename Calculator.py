while True:
    num1 = float(input("Enter your first operation: "))
    operation = (input("Enter your operation(+,-,*,/): "))
    num2 = float(input("Enter your second operation: ")) 
    print("= ", end="")

    if operation == "+":
        print(num1 + num2)
    if operation == "-":
        print(num1 - num2)
    if operation == "*":
        print(num1 * num2)
    if  operation == "/":
        print(num1 / num2)