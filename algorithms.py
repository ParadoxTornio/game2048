import datetime
import time

list_ = []
set_ = set()
for i in range(1000000):
    string = str(i)
    list_.append(string)
    set_.add(string)

time_now = datetime.datetime.now()
print(time_now)
if '756352' in list_:
    print(datetime.datetime.now() - time_now)
time.sleep(1)
time_now = datetime.datetime.now()
print(time_now)
if '756352' in set_:
    print(datetime.datetime.now() - time_now)
