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
            self.overtime_worked += (hours - 8)


class PremiumEmployee(Employee):
    def __init__(self, firstname, lastname, salary_per_hour):
        super().__init__(firstname, lastname, salary_per_hour)
        self.bonus = 0

    def give_bonus(self, bonus):
        self.bonus += bonus

    def pay_salary(self):
        salary = super().pay_salary() + self.bonus
        self.bonus = 0
        return salary


class EmployeeWithBonuses(Employee):
    def __init__(self, firstname, lastname, salary_per_hour):
        super().__init__(firstname, lastname, salary_per_hour)
        self.bonus_type = None

    def set_bonus_type(self, bonus_type):
        self.bonus_type = bonus_type

    def pay_salary(self):
        salary = super().pay_salary()
        if self.bonus_type:
            bonus = self.bonus_type.calculate_bonus(salary)
        else:
            bonus = 0.0
        return salary + bonus


class Bonus:
    def calculate_bonus(self, salary: float) -> float:
        raise NotImplementedError()


class BonusFor10k(Bonus):
    def calculate_bonus(self, salary):
        if salary >= 10000.0:
            return 1000.0
        else:
            return 0.0


class Bonus5PercentFor5k(Bonus):
    def calculate_bonus(self, salary):
        if salary >= 5000.0:
            return salary * 0.05
        else:
            return 0.0


def test_employee_with_bonuses_1k_above_10k():
    emp = EmployeeWithBonuses('Jan', 'Kowalski', 1000.00)
    emp.register_time(5)
    emp.register_time(5)

    emp.set_bonus_type(BonusFor10k())

    assert emp.pay_salary() == 11000.00


def test_employee_with_bonuses_5_percent_above_5k():
    emp = EmployeeWithBonuses('Jan', 'Kowalski', 1000.00)
    emp.register_time(5)

    emp.set_bonus_type(Bonus5PercentFor5k())

    assert emp.pay_salary() == 5250.00


def test_premium_employee():
    emp = PremiumEmployee('Jan', 'Kowalski', 100.00)
    emp.register_time(10)

    emp.give_bonus(300)
    emp.give_bonus(500)

    salary1 = emp.pay_salary()
    salary2 = emp.pay_salary()

    assert salary1 == 2000.00
    assert salary2 == 0.0


def test_employee_init():
    emp = Employee('Jan', 'Nowak', 100.00)

    assert emp.firstname == 'Jan'
    assert emp.lastname == 'Nowak'
    assert emp.salary_per_hour == 100.00


def test_salary_normal_hours():
    emp = Employee('Jan', 'Nowak', 100.00)

    emp.register_time(5)

    assert emp.pay_salary() == 500.0
    assert emp.pay_salary() == 0.0


def test_salary_overtime():
    emp = Employee('Jan', 'Nowak', 100.00)

    emp.register_time(10)

    assert emp.pay_salary() == 1200.0
    assert emp.pay_salary() == 0.0


def test_multiple_registrations():
    emp = Employee('Jan', 'Nowak', 100.00)

    emp.register_time(10)
    emp.register_time(10)
    emp.register_time(6)

    assert emp.pay_salary() == 3000.0
    assert emp.pay_salary() == 0.0
