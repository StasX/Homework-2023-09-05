import random


def print_smiley(number):
    if number == 1:
        smiley = ":-)"
    elif number == 2:
        smiley = ":-("
    elif number == 3:
        smiley = ":-/"
    elif number == 4:
        smiley = ";-)"
    elif number == 5:
        smiley = ";-("

    print(smiley)


def print_all_smileys():
    for i in range(1, 6):
        print_smiley(i)


def print_100_random_numbers():
    for i in range(100):
        number = random.randint(1, 5)
        print_smiley(number)


print_smiley(1)


number = int(input("Enter a number (1-5) for see the smile: "))
print_smiley(number)


number = random.randint(1, 5)
print_smiley(number)


print_all_smileys()


print_100_random_numbers()
