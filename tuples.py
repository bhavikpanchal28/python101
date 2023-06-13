# tuple = collection which is ordered and unchangeable used to group related date

student = ("Bhavik", 26, "male")

print(student.count("Bhavik"))
print(student.index("male"))

for x in student:
    print(x)

if "Bhavik" in student:
    print("Bhavik is here bitches!")
