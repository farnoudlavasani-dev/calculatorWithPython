
def add(a, b):
    result = a + b
    return result
def differentiation(a, b):
    result = a - b
    return result
def multiplication(a, b):
    result = a * b
    return result
def division(a, b):
    result = a / b
    return result
def Exponentiation(a, b):
    result = a ** b
    return result
while True:
    print("hello world. this is a simple Calculator")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exponentiation")
    print("6.Exit")
    choice = input("Select operation | Enter choice(1/2/3/4/5/6):")
    if choice == "6":
        print("goodbye")
        break
    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            add(num1, num2)
        elif choice == "2":
            differentiation(num1, num2)
        elif choice == "3":
            multiplication(num1 , num2)
        elif choice == "4":
            division(num1, num2)
        elif choice == "5":
            Exponentiation(num1, num2)
        else:
            print("Invalid input")


    

        











