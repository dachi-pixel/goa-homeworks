def find_item(item_list, item):
    for i in range(len(item_list)):
        if item_list[i] == item:
            return True
    else:
        return False
print(find_item([1, 2, 3, 4, 5, 6], 3))

#2)

def max_list(num_list):
    maxIn_list = num_list[0]
    for i in num_list:
        if i > maxIn_list:
            maxIn_list = i
    return maxIn_list
print(max_list([8, 9, 123, 40, 5, 2, 23, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]))


#3)

def increment_list(num_list):
    for i in range(len(num_list)):
        num_list[i] += 1
    return num_list
print(increment_list([1, 2, 3, 4, 5]))


#4)

def reverse_string(word):
    return word[::-1]
print(reverse_string("hello"))