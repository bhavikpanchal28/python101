# logical operators (and, or , not)

temp = int(input("What is the temperature?: "))

if not(temp >= 0 and temp <= 30):
    print("The weather is horrible today.")
    print("Stay inside.")

elif not(temp < 0 or temp > 30):
    print("The Weather is great today!")
    print("Go get some fresh air!")
