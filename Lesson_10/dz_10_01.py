def name_of_manth(number):
    manths = {1:'Січень', 2: 'Лютий', 3: 'Березень', 4: 'Квітень', 5: 'Травень', 6: 'Червень',
              7: 'Липень', 8: 'Серпень', 9: 'Вересень', 10: 'Жовтень', 11: 'Листопад', 12:'Грудень'}
    try:
        return manths[number]
    except KeyError:
        try:
            return manths[int(number)]
        except ValueError as ex:
            return f"{ex}: веддіть номер місяця, число від 1 до 12"
    except Exception as ex:
        return f"{ex}: веддіть номер місяця, число від 1 до 12"



print(name_of_manth(6))