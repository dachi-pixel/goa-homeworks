def blahblah(string1, string2):
    return string1 + string2
print(str(blahblah("string", "string2")))

#2
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def listt(list):
    return list[5] + list[3]
print(listt(list))

#3

def DistanceIn_kilometers(miles):
    return miles * 1.60934
print(DistanceIn_kilometers(5))

#4

def max(a, b):
    if a > b:
        return a
    else:
        return b
print(max(5, 10))

#5

def Turn_around(string):
    return string[::-1]
print(Turn_around("string"))