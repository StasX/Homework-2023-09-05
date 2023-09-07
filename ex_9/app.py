import random


def print_list(lst):
    for i in range(len(lst)-1):
        print(lst[i], end=" | ")
    print(lst[-1])


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print_list(lst)

lst = []
items_to_create = random.randint(2, 100)
for i in range(items_to_create):
    number = random.randint(1, 100)
    lst.append(number)

print_list(lst)
