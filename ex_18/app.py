def print_numbers(n):
    for i in range(1, n+1):
        print(i, end=" ")


def print_asterisks(n):
    for i in range(1, n+1):
        print("*", end=" ")


def print_triangle(n):
    for i in range(n, 0, -1):
        print_numbers(i)
        print_asterisks(i)
        print()


n = int(input("Please enter a number: "))
print_triangle(n)
