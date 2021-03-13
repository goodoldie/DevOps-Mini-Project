# Scientific Calculator Functions
import math as m


def square_root(x):
    return m.sqrt(x)


def factorial(x):
    return m.factorial(x)


def natural_log(x):
    return m.log(x)


def power(x, y):
    return (x ** y)


print("Select operation.")
print("1.sqrt")
print("2.fact")
print("3.ln")
print("4.pow")

while True:
    choice = input("Enter your choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num = float(input("Enter the number: "))

        if choice == '1':
            print(square_root(num))

        elif choice == '2':
            print(factorial(num))

        elif choice == '3':
            print(natural_log(num))

        elif choice == '4':
            exponent = float(input("Enter the power: "))
            print(power(num, exponent))
        break
    else:
        print("Invalid Input")
