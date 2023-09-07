def print_line(n):
    line = "* " * n
    print(line)


def print_triangle(n):
    for i in range(n, 0, -1):
        print_line(i)


n = int(input("Please enter a number: "))
print_triangle(n)
