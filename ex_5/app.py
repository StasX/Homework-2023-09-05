import random


def print_avg(first, second, third):
    total = first+second+third
    avg = total/3
    print("Average is:", avg)


print_avg(1, 2, 3)


first = int(input("Please enter first number: "))
second = int(input("Please enter second number: "))
third = int(input("Please enter third number: "))

print_avg(first, second, third)


first = random.randint(1, 10)
second = random.randint(1, 10)
third = random.randint(1, 10)

print_avg(first, second, third)
