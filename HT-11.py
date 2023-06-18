from collections import UserDict
import phonenumbers
from datetime import datetime
from datetime import date as dates


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def iterator(self, n):
        count = 0
        for k, v in self.data.items():
            if count < n:
                count += 1
                yield f'{k}: {v}'
            else:
                raise StopIteration


class Field:
    def __init__(self, value):
        self.value = value
        self._value2 = None

    @property
    def value2(self):
        return self._value2

    @value2.setter
    def value2(self, new_value):
        self._value2 = new_value

        
class Name(Field):
    pass


class Phone(Field):
    
    def true_number(self, number):
        try:
            parsed_number = phonenumbers.parse(number, "UA")
            if phonenumbers.is_valid_number(parsed_number):
                return True
            else:
                return False
        except phonenumbers.phonenumberutil.NumberParseException:
            print("Failed to parse phone number")
    
    @property
    def value(self):
        return self._value2
    
    @value.setter
    def value(self, new_value):
        if self.true_number(new_value):
            self._value2 = new_value
        else:
            return 'Invalid phone number'

class Birthday(Field):
    
    def check_correct(self, date):
        if isinstance(date, dates):
            return True

        @property
        def value(self):
            return self._value2
        
        @value.setter
        def value(self, new_value):

            if self.check_correct(new_value):
                self._value2 = new_value

            else:
                print(f'Invalid date')

class Record(Field):
    
    def __init__(self, name, phone, birthday=None):
        self.name = name

        if phone:
           self.phones = []
           self.phones.append(phone)

        if birthday:
            self.birthday = birthday

    def days_to_birthday(self):
        if self.birthday.value2:
            current_date = datetime.datetime.now()
            birth_date = datetime.datetime.strptime(self.value2, "%Y-%m-%d")
            if birth_date < current_date:
                next_birthday = datetime.datetime(year=current_date.year + 1, month=birth_date.month, day=birth_date.day)
            else: 
                next_birthday = birth_date
            days_left = (next_birthday - current_date).days + 1
            print("Days until next birthday:", days_left)
            return days_left
        else:
            return 'You didn\'t give your date of birth'   
    
    def add_birthday(self, birthday):
        self.birthday = birthday
    
    def add_phone(self, phone):
        try:
            self.phones.append(phone)
        except AttributeError:
            self.phones = []
            self.phones.append(phone)

    def remove_phone(self, phone):
        for old_phone in self.phones:
            if phone == old_phone.value:
                self.phones.remove(old_phone)

    def change_phone(self, phone, new_phone):
        for old_phone in self.phones:
            if phone == old_phone.value:
                self.phones[self.phones.index(old_phone)] = Phone(new_phone)
    


if __name__ == '__main__':

    # Создание объектов класса Name
    name1 = Name("John")
    name2 = Name("Alice")

    # Проверка метода value
    print(name1.value)

    # Создание объектов класса Phone
    phone1 = Phone("+380955555555")
    phone2 = Phone("2311222211111")

    # Проверка метода value
    print(phone1.value)

    # Проверка метода true_number
    print(phone1.true_number(phone1.value))  # Вывод: True
    print(phone1.true_number("invalid"))  # Вывод: False

    # Создание объектов класса Birthday
    birthday1 = Birthday('1990-5-18')
    birthday2 = Birthday("1995-12-31")

    # Проверка метода value
    print(birthday1.value)

    # Проверка метода check_correct
    print(birthday1.check_correct(birthday1.value))  # Вывод: True
    print(birthday1.check_correct("invalid"))  # Вывод: False

    # Создание объектов класса Record
    record1 = Record(name1, phone1, birthday1)
    record2 = Record(name2, phone2)

    # Проверка метода add_birthday
    record2.add_birthday(birthday2)
    print(record2.birthday)  # Вывод: 1995-12-31

    # Проверка метода add_phone
    record1.add_phone(phone2)
    print(record1.phones)  # Вывод: [Phone(123456789), Phone(987654321)]

    # Проверка метода remove_phone
    record1.remove_phone("123456789")
    print(record1.phones)  # Вывод: [Phone(987654321)]

    # Проверка метода change_phone
    record2.change_phone("987654321", "111111111")
    print(record2.phones)

    # Проверка метода days_to_birthday
    record1.days_to_birthday()  # Вывод: Days until next birthday: 365
    record2.days_to_birthday()  # Вывод: You didn't provide your date of birth
    print('ALL OK')