# Написать функцию-декоратор для кеширования значений функции
# Написать функцию seq(n)
# n = 0 ....N
# (1 + n) ** n возвращает [x1, x2, x3, , , , xn]

# (**) с помощью декоратора-логгера создать лог функции (с замером времени выполнения функции)

import datetime


def cache(func):

    def wrapper(*args):
        results = []
        cache = {}
        time_start = datetime.datetime.now()

        for n in args:
            if n in cache:
                current_result = cache[n]
            else:
                current_result = func(n)
                cache.update({n: current_result})
            results.append(current_result)

        time_end = datetime.datetime.now()
        time_result = time_end - time_start

        log_msg = f'Период: {time_start:%H:%M:%S} - {time_end:%H:%M:%S}; Время: {time_result}; Результат: {results}\n'
        print(log_msg)

        with open('Seminar10/task1_log.log', 'a', encoding='utf-8') as file:
            file.write(log_msg)

        return results

    return wrapper


@cache
def seq(n):
    return (1 + n) ** n


print(seq(1, 3, 5, 4, 5, 5, 4))
