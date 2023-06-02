def unicum_namber(lst):
    try:
        a = 0
        if lst == []:
            raise ValueError('Цей список порожній, программа приймає список із чисел.')
        else:
            for i in lst:
                if type(i) is int:
                    if lst.count(i) > 1:
                        a +=1
                else:
                    raise ValueError('Программа приймає список чисел.')
        if a > 0:
            return f'Числа в цьому списку не є унікальними'
        else:
            return f'Числа в цьому списку  є унікальними'
    except ValueError as ex:
        print(f" {ex} Введіть список чисел")







d = {'one': 1, 'two': 2}
my_list = '1, 3, 3, 4, 5, 6, 5, 4, 3'
my_list2 = ['1', 2, 3, 4, 5, 6, 7, 8, 2]
my_list3 = [1, 2, 3, 4, 5, 6, 7, 8, 0]
print(unicum_namber(my_list2))

