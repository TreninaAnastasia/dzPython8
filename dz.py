def enter_name():
    return input('Введите имя: ').capitalize()
def enter_surname():
    return input('Введите фамилию: ').capitalize()
def enter_phone():
    return input('Введите телефон: ').capitalize()
def enter_adress():
    return input('Введите адрес: ').capitalize()
def input_data():
    name = enter_name()
    surname = enter_surname()
    phone = enter_phone()
    adress = enter_adress()

    with open ('phone_book.txt', 'a', encoding = 'utf-8' ) as file:
        file.write(f'{name} {surname}: {phone}\n{adress}\n\n')
def print_data():
    with open('phone_book.txt', 'r', encoding='utf-8') as file:
        print(file.read())

input_data()
print_data()

def search_line():
    search = input('Введите данные для поиска: ').capitalize()
    with open('phone_book.txt', 'r', encoding='utf-8') as file:
            data = file.read().split('\n\n')[:-1]
            for line in data:
                if search in line:
                    print(line + '\n')

def edit_contact():
    search = input("Введите имя или фамилию контакта: ").capitalize()
    with open('phone_book.txt', 'r', encoding='utf-8') as file:
        data  = file.read().split('\n\n')[:-1]
        for line in data:
            if search in line:
                phone = input('Введите новый номер телефона: ')
                adress = input('Введите новый адрес: ')
                name = input ('Введите новое имя: ')
                surname = input ('Введите новую фамилию: ')
                print(f'{name} {surname}: {phone}\n{adress}\n\n')
            else:
                print("Контакт не найден")


search_line()
edit_contact()