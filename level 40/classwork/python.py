#upper makes all letters uppercase
#lower makes all letters lowercase
#capitalize makes the first letter uppercase
#find finds letter in your word and tells your what index number it is

input = input("Enter your name: ")
if input == input.capitalize():
    print("hello")
else:
    print("bye")


#3)

input = input("Enter your name: ")
input = input("Enter your username: ")
if input.find("a") == -1:
    print("theres no a in your name and username")
else:
    print("theres an a in your name and username")


#4)

input = input("Enter your username: ")
input = input("how wuld you like your username to be displayed?: ")
if input == "upper":
    print(input.upper())
elif input == "lower":
    print(input.lower())
elif input == "capitalize":
    print(input.capitalize())