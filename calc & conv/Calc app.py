import BasicOpsModule as calc 

print("""Welcome to my basic calculator. """) 


try: 
    option = int(input("""1. Basic operations. \n2. Length converter. \n3. Weight converter. \n10. Quit. """)) 

    while option != 10: 
        first_num = float(input("Enter your first number : "))
        op = input("Operator sign : ") 
        second_num = float(input("Enter your second number : ")) 
        print(" ")


        if option == 1: 
            if op.strip() == "+":
                ans = calc.Calculator.add(first_num, second_num)

            elif op.strip() == "-":
                ans = calc.Calculator.subtract(first_num, second_num) 

            elif op.strip() == "*":
                ans = calc.Calculator.multiply(first_num, second_num)

            elif op.strip() == "/":
                ans = calc.Calculator.divide(first_num, second_num)

            elif op.strip() == "**":
                ans = calc.Calculator.exponent(first_num, second_num)

            elif op.strip() == "%":
                ans = calc.Calculator.modulus(first_num, second_num)

            # else:
            #     print("Undefined operator. ")  

            # print(" ")

            print(f"{first_num} {op} {second_num} = {ans}")
            op.replace(op, "")

            print(" ")  

        elif option == 2: 
            print("Not yet ready. ")

        elif option == 3: 
            print("Not yet ready. ") 

        else: 
            print("Undefined option. ") 


except ZeroDivisionError:
    print("Cannot divide by zero. ") 

except ValueError:
    print("Enter a real number. ")  

except NameError: 
    print("Enter a defined operator. ") 


# tackle zerodiverror, valueerror(entering nothing at the value side), nameerror(occured when i entered a number for the operator.)
# errors in the while loop 
