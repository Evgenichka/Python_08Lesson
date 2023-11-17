def read_phonebook(filename="phonebook.txt"):
    ## Читать телефонный справочник из файла.
    with open(filename, "a+"):
        pass

    with open(filename, "r") as file:
        lines = file.readlines()

    phonebook = {}
    for line in lines:
        surname, name, phone = line.strip().split(";")
        phonebook[surname] = (name, phone)
    return phonebook


def write_phonebook(phonebook, filename="phonebook.txt"):
    ## Записать телефонный справочник в файл.
    with open(filename, "w") as file:
        for surname, (name, phone) in phonebook.items():
            file.write(f"{surname};{name};{phone}\n")


def add_entry(surname, name, phone):
    phonebook = read_phonebook()
    phonebook[surname] = (name, phone)
    write_phonebook(phonebook)


def update_entry(surname, name=None, phone=None):
    phonebook = read_phonebook()
    if surname in phonebook:
        current_name, current_phone = phonebook[surname]
        phonebook[surname] = (name if name else current_name, phone if phone else current_phone)
        write_phonebook(phonebook)


def delete_entry(surname):
    phonebook = read_phonebook()
    if surname in phonebook:
        del phonebook[surname]
        write_phonebook(phonebook)


def find_entry(surname):
    phonebook = read_phonebook()
    return phonebook.get(surname, None)

def copy_entry(surname, name, phone):
    with open('phonebook.txt','r') as firstfile, open('new_phonebook.txt','a') as secondfile: 
    ## считывание содержимого из первого файла
        for line in firstfile: 
    ## считывание содержимого из первого файла добавление содержимого во второй файл 
             secondfile.write(line)



def main():
    while True:
        choice = input("Укажите действие (add/update/delete/copy/find/quit): ").lower()
        if choice == "quit":
            break
        elif choice == "add":
            surname = input("Введите фамилию: ")
            name = input("Введите имя: ")
            phone = input("Введите номер телефона: ")
            add_entry(surname, name, phone)
        elif choice == "update":
            surname = input("Введите фамилию: ")
            name = input("Введите новое имя (или оставьте пустым, чтобы не менять): ")
            phone = input("Введите новый номер телефона (или оставьте пустым, чтобы не менять): ")
            update_entry(surname, name, phone)
        elif choice == "delete":
            surname = input("Введите фамилию для удаления: ")
            delete_entry(surname)
        elif choice == "copy":
            surname = input("Введите фамилию: ")
            name = input("Введите имя: ")
            phone = input("Введите номер телефона: ")
            add_entry(surname, name, phone)
        elif choice == "find":
            surname = input("Введите фамилию для поиска: ")
            entry = find_entry(surname)
            if entry:
                print(f"Имя: {entry[0]}, Номер телефона: {entry[1]}")
            else:
                print("Запись не найдена.")
        else:
            print("Упс! Проверьте вводимые данные")


if __name__ == "__main__":
    main()
