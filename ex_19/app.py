def print_line(n):
    line = "* " * n
    print(line)


def print_rotated_triangle(n):
    for i in range(n, 0, -1):
        print_line(i)


def print_triangle(n):
    for i in range(1, n+1):
        print_line(i)


def solution(n):
    print_rotated_triangle(n)
    print_triangle(n)


n = int(input("Please enter a number: "))
solution(n)
