import json


class EmployeeDataBase:
    def __init__(self, data_file):
        self._data_file = data_file
        self._employees = []

    def load_employees(self):
        with open(self._data_file) as data:
            self._employees = json.load(data)

    def print_employees(self):
        try:
            self.load_employees()
        except FileNotFoundError:
            print(f'Plik {self._data_file} nie istnieje!')
        for i, e in enumerate(self._employees, start=1):
            print(
                f'[{i}] {e["firstname"]} {e["lastname"]} - rok: {e["birthyear"]}, pensja: {e["salary"]:.2f}')

    def add_employee(self, employee_dict):
        try:
            self.load_employees()
        except FileNotFoundError:
            pass
        self._employees.append(employee_dict)
        with open(self._data_file, 'w') as data:
            json.dump(self._employees, data)


if __name__ == '__main__':
    data_file = 'employee_data.json'
    db = EmployeeDataBase(data_file)

    action = input('Co chcesz zrobić? [dodaj - d/wypisz - w] ')
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
    else:
        print('Niewłaściwa komenda!')
