last_name, first_name, phone_number, description, id = '', '', '', '', 0


def contact(last_n, first_n, phone, desc, id_contact):
    global last_name
    global first_name
    global phone_number
    global description
    global id
    id = id_contact
    last_name = last_n
    first_name = first_n
    phone_number = phone
    description = desc

    return {f'{id}': {
        'Фамилия': last_name,
        'Имя': first_name,
        'Телефон': phone_number,
        'Описание': description}}
