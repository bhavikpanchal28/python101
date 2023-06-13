# *args = parameter that will pack all arguments into a tuple

# def add (num1, num2):
#     sum = num1 + num2
#     return sum
#
# print(add(1,2,3))

def add (*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5,6))

# *args can be named anything
# ex/
def add (*random_name):
    sum = 0
    for i in random_name:
        sum += i
    return sum

print(add(1,2,3,4,5,6))