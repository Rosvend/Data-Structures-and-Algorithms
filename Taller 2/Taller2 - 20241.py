from random import randint
from math import sqrt
import time

class Person:
    """
    Implementación ADT Persona
    """
    def __init__(self, person_id, x_coordinate, y_coordinate):
        self.station = None
        self.id = person_id
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate


class Station:
    """
    Implementación ADT Estación
    """

    def __init__(self, name, x_coordinate, y_coordinate):
        self.name = name
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

        

def taller2():
    """
    Función para iniciar el programa
    """
    people = []
    stations = []
    
    
    N = int(input('Por favor ingrese la cantidad de personas:  '))
    M = int(input('Por favor ingrese la cantidad de estaciones:  '))

    
    for i in range(N):
        person_id = f'Person_{i}'
        x_coordinate = randint(0, 10000) #Se asignan coordenadas aleatorias para X y Y entre 0 y 10000 metros el plano
        y_coordinate = randint(0, 10000)
        person = Person(person_id, x_coordinate, y_coordinate)
        people.append(person)

    for i in range(M):
        name = f'Station_{i}'
        x_coordinate = randint(0, 10000) #Se asignan coordenadas aleatorias X y Y entre 0 y 10000 para las estaciones
        y_coordinate = randint(0, 10000)
        station = Station(name, x_coordinate, y_coordinate)
        stations.append(station)
    
    return people, stations


def generar_adts(N,M):
    """
    Función para crear personas y estaciones sin preguntar al usuario (solo se usa en  funcion @medirTiempo)
    
    Args:
        N (int): Numero de personas a crear 
        M (int): Numero de estaciones a crear
    """
    people = []
    stations = []
    
    for i in range(N):
        person_id = f'Person_{i}'
        x_coordinate = randint(0, 10000) #Se asignan coordenadas aleatorias para X y Y entre 0 y 10000 metros el plano
        y_coordinate = randint(0, 10000)
        person = Person(person_id, x_coordinate, y_coordinate)
        people.append(person)

    for i in range(M):
        name = f'Station_{i}'
        x_coordinate = randint(0, 10000) #Se asignan coordenadas aleatorias X y Y entre 0 y 10000 para las estaciones
        y_coordinate = randint(0, 10000)
        station = Station(name, x_coordinate, y_coordinate)
        stations.append(station)
    
    return people, stations

def asignarEstaciones(people,stations):
    """
    Función biblioteca que asigna la estación mas cercana a cada persona
    """
    for person in people:
        min_distance = float('inf') #Numero infinito
        for station in stations:
            distance = sqrt((person.x_coordinate - station.x_coordinate) ** 2 + (person.y_coordinate - station.y_coordinate) ** 2) #Distancia euclidiana entre 2 puntos
            if distance < min_distance:
                min_distance = distance
                person.station = station #Se verifica que sea la distancia mas corta y se le asigna la estación a la persona

def medirTiempo(N,M,k):
    """Calcular tiempo promedio por cada vez que se corre el programa

    Args:
        N (list): Numero de personas
        M (list): Numero de estaciones
        k (int): Numero de veces que se corre el programa
    """
    tiempo_total = 0
    people, stations = generar_adts(N,M) #Se crean instancias de personas y estaciones sin preguntar al usuario cada vez que se corre el programa

    for i in range(k):
        start_time = time.time()
        asignarEstaciones(people,stations)
        end_time = time.time()
        tiempo_total += end_time - start_time
    tiempo_promedio = tiempo_total / k
    print(f'Tiempo promedio para N = {N} y M = {M} es {tiempo_promedio} segundos')


medirTiempo(100,100,100)
