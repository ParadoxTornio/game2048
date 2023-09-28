def selection_sort(list_):
    len_ = len(list_)
    for a in range(len_):
        min_index = a
        for j in range(a + 1, len_):
            if list_[j] < list_[min_index]:
                min_index = j
        list_[a], list_[min_index] = list_[min_index], list_[a]
    print(list_)


num_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
selection_sort(num_list)
