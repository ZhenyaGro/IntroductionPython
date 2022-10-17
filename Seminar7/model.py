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


# читаем что получилось
# with open('Seminar7/contacts.csv', newline='') as contacts_file:
#     reader = csv.reader(contacts_file, delimiter=' ')
#     for row in reader:
#         print(', '.join(row))
