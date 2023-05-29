def name_of_manth(number):
    manths = ('Січень', 'Лютий', 'Березень', 'Квітень', 'Травень', 'Червень', 'Липень', 'Серпень', 'Вересень', 'Жовтень', 'Листопад', 'Грудень')
    try:
        return manths[number - 1]
    except IndexError as ex:
        return f"{ex}: веддіть номер місяця, число від 1 до 12"
    except TypeError as ex:
        try:
            return manths[int(number) - 1]
        except Exception as ex:
            return f"{ex}: веддіть номер місяця, число від 1 до 12"


print(name_of_manth(5))