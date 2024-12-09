i = 0
while i <= 20:
    print(i)
    i += 2

# 2)

num2 = 2
while num2 <= 4:
    print(num2)
    num2 += 2


# 3)



secretnum = 4
guessedNum = int(input("enter your guess:"))
while guessedNum != secretnum:
    print("your num is incorrect try again")
    break
else:
    print("u guessed the number, congrats")


# 4)


password = "password123"
enterPassword = input("Enter your password: ")
while enterPassword != password:
    print("try again")
    enterPassword = input("Enter your password: ")
    break
print("correct")
