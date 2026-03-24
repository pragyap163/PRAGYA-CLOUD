while True:
    print("\n1.Add 2.Sub 3.Mul 4.Div 5.Exit")
    ch = int(input("Enter choice: "))

    if ch == 5:
        break

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if ch == 1:
        print("Result:", a + b)
    elif ch == 2:
        print("Result:", a - b)
    elif ch == 3:
        print("Result:", a * b)
    elif ch == 4:
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")
