class Employee:
    def __init__(self, firstname, lastname, salary_per_hour):
        self.firstname = firstname
        self.lastname = lastname
        self.salary_per_hour = salary_per_hour
        self.hours_worked = 0
        self.overtime_worked = 0

    def pay_salary(self):
        salary = self.hours_worked * self.salary_per_hour
        salary += self.overtime_worked * 2 * self.salary_per_hour
        self.hours_worked = 0
        self.overtime_worked = 0
        return salary

    def register_time(self, hours):
        if hours <= 8:
            self.hours_worked += hours
        else:
            self.hours_worked += 8
            self.overtime_worked += hours - 8

    def __str__(self):
        return f'{self.firstname} {self.lastname}, stawka: {self.salary_per_hour:.2f}'


class EmployeeRegistry():
    def __init__(self):
        self.employees = []

    def register_employee(self, firstname: str, lastname: str,
                          salary_per_hour: str):
        employee = Employee(firstname, lastname, salary_per_hour)
        self.employees.append(employee)

    def register_employees_hours(self, hours, employee_index):
        try:
            employee = self.employees[employee_index]
            employee.register_time(hours)
        except IndexError:
            print('Pracownik o podanym indeksie nie istnieje!')

    def pay_employees_salary(self, emploee_index):
        try:
            employee = self.employees[emploee_index]
            return employee.pay_salary()
        except IndexError:
            print('Pracownik o takim indeksie nie istnieje!')

    def print_employees(self):
        for index, employee in enumerate(self.employees):
            print(f'{index}: {employee.__str__()}')


if __name__ == '__main__':
    registry = EmployeeRegistry()

    while True:
        act = input(
            'Co chcesz zrobić? [d - dodaj, l - wypisz, w - wypłata, r - rejestruj godziny, k - koniec]')
        if act == 'd':
            firstname = input('Podaj imię pracownika: ')
            lastname = input('Podaj nazwisko pracownika: ')
            salary_per_hour = float(
                input('Podaj stawkę pracownika za godzinę: '))
            registry.register_employee(firstname, lastname, salary_per_hour)
        elif act == 'l':
            registry.print_employees()
        elif act in ['r', 'w']:
            index = int(input('Podaj indeks pracownika: '))
            if act == 'r':
                hours = int(input('Podaj liczbę godzin: '))
                registry.register_employees_hours(hours, index)
            else:
                salary = registry.pay_employees_salary(index)
                print(
                    f'Pracownikowi wypłacono {salary:.2f}')
        elif act == 'k':
            break
        else:
            print('Zła akcja!')
