def print_line(length):
    string = "* " * length
    print(string)


def print_square(size):
    for i in range(size):
        print_line(size)


print_square(4)


number = int(input("Please enter a number: "))
print_square(number)
