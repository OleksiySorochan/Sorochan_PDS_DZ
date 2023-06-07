from multiprocessing import Pool
import threading
import time, os


# функція для порівяння часу і визначення переможця
def comparison(*args):
    a = list(args)
    sort = sorted(a)
    return sort[0]

comparison_dict = {}

# обчислення факторіалу
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f

# звичайний спосіб
def normal_way():
    s = time.time()
    for i in range(1, 500):
        factorial(i)
    nor_time = time.time() - s
    return nor_time

# threading
def ran(start=0, finish=0):
    for i in range(start, finish):
        factorial(i)

task_1 = threading.Thread(target=ran, kwargs={'finish': 250})
task_2 = threading.Thread(target=ran, kwargs={'start': 250, 'finish': 500})



if __name__ == '__main__':
    # запуск завдань threading способом
    s = time.time()
    task_1.start()
    task_2.start()
    task_1.join()
    task_2.join()
    th_time = time.time()-s
    comparison_dict[th_time] = 'threading'

    #pool спосіб
    cpu = os.cpu_count()
    with Pool(cpu) as p:
        s2 = time.time()
        p.map(factorial, range(1, 500))
        pl_time = time.time() - s2
        comparison_dict[pl_time] = 'pool'

    # запуск функції для обчислення звисайним способом
    nor_time = normal_way()
    comparison_dict[nor_time] = 'normal_way'

    com_t = comparison(th_time, pl_time, nor_time)
    res = comparison_dict[com_t]
    print("Обчислення факторіалу числа від 1 до 500 декількома способами")
    print(f"Самий швидчий варіант: {res}, займає часу: {com_t}")

