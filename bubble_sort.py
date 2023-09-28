def bubble_sort(list_):
    len_ = len(list_)
    for j in range(len_):
        for i in range(0, len_ - 1 - j):
            if list_[i] > list_[i + 1]:
                list_[i], list_[i + 1] = list_[i + 1], list_[i]
    print(list_)


num_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
bubble_sort(num_list)
