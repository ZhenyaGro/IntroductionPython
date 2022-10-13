# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def encode(line):
    encoded_string = ""
    i = 0
    while (i <= len(line) - 1):
        count = 1
        ch = line[i]
        j = i
        while (j < len(line)-1):
            if (line[j] == line[j + 1]):
                count = count + 1
                j = j + 1
            else:
                break
        encoded_string = encoded_string + str(count) + ch
        i = j + 1

    return encoded_string


def decode(line):
    num, result = '', ''
    for i in line:
        if i.isdigit():
            num += i
        else:
            result += i * int(num)
            num = ''
    return result


file = open('Seminar5/FileTask4.txt')
string = encode(file.read())
file.close()
print(string)
print(decode(string))

# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE Выходные данные: 6A1F2D7C1A17E
