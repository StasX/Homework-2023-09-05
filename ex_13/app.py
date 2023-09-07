import random


def print_line(length):
    line = "* " * length
    print(line)


def print_rectangle(height, length):
    for i in range(height):
        print_line(length)


print_rectangle(4, 6)


length = random.randint(1, 10)
height = random.randint(1, 10)

print_rectangle(height, length)


length = int(input("Please enter length: "))
height = int(input("Please enter height: "))

print_rectangle(height, length)
