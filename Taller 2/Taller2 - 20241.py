class Person:
    """
    Implementacion ADT Persona
    """
    def __init__(self, person_id, x_coordinate, y_coordinate):
        self.station = None
        self.id = person_id
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def method1(self):
        """
        Metodo 1
        """
        

    def method2(self):
        """
        Metodo 2.
        """
        


class Station:
    """
    Implementacion ADT Estacion
    """

    def __init__(self, name, distance, x_coordinate, y_coordinate):
        self.name = name
        self.distance = distance
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def method1(self):
        """
        Metodo 1 
        """
        

    def method2(self):
        """
        Metodo 2.
        """
        


N = int(input('Por favor ingrese la cantidad de personas:  '))
M = int(input('Por favor ingrese la cantidad de estaciones:  '))

people = []
stations = []

for i in range(N):
    person_id = input('Ingrese el ID de la persona: ')
    x_coordinate = float(input('Ingrese la coordenada X de la persona: '))
    y_coordinate = float(input('Ingrese la coordenada Y de la persona: '))
    person = Person(person_id, x_coordinate, y_coordinate)
    people.append(person)

for i in range(M):
    name = input('Ingrese el nombre de la estación: ')
    distance = float(input('Ingrese la distancia de la estación: '))
    x_coordinate = float(input('Ingrese la coordenada X de la estación: '))
    y_coordinate = float(input('Ingrese la coordenada Y de la estación: '))
    station = Station(name, distance, x_coordinate, y_coordinate)
    stations.append(station)

