from dz_13_01 import int_list, float_list, str_list
import time

def bubble_sort(lst):
    length = len(lst)
    for index in range(0, length):
        swap = False
        for i in range(0, length - index - 1):
            if lst[i] > lst[i +1]:
                lst[i], lst[i +1] = lst[i +1], lst[i]
                swap = True
            if not swap:
                break
    return lst


def mid_time(lst, n=2):
    time_list = []
    a = 1
    while a <= n:
        start = time.time()
        bubble_sort(lst)
        time_list.append(time.time() - start)
        a +=1
    return sum(time_list) / len(time_list)

if __name__ == '__main__':
    print(f"Середній час для сортування списку 'int_list' за {12} ітерацій бульбашковим методом: {mid_time(int_list, 12)} сек")
    print(f"Середній час для сортування списку 'float_list' за {12} ітерацій бульбашковим методом: {mid_time(float_list, 12)} сек")
    print(f"Середній час для сортування списку 'str_list' за {12} ітерацій бульбашковим методом: {mid_time(str_list, 12)} сек")
