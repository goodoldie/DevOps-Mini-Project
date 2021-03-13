import scientific_calculator

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
            print(scientific_calculator.square_root(num))

        elif choice == '2':
            print(scientific_calculator.factorial(num))

        elif choice == '3':
            print(scientific_calculator.natural_log(num))

        elif choice == '4':
            exponent = float(input("Enter the power: "))
            print(scientific_calculator.power(num, exponent))
        break
    else:
        print("Invalid Input")
