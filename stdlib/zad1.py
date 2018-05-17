import json


class Employee:
    def __init__(self, firstname, lastname, birthyear, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.birthyear = birthyear
        self.salary = salary

    @classmethod
    def from_dict(cls, data_dict):
        return cls(firstname=data_dict['firstname'], lastname=data_dict['lastname'],
                   birthyear=data_dict['birthyear'], salary=data_dict['salary'])

    def to_dict(self):
        return {'firstname': self.firstname,
                'lastname': self.lastname,
                'birthyear': self.birthyear,
                'salary': self.salary}


class EmployeeDataBase:
    def __init__(self, data_file):
        self._data_file = data_file

    def _load_employees(self):
        try:
            with open(self._data_file) as data:
                es = json.load(data)
                return [Employee.from_dict(e) for e in es]
        except FileNotFoundError:
            return []

    def print_employees(self):
        employees = self._load_employees()
        if not employees:
            print(f'Plik {self._data_file} nie istnieje lub jest pusty!')
        else:
            for i, e in enumerate(employees, start=1):
                print(
                    f'[{i}] {e.firstname} {e.lastname} - rok: {e.birthyear}, pensja: {e.salary:.2f}')

    def add_employee(self, employee_dict):
        new_employee = Employee.from_dict(employee_dict)
        employees = self._load_employees()
        employees.append(new_employee)
        with open(self._data_file, 'w') as data:
            json.dump([e.to_dict() for e in employees], data)

    def remove_employee(self, index):
        employees = self._load_employees()
        try:
            del employees[index]
            with open(self._data_file, 'w') as data:
                json.dump([e.to_dict() for e in employees], data)
        except IndexError:
            print(f'Pracownik o indeksie {index + 1} nie istnieje!')


if __name__ == '__main__':
    data_file = 'employee_data.json'
    db = EmployeeDataBase(data_file)

    action = input('Co chcesz zrobić? [dodaj - d/wypisz - w/usuń - u] ')
    if action == 'd':
        firstname = input('Imię: ')
        lastname = input('Nazwisko: ')
        birthyear = int(input('Rok urodzenia: '))
        salary = float(input('Pensja: '))
        emp = {'firstname': firstname, 'lastname': lastname, 'birthyear': birthyear,
               'salary': salary}
        db.add_employee(emp)
    elif action == 'w':
        db.print_employees()
    elif action == 'u':
        index = int(input('Podaj indeks pracownika do usunięcia: ')) - 1
        db.remove_employee(index)
    else:
        print('Niewłaściwa komenda!')
