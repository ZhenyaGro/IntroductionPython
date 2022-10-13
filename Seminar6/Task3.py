# Дан файл jack.txt (https://disk.yandex.ru/d/orFlUSXkcA600w)
# по аналогии с предыдущим заданием составить аналогичный словарь.

def count_words(string):
    dictionary = {}
    for i in string.lower().replace('\n', ' ').replace(
            ',', '').replace('.', '').replace('-', ' ').replace('  ', ' ').split(' '):
        dictionary[i] = dictionary[i] + 1 if i in dictionary else 1

    return dictionary


file = open('Seminar6/jack.txt')
string = count_words(file.read())
print(string)
