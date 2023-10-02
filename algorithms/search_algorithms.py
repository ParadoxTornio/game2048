from decorators import time_counter
import time


class Human:
    def __init__(self, name):
        self.name = name


@time_counter
def linear_search(list_, target):
    time.sleep(1)
    for i in range(len(list_)):
        if list_[i] == target:
            print(i)


def class_linear_search(list_, target):
    time.sleep(1)
    for i in range(len(list_)):
        if list_[i].name == target:
            print(i)


@time_counter
def binary_search(list_, target):
    time.sleep(1)
    len_ = len(list_)
    left = 0
    right = len_ - 1
    result = []

    while left <= right:
        middle = (left + right) // 2
        if list_[middle] == target:
            result.append(middle)
            break
        elif list_[middle] > target:
            right = middle - 1
        else:
            left = middle + 1

    counter = 1
    while list_[middle + counter] == target:
        result.append(middle + counter)
        counter += 1

    counter_2 = 1
    while list_[middle - counter_2] == target:
        result.insert(0, middle - counter_2)
        counter_2 += 1

    return result


# num_list = [i for i in range(1, 500000001)]
num_list = [1, 2, 2, 2, 3]

print(binary_search(num_list, 2))
# linear_search(num_list, 500000000)


# num_list = [1, 2, 2, 2, 3]
# linear_search(num_list, 2)

# human1 = Human('1')
# human2 = Human('2')
# human3 = Human('3')
# human4 = Human('4')
# human5 = Human('5')
# num_list = [human1, human2, human3, human4, human5]
# class_linear_search(num_list, '4')
