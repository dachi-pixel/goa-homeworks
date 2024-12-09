#1)
#true output)
print(19 < 20)
print(29 > 20)
print(20 == 20) 

#false output)

print(20 < 10)
print(20 > 29)
print(20 == 78)

#2)

for i in range(0, 102, 2): print(i)

#3)

needToGuess = 2
userNum = input("Enter your num: ")
while  userNum != needToGuess:
    print("try again")
    userNum = input("Enter your num: ")
    break
print("correct")
