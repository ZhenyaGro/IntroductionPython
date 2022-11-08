# Написать функцию-декоратор для кеширования значений функции
# Написать функцию seq(n)
# n = 0 ....N
# (1 + n) ** n возвращает [x1, x2, x3, , , , xn]

# (**) с помощью декоратора-логгера создать лог функции (с замером времени выполнения функции)

import datetime


def cache(func):

    def wrapper(n):
        result_cache = []
        for i in range(1, n + 1):
            time_start = datetime.datetime.now()
            result = func(i)
            time_end = datetime.datetime.now()

            result_cache.append(result)
            time_result = time_end - time_start

            log_msg = f'Период: {time_start:%H:%M:%S} - {time_end:%H:%M:%S}; Время: {time_result}; Результат: {result}\n'
            print(log_msg)
            with open('Seminar10/task1_log.log', 'a', encoding='utf-8') as file:
                file.write(log_msg)

        return result_cache

    return wrapper


@cache
def seq(n):
    return (1 + n) ** n


print(seq(5))
