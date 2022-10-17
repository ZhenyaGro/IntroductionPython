import controller
import model


def menu():
    try:
        choosen_menu_point = int(input(
            '\nМеню справочника\n1 - Создать контакт\n2 - Показать список контактов\n3 - Импортировать контакты\n4 - Экспортировать контакты\n0 - Выйти\nДействие: '))
    except:
        print('Некорректный ввод')
        return -1

    if choosen_menu_point < 0 or choosen_menu_point > 5:
        print('Некорректный ввод')
        return -1

    return choosen_menu_point


def show_contacts(contacts_list):
    print(contacts_list)


def add_contact():
    last_name = input('Фамилия: ')
    first_name = input('Имя: ')
    phone_number = input('Телефон: ')
    description = input('Описание: ')

    return [last_name, first_name, phone_number, description]
