import json


class EmployeeDataBase:
    def __init__(self, data_file):
        self._data_file = data_file
        self._employees = []

    def load_employees(self):
        try:
            with open(self._data_file) as data:
                self._employees = json.load(data)
        except FileNotFoundError:
            pass

    def print_employees(self):
        self.load_employees()
        if not self._employees:
            print(f'Plik {self._data_file} nie istnieje lub jest pusty!')
        else:
            for i, e in enumerate(self._employees, start=1):
                print(
                    f'[{i}] {e["firstname"]} {e["lastname"]} - rok: {e["birthyear"]}, pensja: {e["salary"]:.2f}')

    def add_employee(self, employee_dict):
        self.load_employees()
        self._employees.append(employee_dict)
        with open(self._data_file, 'w') as data:
            json.dump(self._employees, data)

    def remove_employee(self, index):
        self.load_employees()
        try:
            del self._employees[index]
            with open(self._data_file, 'w') as data:
                json.dump(self._employees, data)
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
