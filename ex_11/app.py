import random


def print_random_number(start, end):
    number = random.randint(start, end)
    print(number)


print_random_number(10, 20)


start = int(input("Please enter a number for start: "))
end = int(input("Please enter a number for end: "))
print_random_number(start, end)


for i in range(100):
    print_random_number(-10, 10)
