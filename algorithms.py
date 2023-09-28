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
        left, right, index_counter = 0, 0, 0
        while left < len(left_half) and right < len(right_half):
            if left_half[left] < right_half[right]:
                list_[index_counter] = left_half[left]
                left += 1
            else:
                list_[index_counter] = right_half[right]
                right += 1
            index_counter += 1
        while left < len(left_half):
            list_[index_counter] = left_half[left]
            left += 1
            index_counter += 1
        while right < len(right_half):
            list_[index_counter] = right_half[right]
            right += 1
            index_counter += 1
    return list_


@time_counter
def selection_sort(list_):
    len_ = len(list_)
    for a in range(len_):
        min_index = a
        for j in range(a + 1, len_):
            if list_[j] < list_[min_index]:
                min_index = j
        list_[a], list_[min_index] = list_[min_index], list_[a]
    return list_


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
selection_sort(num_list_2)
