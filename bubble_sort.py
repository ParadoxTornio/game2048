from decorators import time_counter
import time


@time_counter
def bubble_sort(list_):
    time.sleep(1)
    len_ = len(list_)
    replacement_counter = 0
    past_replacement_counter = 0
    for j in range(len_):
        if (replacement_counter != past_replacement_counter) or (
                replacement_counter == 0 and past_replacement_counter == 0):
            for i in range(0, len_ - 1 - j):
                if list_[i] > list_[i + 1]:
                    list_[i], list_[i + 1] = list_[i + 1], list_[i]
        past_replacement_counter = replacement_counter
        replacement_counter += 1
    print(list_)


num_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
num_list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
bubble_sort(num_list)
bubble_sort(num_list_2)
