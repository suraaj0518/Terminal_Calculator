#numbers input and operation
op = input("Operation[+,-,*,/,Type_1 for sqrt]: ")
x = float(input("First number: "))

if op == "1":
    def squareroot(n):
        return pow(n, 2)
    print("Sqrt of number:", squareroot(x))

else:
    y = float(input("Second number: "))
    print("Result: ", end="")
    if op == "+":
        print(f"{x+y:,}")
    elif op == "-":
        print(f"{x-y:,}")
    elif op == "*":
        print(f"{x*y:,}")
    elif op == "/":
        print(f"{x/y:,}")
