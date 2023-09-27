import time
import random


#
# list_ = []
# set_ = set()
# for i in range(1000000):
#     string = str(i)
#     list_.append(string)
#     set_.add(string)
#
# time_now = datetime.datetime.now()
# print(time_now)
# if '756352' in list_:
#     print(datetime.datetime.now() - time_now)
# time.sleep(1)
# time_now = datetime.datetime.now()
# print(time_now)
# if '756352' in set_:
# print(datetime.datetime.now() - time_now

# пузырьковая сортировка

# list_ = [9, 8, 7, 6, 5, 4, 3, 2, 1]
# len_ = len(list_)
# for j in range(len_):
#     for i in range(0, len_ - 1 - j):
#         if list_[i] > list_[i + 1]:
#             list_[i], list_[i + 1] = list_[i + 1], list_[i]
# print(list_)

# сортировка выбором

# list_ = [9, 8, 7, 6, 5, 4, 3, 2, 1]
# len_ = len(list_)
# for i in range(len_):
#     min_index = i
#     for j in range(i + 1, len_):
#         if list_[j] < list_[min_index]:
#             min_index = j
#     list_[i], list_[min_index] = list_[min_index], list_[i]
# print(list_)

# list_ = ['bca', 'acb', 'abc', 'aa']
# len_ = len(list_)
# for i in range(len_):
#     min_index = i
#     for j in range(i + 1, len_):
#         if list_[j] < list_[min_index]:
#             min_index = j
#     list_[i], list_[min_index] = list_[min_index], list_[i]
#
# print(list_)
from typing import List


def time_counter(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        function(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)
    return wrapper


def merge_sort(list_: list):
    if len(list_) > 1:
        mid = len(list_) // 2
        left_half = list_[:mid]
        right_half = list_[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                list_[k] = left_half[i]
                i += 1
            else:
                list_[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            list_[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            list_[k] = right_half[j]
            j += 1
            k += 1
    return list_


@time_counter
def selection_sort(list_):
    len_ = len(list_)
    for i in range(len_):
        min_index = i
        for j in range(i + 1, len_):
            if list_[j] < list_[min_index]:
                min_index = j
        list_[i], list_[min_index] = list_[min_index], list_[i]
    return list_


@time_counter
def counting_sort(nums: List[int]) -> List[int]:
    i_lower_bound, upper_bound = min(nums), max(nums)
    lower_bound = i_lower_bound
    if i_lower_bound < 0:
        lb = abs(i_lower_bound)
        nums = [item + lb for item in nums]
        lower_bound, upper_bound = min(nums), max(nums)

    counter_nums = [0] * (upper_bound - lower_bound + 1)
    for item in nums:
        counter_nums[item - lower_bound] += 1
    pos = 0
    for idx, item in enumerate(counter_nums):
        num = idx + lower_bound
        for i in range(item):
            nums[pos] = num
            pos += 1
    if i_lower_bound < 0:
        lb = abs(i_lower_bound)
        nums = [item - lb for item in nums]
    return nums


num_list = []
num_list_2 = []
num_list_3 = []

for i in range(30000):
    random_num = random.randint(0, 1000000)
    num_list.append(random_num)
    num_list_2.append(random_num)
    num_list_3.append(random_num)

start_time_ = time.time()
merge_sort(num_list)
end_time_ = time.time()
print(end_time_ - start_time_)
counting_sort(num_list_3)
selection_sort(num_list_2)
