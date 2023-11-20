class Transport():
    def __init__(self, coordinates, speed, brand, year, number):
        self._coordinates = coordinates
        self._speed = speed
        self._brand = brand
        self._year = year
        self._number = number
        
    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        self._coordinates = coordinates

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        self._speed = speed

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        self._year = year

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number
        
    def __str__(self):
        pass
        
    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        pass


class Passenger():
    def __init__(self, passengers_capacity, number_of_passengers):
        self._passengers_capacity = passengers_capacity
        self._number_of_passengers = number_of_passengers
        
    @property
    def passengers_capacity(self):
        return self._passengers_capacity
        
    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        self._passengers_capacity = passengers_capacity
        
    @property
    def number_of_passengers(self):
        return self._number_of_passengers
        
    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        self._number_of_passengers = number_of_passengers


class Cargo():
    def __init__(self, carrying):
        self._carrying = carrying
        
    @property
    def carrying(self):
        return self._carrying
        
    @carrying.setter
    def carrying(self, carrying):
        self._carrying = carrying


class Plane(Transport):
    def __init__(self, coordinates, speed, brand, year, number, height):
        super().__init__(coordinates, speed, brand, year, number)
        self._height = height
        
    @property
    def height(self):
        return self._height
        
    @height.setter
    def height(self, height):
        self._height = height


class Auto(Transport):
    pass


class Ship(Transport):
    def __init__(self, coordinates, speed, brand, year, number, name, port):
        super().__init__(coordinates, speed, brand, year, number)
        self._name = name
        self._port = port

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        self._port = port


class Car(Auto):
    pass


class Bus(Auto, Passenger):
    pass


class CargoAuto(Auto, Cargo):
    pass


class Boat(Ship):
    pass


class PassengerShip(Ship, Passenger):
    pass


class CargoShip(Ship, Cargo):
    pass


class Seaplane(Plane, Ship):
    pass
