def double_list_elements(num_list):
    new_list =[]
    for i in num_list:
        new_list.append(i*2)
    return new_list
print(double_list_elements([2, 3, 4, 6, 8, 9]))

#2

def add_item(item_list, item): 
    item_list.append(item)
    return item_list
print(add_item([1, 2, 3],4))

#3

def remove_item(item_list, item):
    item_list.remove(item)
    return item_list
print(remove_item([1, 2, 3, 4], 3))

#4

def min_item(num_list):
    minIn_list = num_list[0]
    for i in num_list:
        if i < minIn_list:
            minIn_list = i
    return minIn_list
print(min_item([8, 9, 123, 40, 5, 2, 1000]))