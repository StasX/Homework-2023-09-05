import random


def print_full_line(length):
    line = "* "*length
    print(line)


def print_empty_line(length):
    if length == 1:
        line = "* "
    elif length == 2:
        line = "* "*2
    else:
        spaces_count = length-2
        spaces = "  "*spaces_count
        line = f"* {spaces}* "
    print(line)


def print_rectangle(height, length):
    print_full_line(length)
    if height == 2:
        print_full_line(length)
    elif height > 2:
        for i in range(height-2):
            print_empty_line(length)
        print_full_line(length)


print_rectangle(4, 6)

print()

height = random.randint(1, 10)
length = random.randint(1, 10)
print_rectangle(height, length)

print()

height = int(input("Please enter a height: "))
length = int(input("Please enter a length: "))
print_rectangle(height, length)
