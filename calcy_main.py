import scientific_calculator
import os

os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print("DevOps Scientific Calculator. Select an Operation.")
    print("1: Sqaure Root")
    print("2: Factorial")
    print("3: Natural Log")
    print("4: Power")
    print("e: Exit")
    choice = input("Enter your choice : ")
    if choice in ('1', '2', '3', '4'):
        num = float(input("Enter the number: "))

        if choice == '1':
            print("Answer : ", scientific_calculator.square_root(num))

        elif choice == '2':
            print("Answer : ", scientific_calculator.factorial(num))

        elif choice == '3':
            print("Answer : ", scientific_calculator.natural_log(num))

        elif choice == '4':
            exp = float(input("Enter the power : "))
            print("Answer : ", scientific_calculator.power(num, exp))

    elif choice == 'e' or 'E':
        break

    else:
        print("Please Enter a valid Input")
    print("\n")
