def print_n_times(msg, times):
    for i in range(times):
        print(msg)


print_n_times("Hi", 3)

user_msg = input("Please enter a message: ")
times_to_print = input("Please enter how many times to print your message: ")
times_to_print = int(times_to_print)

print_n_times(user_msg, times_to_print)
