import random
class Person:
    """
    Implementacion ADT Persona
    """
    def __init__(self, person_id, x_coordinate, y_coordinate):
        self.station = None
        self.id = person_id
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate


class Station:
    """
    Implementacion ADT Estacion
    """

    def __init__(self, name, x_coordinate, y_coordinate):
        self.name = name
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

        

def taller2():
    people = []
    stations = []
    
    
    N = int(input('Por favor ingrese la cantidad de personas:  '))
    M = int(input('Por favor ingrese la cantidad de estaciones:  '))

    
    for i in range(N):
        person_id = input('Ingrese el ID de la persona: ')
        x_coordinate = randint(0, 10000)
        y_coordinate = randint(0, 10000)
        person = Person(person_id, x_coordinate, y_coordinate)
        people.append(person)

    for i in range(M):
        name = input('Ingrese el nombre de la estación: ')
        x_coordinate = randint(0, 10000)
        y_coordinate = randint(0, 10000)
        station = Station(name, distance, x_coordinate, y_coordinate)
        stations.append(station)

def assign_stations():
    for person in people:
        min_distance = float('inf')
        for station in stations:
            distance = ((person.x_coordinate - station.x_coordinate) ** 2 + (person.y_coordinate - station.y_coordinate) ** 2) ** 0.5
            if distance < min_distance:
                min_distance = distance
                person.station = station

taller2()