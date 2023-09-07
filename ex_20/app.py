def print_numbers(n):
    for i in range(1, n+1):
        print(i, end=" ")

    for i in range(n+1, 0, -1):
        print(i, end=" ")


def print_line(spaces_count, line):
    spaces = "  " * spaces_count
    print(spaces, end="")
    print_numbers(line)
    print()


def print_triangle(n):
    for i in range(n):
        spaces_count = n-i
        print_line(spaces_count, i)


n = int(input("Please enter a number: "))
print_triangle(n)
