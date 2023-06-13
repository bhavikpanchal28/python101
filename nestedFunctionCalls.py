#nested function calls = function calls that are inside other function calls
#                       innermost functions calls are resolved first

# num = input("Enter a positiver integer:")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)


#exact same as :
print(round(abs(float(input("Enter a positive integer:")))))
