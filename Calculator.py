while True:
    x = float(input("Enter your first operation: "))
    operation = (input("Enter your operation(+,-,*,/): "))
    y = float(input("Enter your second operation: ")) 
    print("= ", end="")

    if operation == "+":
        print(f"{x + y:,}")
    if operation == "-":
        print(f"{x - y:,}")
    if operation == "*":
        print(f"{x * y:,}")
    if  operation == "/":
        print(f"{x / y:,}")
