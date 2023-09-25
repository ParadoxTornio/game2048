# import datetime
# import time
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
#     print(datetime.datetime.now() - time_now)

list_ = [9, 8, 7, 6, 5, 4, 3, 2, 1]
len_ = len(list_)
for j in range(len_):
    for i in range(0, len_ - 1 - j):
        if list_[i] > list_[i + 1]:
            list_[i], list_[i + 1] = list_[i + 1], list_[i]
print(list_)
