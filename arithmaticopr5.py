operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b if b != 0 else "Error"
}

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+,-,*,/): ")

if op in operations:
    print("Result:", operations[op](a, b))
else:
    print("Invalid operator")
