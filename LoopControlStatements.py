#Loop control statements + change a loops execution from its normal sequence

#break = used to terminate the loop entirely
#continue = skips to the next iteration of the loop
#pass = does nothing, acts as a placeholder

#this program continues to run if a blank input is provided
#and stops when you provide any sort of name (technically input)

while True:
    name = input("Enter your name: ")
    if name != "":
        break

#This program will take out the "-" from the phone number

# phone_number = "905-550-5622"
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")

for i in range(1,21):

    if i ==13:
        pass
    else:
        print(i)
