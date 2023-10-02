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
    print(list_)


num_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
merge_sort(num_list)
