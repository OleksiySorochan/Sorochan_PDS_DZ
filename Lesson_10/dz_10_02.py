def unicum_namber(lst):
    try:
        a = 0
        for i in lst:
            if lst.count(i) > 1:
                a +=1
        if a > 0:
            return f'Числа в цьому списку не є унікальними'
        else:
            return f'Числа в цьому списку  є унікальними'
    except AttributeError as ex:
        print(f" {ex} Введіть список чисел")
    except Exception as ex:
        print(f" Невідома помилка: {ex}. Программа приймає список числел, і провіряє на унікальность")






d = {'one': 1, 'two': 2}
my_list = '1, 3, 3, 4, 5, 6, 5, 4, 3'
my_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 0]
print(unicum_namber(my_list2))

