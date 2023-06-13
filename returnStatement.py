# Return Statement = functions send python values/objects back to the caller
#                   These values/objects are known as the function's return value

def multiply(num1, num2):
    result = num1 * num2
    return result
#   can even write it like this
#   return num1 * num2


x = multiply(6, 8)

print(x)