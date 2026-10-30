while True: 

    operation = input("Choose an operation (+, -, *, /, **):")
    print()

    if operation == "**":
        num = float(input("Enter a number:"))
        power = int(input("Enter power such as square(2), cube(3) so on:"))
        print(num ** power)
        
    else:
        if operation in ["+", "-", "*", "/"]:
            num1 = float(input("Enter a number:"))
            num2 = float(input("Enter second number:"))

            if operation == "+":
                print(num1 + num2)

            elif operation == "-":
                print(num1 - num2)

            elif operation == "*":
                print(num1 * num2)    

            elif operation == "/":
                if num2 != 0:
                    print(num1 / num2)
                else:
                    print(f"{num1} cannot devided by zero!")

        else:
            print("Error!")

    print()
    choice = input("Do you want to continue? (y/n)")

    if choice == "n":
        break