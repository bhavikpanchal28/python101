#scope = the region that a variable is recognized

name = "Panchal"         # a global scope (available inside and outside the function)
def display_name():
#    name = "Bhavik"     # a local scope (available only inside this function)
    print(name)


display_name()
print(name)