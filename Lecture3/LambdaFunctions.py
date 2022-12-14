# В файле хранятся числа, нужно выббрать четные и составить список пар (число; квадрат числа).
# Пример 1 2 3 5 8 15 23 38
# получить [(2, 4), (8, 64), (38, 1444)]

file = open(f'Lecture3/numbers.txt', 'r')
# result = [(i, int(i) * int(i))
#          for i in file.read().split() if int(i) % 2 == 0]

res = map(int, file.read().split())
file.close()
res = filter(lambda x: not x % 2, res)
res = list(map(lambda x: (x, x ** 2), res))

print(res)
