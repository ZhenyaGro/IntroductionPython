# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def factorization(n):
    result = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            result.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        result.append(n)
    return result


number = 100
print(factorization(number))
