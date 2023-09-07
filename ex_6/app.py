import random


def print_max_number(first, second, third):
    if first > second and first > third:
        max_number = first
    elif second > third:
        max_number = second
    else:
        max_number = third

    print("Max:", max_number)


print_max_number(1, 2, 3)


first = int(input("Please enter first number: "))
second = int(input("Please enter second number: "))
third = int(input("Please enter third number: "))

print_max_number(first, second, third)


first = random.randint(1, 10)
second = random.randint(1, 10)
third = random.randint(1, 10)

print_max_number(first, second, third)
