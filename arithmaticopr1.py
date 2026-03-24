import math

a = float(input("Enter number: "))
print("1.Sqrt  2.Power  3.Log  4.Factorial")
ch = int(input("Enter choice: "))

if ch == 1:
    print("Square Root:", math.sqrt(a))
elif ch == 2:
    b = float(input("Enter power: "))
    print("Result:", math.pow(a, b))
elif ch == 3:
    print("Log:", math.log(a))
elif ch == 4:
    print("Factorial:", math.factorial(int(a)))
else:
    print("Invalid choice")
