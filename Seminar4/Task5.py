# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

def dictionary_from_file(file_name):
    file = open(f'Seminar4/{file_name}', 'r')
    array = file.read().split(' + ')
    last_two = array[-1].split(' = ')
    array.pop()
    array.append(last_two[0])
    array.append(last_two[1])
    if last_two[0].find('x') != -1:
        last_x = 2
    else:
        last_x = 1

    dictionary = {}
    for i in range(0, len(array) - last_x):
        if array[i].find('x') != -1:
            current = array[i].split(' * ')
            if len(current) == 2:
                dictionary.update({current[1]: int(current[0])})
            else:
                dictionary.update({current[0]: 1})
        else:
            dictionary.update({'free_number': int(array[i])})

    return dictionary


first_dictionary = dictionary_from_file('FirstFile.txt')
print(first_dictionary)
second_dictionary = dictionary_from_file('SecondFile.txt')
print(second_dictionary)


def calculate_result(first_dictionary, second_dictionary):
    result = {}
    for element in first_dictionary:
        if element in second_dictionary.keys():
            result.update(
                {element: first_dictionary[element] + second_dictionary[element]})
        else:
            result.update({element: first_dictionary[element]})

    for element in second_dictionary:
        if element not in first_dictionary.keys():
            result.update({element: second_dictionary[element]})

    result = dict(sorted(result.items(), reverse=True))

    return result


result = calculate_result(first_dictionary, second_dictionary)
print(result)


def create_file(dictionary):
    file = open('Seminar4/Task5Result.txt', 'w')

    j = 1
    for i in dictionary.keys():
        if j == len(dictionary):
            if i == 'free_number':
                file.write(f'{dictionary[i]}')
            elif dictionary[i] == 1:
                file.write(f'{i}')
            else:
                file.write(f'{dictionary[i]} * {i}')
            continue
        if i == 'free_number':
            file.write(f'{dictionary[i]} + ')
        elif dictionary[i] == 1:
            file.write(f'{i} + ')
        else:
            file.write(f'{dictionary[i]} * {i} + ')
        j += 1

    file.write(' = 0')


create_file(result)


# 2 * x ** 5 + 2 * x ** 4 + x ** 2 + 2 * x + 3 = 0
# x ** 5 + 2 * x ** 4 + x ** 3 + x ** 2 + 1 = 0

# 3 * x ** 5 + 4 * x ** 4 + x ** 3 + 2 * x ** 2 + 2 * x + 4 = 0
