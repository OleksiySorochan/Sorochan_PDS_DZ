from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

def comparison(*args):
    a = list(args)
    sort = sorted(a)
    return sort[0]

comparison_dict = {}

def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


def main():
    with ThreadPoolExecutor() as tr:
        start_time = time.time()
        res_tr = tr.map(factorial, range(1, 500))
        tr_time = time.time() - start_time
        comparison_dict[tr_time] = 'ThreadPoolExecutor'

        # print('вивід значення для ThreadPoolExecutor')
        # for value in res_tr:
        #     print(value)

    with ProcessPoolExecutor() as pr:
        start_time_pr = time.time()
        res_pr = pr.map(factorial, range(1, 500))
        pr_time = time.time() -  start_time_pr
        comparison_dict[pr_time] = 'ProcessPoolExecutor'

        # print('вивід значення для ProcessPoolExecutor')
        # for value in res_pr:
        #     print(value)

    com_t = comparison(tr_time, pr_time)
    res = comparison_dict[com_t]
    print("Обчислення факторіалу числа від 1 до 500 ProcessPoolExecutor і ThreadPoolExecutor способами")
    print(f"Самий швидчий варіант: {res}, займає часу: {com_t} секунд")
    print('*'*50)
    print(f'{comparison_dict[tr_time]} займає часу: {tr_time} секунд')
    print(f'{comparison_dict[pr_time]} займає часу: {pr_time} секунд')


if __name__ == '__main__':
    main()