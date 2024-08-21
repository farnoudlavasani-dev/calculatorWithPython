
def add(a, b):
    return a + b
def differentiation(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed in my world"
    return a / b
def Exponentiation(a, b):
    return a ** b
print("hello. this is a simple Calculator")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exponentiation")
print("6.Exit")

while True: 
    choice = input("Select operation | Enter choice(1/2/3/4/5/6):")
    if choice == "6":
        print("goodbye")
        break
    elif choice in ["1", "2", "3", "4", "5"]:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        if choice == "1":
            print(add(num1, num2))
        elif choice == "2":
            print(differentiation(num1, num2))
        elif choice == "3":
            print(multiplication(num1, num2))
        elif choice == "4":
            print(division(num1, num2))
        elif choice == "5":
            print(Exponentiation(num1, num2))
    else:
        print("Invalid input")
        











