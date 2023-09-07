import random


def print_line(length):
    line = "* " * length
    print(line)


def print_rectangle(height, length):
    for i in range(height):
        print_line(length)


def print_n_rectangles(count):
    for i in range(count):
        length = random.randint(1, 10)
        height = random.randint(1, 10)

        print_rectangle(height, length)
        print()


n = int(input("How many rectangles to draw?: "))
print_n_rectangles(n)
