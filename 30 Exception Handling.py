# Exception =   Events detected during execution
#               that interrupt the flow of a program

try: #For codes that are dangerous, because we dk what user will input
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
    
except ZeroDivisionError as e: #ZeroDivisionError is a specific error.
    print(e)
    print("You can't divide that by zero.")


except ValueError as e:#as e to describe the error
    print(e)
    print("Enter only numbers, please.")


except Exception as e: #Exception is ANY error, good to use this at the end.
    print(e)
    print("Something went wrong :(")

else: #try is similar to IF statement, ends with an else statement.
    print(result)

#if you open files, to close them in the final block.
finally:
    print("This will always execute")