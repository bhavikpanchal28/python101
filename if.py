#if statements

age = int(input("How old are you:"))

if age == 100:
    print("Congrats on 100 years of life!")
elif age >= 18:
    print("You are an adult")
elif age < 0:
    print("Invalid age")
else:
    print("You are a child")