class ElectricCar:
    def __init__(self, range_to_drive):
        self.max_range = range_to_drive
        self.range = range_to_drive

    def drive(self, distance):
        if self.range >= distance:
            self.range -= distance
        else:
            distance = self.range
            self.range = 0
        return distance

    def charge(self):
        self.range = self.max_range


def test_initialize():
    car = ElectricCar(100)
    assert car.range == 100


def test_simple_drive():
    car = ElectricCar(100)

    distance = car.drive(50)

    assert distance == 50


def test_drive_out_of_range():
    car = ElectricCar(100)

    car.drive(70)
    second_distance = car.drive(50)

    assert second_distance == 30


def test_drive_with_charging():
    car = ElectricCar(100)

    car.drive(50)
    car.drive(50)
    third_distance = car.drive(50)
    car.charge()
    fourth_distance = car.drive(80)

    assert third_distance == 0
    assert fourth_distance == 80
