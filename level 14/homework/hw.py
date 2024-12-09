#1)
num1 =(input("enter your first num: "))
num2 =(input("enter your second num: "))

print ("operator")
print("+,-,/,*")
operator = (input("enter your operator: "))

if operator == "+":
    print(int(num1) + int(num2))
elif operator == "-":
    print(int(num1) - int(num2))
elif operator == "/":
    print(int(num1) / int(num2))
elif operator == "*":
    print(int(num1) * int(num2))
    if num1 or num2 == 0:
        print("you cant use 0 in our calculator")

#2)

for i in range(0, 700, 2):
    print(i)

#3)

for num in range(20, 100):
    print(num)

#4)

for o in range(100):
    if o / 2 == 0:
        print(str(o) + "even")
    else:
        print(str(o) + "odd")