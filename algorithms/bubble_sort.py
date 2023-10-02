from decorators import time_counter
import time
import random


@time_counter
def new_bubble_sort(list_):
    len_ = len(list_)
    for j in range(len_):
        any_changed = False
        for i in range(0, len_ - 1 - j):
            if list_[i] > list_[i + 1]:
                list_[i], list_[i + 1] = list_[i + 1], list_[i]
                any_changed = True
        if not any_changed:
            break
    print(list_)


@time_counter
def old_bubble_sort(list_):
    len_ = len(list_)
    for j in range(len_):
        for i in range(0, len_ - 1 - j):
            if list_[i] > list_[i + 1]:
                list_[i], list_[i + 1] = list_[i + 1], list_[i]
    print(list_)


num_list = []
num_list_2 = []
for i in range(10000):
    num_list.append(i)
    num_list_2.append(i)
num_list.reverse()
num_list_2.reverse()
new_bubble_sort(num_list)
new_bubble_sort(num_list)
old_bubble_sort(num_list_2)
old_bubble_sort(num_list_2)
