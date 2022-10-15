# Задание в группах: Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.

# Create contact
# Show contacts list
# Show contact
# Update contact
# Delete contact
# Import contact
# Export contact

def menu():
    input('\nМеню справочника\n1 - Создать контакт\n2 - Показать список контактов\n3 - Показать данные контакта\n4 - Импортировать контакты\n5 - Экспортировать контакты\nДействие: ')


def create_contact():
    last_name = input('Фамилия: ')
    first_name = input('Имя: ')
    phone_number = input('Телефон: ')
    description = input('Описание: ')

    return {'Фамилия': last_name, 'Имя': first_name, 'Телефон': phone_number, 'Описание': description}


menu()
