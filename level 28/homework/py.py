def double(a):                                           #ამ კოდით ვქმნით ფუნქციას და ვიყენებთ ერთჯერად  ნაცვალსახელს, ამ შემთხვევაში "a"
    return (str(a) * 2)                                  #ეს არის ფუნქციის კოდი თუ რა უნდა გააკეთოს
print(int(double(str(input("enter your chosen key: "))))) #აქ კი ერთჯერადი ნაცვალსახელი შევცვალეთ სრულ სახელში და დავპრინტეთ ფუნქცია

#2

def is_max(a, b):
    if int(a) > int(b):
        print("first is bigger")
    else:
        print("second is bigger")
is_max(input("enter your 1num: "), input("enter your 2num: "))