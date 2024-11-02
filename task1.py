from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass  


class Phone(Field):
    def __init__(self, value):
        # Перевіряю, чи номер телефону відповідає формату з 10 цифр
        if re.fullmatch(r'\d{10}', value):
            super().__init__(value)
        else:
            raise ValueError("Phone number must contain exactly 10 digits.")
    

# Клас для зберігання інформації про контакт (ім'я та список телефонів)
class Record:
    def __init__(self, name):
        # Створюю об'єкт Name та список телефонів
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        phone = Phone(phone_number)  
        self.phones.append(phone)    

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number: 
                self.phones.remove(phone)
                return f"Phone {phone_number} removed."
        return f"Phone {phone_number} not found."

   
    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:  # Шукаю номер, який потрібно змінити
                phone.value = new_phone   # Змінюю значення на новий номер
                return f"Phone {old_phone} changed to {new_phone}."
        return f"Phone {old_phone} not found."

    # Пошук конкретного номера телефону в записі
    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone.value  # Повертається номер, якщо знайдено
        return "Phone not found."

    # Форматований вивід запису
    def __str__(self):
       return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"



class AddressBook(UserDict):
 
    def add_record(self, record):
        self.data[record.name.value] = record  # Використовую ім'я як ключ
        return f"Record for {record.name.value} added."

    def find(self, name):
        return self.data.get(name, "Contact not found.")

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return f"Record for {name} deleted."
        return "Contact not found."


# Демонстрація роботи класів
if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")  # Додавання першого телефону
    john_record.add_phone("5555555555")  # Додавання другого телефону

    # Додавання запису John до адресної книги
    print(book.add_record(john_record))

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    print(book.add_record(jane_record))

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    if isinstance(john, Record):  # Перевіряємо, чи знайдено контакт
        print(john.edit_phone("1234567890", "1112223333"))  # Змінюємо номер
        print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name.value}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    print(book.delete("Jane"))
