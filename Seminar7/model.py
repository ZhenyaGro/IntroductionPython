import csv
from genericpath import exists
import os.path
last_name, first_name, phone_number, description = '', '', '', ''


def create_contact(ln, fn, phn, dsc):
    global last_name
    global first_name
    global phone_number
    global description
    last_name = ln
    first_name = fn
    phone_number = phn
    description = dsc

    contact = {
        'Фамилия': last_name,
        'Имя': first_name,
        'Телефон': phone_number,
        'Описание': description}

    with open('Seminar7/contacts.csv', 'a', newline='') as contacts_file:
        writer = csv.writer(contacts_file, delimiter=' ')
        writer.writerow(contact.values())

    return contact


def import_contacts(path='Seminar7/contacts.csv'):
    contacts_list = []
    if (exists(path)):
        with open(path, 'r') as file:
            for i in file:
                contacts_list.append(i.strip().split(','))
        return contacts_list
    else:
        print(f'Не найден файл {path}')
        return


def export_contacts(contacts_list, extension='.txt'):
    if extension != '.txt' and extension != '.csv':
        print('Некорректное расширение файла')
    else:
        with open(f'Seminar7/exportedContacts{extension}', 'w', encoding='utf-8') as file:
            for i in contacts_list:
                for j in range(0, len(i)):
                    if j == len(i) - 1:
                        file.write(f'{i[j]}')
                    else:
                        file.write(f'{i[j]},')
                file.write('\n')
        print(f'Файл "exportedContacts{extension}" сохранен')
