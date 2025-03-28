def add(a,b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("Select operation -\n"
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n")

sel = int(input("Select Operation(1-4):"))
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

if sel == 1:
    print(a, "+", b, "=", add(a, b))
elif sel ==2:
    print(a, "-", b, "=", subtract(a, b))
elif sel == 3:
    print(a, "*", b, "=", multiply(a, b))
elif sel ==4:
    print(a, "/", b, "=",divide(a, b))
else:
    print("Invalid input.")
