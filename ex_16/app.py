

def print_line(n):
    for i in range(n, 0, -1):
        print(i, end=" ")


def print_triangle(size):
    for i in range(size, 0, -1):
        print_line(i)
        print()


print_triangle(5)
