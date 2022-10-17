import csv
last_name, first_name, phone_number, description, id = '', '', '', '', 0
contacts_list = {}


def create_contact(ln, fn, phn, dsc):
    global last_name
    global first_name
    global phone_number
    global description
    global id
    id += 1
    last_name = ln
    first_name = fn
    phone_number = phn
    description = dsc

    contacts_list.update({f'{id}': {
        'Фамилия': last_name,
        'Имя': first_name,
        'Телефон': phone_number,
        'Описание': description}})

    with open('Seminar7/contacts.csv', 'a', newline='') as contacts_file:
        writer = csv.writer(contacts_file, delimiter=' ')
        writer.writerow(contacts_list.values())

    return {f'{id}': {
        'Фамилия': last_name,
        'Имя': first_name,
        'Телефон': phone_number,
        'Описание': description}}


def read_file(path):
    file = open(path)
    contacts = file.read()
    file.close()
    return contacts


def import_contacts():
    pass


# читаем что получилось
# with open('Seminar7/contacts.csv', newline='') as contacts_file:
#     reader = csv.reader(contacts_file, delimiter=' ')
#     for row in reader:
#         print(', '.join(row))
