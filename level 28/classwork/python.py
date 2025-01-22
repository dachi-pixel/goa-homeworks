def add_numbers(a, b):
    return (int(a) + int(b))
print(add_numbers(input("enter your first num: "), input("enter your second num: ")))

# 2)

def is_even(number):
    if number % 2 == 0:
        print("even")
    else:
        print("odd")
is_even(int(input("enter num: ")))

# 3)

def is_max(a, b):
    if int(a) > int(b):
        print("first is bigger")
    else:
        print("second is bigger")
is_max(input("enter your 1num: "), input("enter your 2num: "))
