# Nested Function Calls =
# Function calls inside other function calls
# Innermost function calls are resolved first
# Returned value is used as arguement for the next outer function

# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

#These are pre built-in functions therefore there's no need to define them.
print(round(abs(float(input("Enter a whole positive number: ")))))