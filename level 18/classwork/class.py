userNum = int(input("enter your num: "))
if userNum % 2 == 1:
    print("odd")
else:
    print("even")

#2)

userAge = int(input("enter your age: "))
if userAge < 18:
    print("you are not eneble to vote")
else:
    userVote = input("enter your vote red or blue: ")
print("your vote was suspectful")

#3)

temperature = 23
if temperature <= 15:
    print("cold")
elif temperature > 15 and temperature < 25:
    print("warm")
elif temperature >= 25:
    print("hot")

#4)

password = "pithon123"

userPassowrd = input("enter password: ")
if password == userPassowrd:
    print("Access Granted")
else:
    print('Access Denied')
