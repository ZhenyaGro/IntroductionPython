import sqlite3
from time import sleep

DB = sqlite3.connect('Seminar8/data_base.db')

cursor = DB.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS personal(
  id INTEGER PRIMARY KEY autoincrement,
  name TEXT,
  last_name TEXT,
  position TEXT,
  salary INT,
  bonus INT
)''')

data = [(1, 'Иван', 'Иванов', 'Главный инженер', 50000, 10000), (2, 'Игорь',
                                                                 'Игорев', 'Инженер', 20000, 8000), (3, 'Олег', 'Олегов', 'Завхоз', 12000, 3000)]

try:
    cursor.execute('INSERT INTO personal VALUES(?,?,?,?,?,?);', data)
    DB.commit()
except:
    print('Данные уже есть')


cursor.execute('SELECT * FROM personal WHERE id=2;')
search_result = cursor.fetchone()
print(search_result)


def show_data():
    for i in cursor.execute('SELECT * FROM personal;'):
        print(*i)


def add_record(data):
    try:
        cursor.execute(
            f'''INSERT INTO personal VALUES({", ".join(f'"{str(i)}"' if isinstance(i, str) else str(i) for i in data)});''')
        DB.commit()
        print('Запись добавлена')
    except:
        print('Не удалось добавить запись')


def delete_record(id):
    cursor.execute(f'DELETE FROM personal WHERE id={id};')
    DB.commit()


def search_by_lastname(lastname):
    cursor.execute(
        f'SELECT * FROM personal WHERE last_name LIKE "{lastname}";')
    return cursor.fetchall()


def update_salary(salary, id):
    try:
        update_query = '''UPDATE personal SET salary = ? WHERE id = ?'''
        data = (salary, id)
        cursor.execute(update_query, data)
        DB.commit()
        print('Зарплата обновлена')
    except:
        print('Не удалось обновить зарплату')


def exit():
    return


def launch_app():
    while True:
        user_choice = input(
            '\nМеню\n1 - Показать базу\n2 - Добавить запись\n3 - Удалить запись\n4 - Найти работника по фамилии\n5 - Обновить зарплату\nq - Выход\n')

        if user_choice == '1':
            show_data()
            sleep(1)

        elif user_choice == '2':
            cursor.execute('SELECT MAX(id) FROM personal')
            max_id = cursor.fetchone()
            next_id = max_id[0] + 1
            print(f'Next id = {next_id}')

            record_data = [next_id, input('Имя: '), input('Фамилия: '), input('Должность: '), int(
                input('Зарплата: ')), int(input('Бонус: '))]

            add_record(record_data)

        elif user_choice == '3':
            try:
                deleting_id = int(input('Введите id: '))
            except:
                print('Некорректный ввод')
                break
            delete_record(deleting_id)

        elif user_choice == '4':
            print(search_by_lastname(input('Введите фамилию: ')))
            sleep(1)

        elif user_choice == '5':
            try:
                employee_id = int(input('Введите id работника: '))
                new_salary = int(input('Введите новую зарплату: '))
            except:
                print('Некорректный ввод')
                break
            update_salary(new_salary, employee_id)

        elif user_choice == 'q':
            print('\nВыход\n')
            cursor.close()
            break

        else:
            print('Некорректный ввод')


launch_app()
