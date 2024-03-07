from random import randint
from math import sqrt
import time

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
    """
    Funcion para iniciar el programa
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

def asignarEstaciones(people,stations):
    """
    Funcion biblioteca que asigna la estacion mas cercana a cada persona
    """
    for person in people:
        min_distance = float('inf') #Numero infinito
        for station in stations:
            distance = sqrt((person.x_coordinate - station.x_coordinate) ** 2 + (person.y_coordinate - station.y_coordinate) ** 2) #Distancia euclidiana entre 2 puntos
            if distance < min_distance:
                min_distance = distance
                person.station = station #Se verifica que sea la distancia mas corta y se le asigna la estacion a la persona

def medirTiempo(N,M,k):
    """Calcular tiempo promedio por cada vez que se corre el programa

    Args:
        N (list): Numero de personas
        M (list): Numero de estaciones
        k (int): Numero de veces que se corre el programa
    """
    tiempo_total = 0
    for _ in range(k):
        people, stations = taller2() #Revisar esta parte
        start_time = time.time()
        asignarEstaciones(people,stations)
        end_time = time.time()
        tiempo_total += end_time - start_time
    tiempo_promedio = tiempo_total / k
    print(f'Tiempo promedio para N = {N} y M = {M} es {tiempo_promedio} segundos')


medirTiempo(10,10,10)