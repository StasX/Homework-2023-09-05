import random


def avg_of_list(lst):
    total = 0
    for number in lst:
        total += number

    avg = total/len(lst)
    print("Average is:", avg)


avg_of_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

numbers = []

for i in range(10):
    number = random.randint(1, 100)
    numbers.append(number)

avg_of_list(numbers)
