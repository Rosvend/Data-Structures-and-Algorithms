#Roy Sandoval 00516163, Miguel Carrillo, Stefany Morelos.
import random

class Persona: #Constructor ADT persona
    def __init__(self, id_persona, hora_llegada, tiempo_servicio):
        self.id_persona = id_persona
        self.hora_llegada = hora_llegada
        self.tiempo_servicio = tiempo_servicio
        self.tiempo_espera = 0

    def __str__(self): #to string persona
        return f"ID Persona: {self.id_persona}, Hora de Llegada: {self.hora_llegada} sec, Tiempo de Servicio: {self.tiempo_servicio} sec, Tiempo de Espera: {self.tiempo_espera} sec"

class Agente: #Implementacion ADT Agente
    def __init__(self, id_agente):
        self.id_agente = id_agente
        self.tiempo_total_ocupado = 0 #los agentes empiezan con tiempo ocupado 0
        self.disponible_desde = 0 #todos los agentes empiezan disponibles
        

    def __str__(self): #to string agente
        return f"ID Agente: {self.id_agente}, Tiempo Total Ocupado: {self.tiempo_total_ocupado} sec"

class Cola: #Implementacion adt Cola o Fila
    def __init__(self):
        self.personas = [] #Se crea una lista con las personas de la fila

    def encolar(self, persona): #agrega persona a la fila
        self.personas.append(persona)

    def desencolar(self): #persona se va de la fila
        return self.personas.pop(0) if self.personas else None

    def esta_vacia(self):
        return len(self.personas) == 0

    def __str__(self):
        return "\n".join(str(persona) for persona in self.personas)


def simular(M, N): #Simula el comportamiento de la fila y los agentes
    personas = [Persona(i + 1, random.randint(0, 28800), random.randint(300, 3601)) for i in range(M)] #Se le asigna un id, tiempo de llegada random y tiempo de servicio random
    agentes = [Agente(f'A{i + 1}') for i in range(N)] #se crean N agentes
    cola = Cola() #se crea la cola
    for persona in sorted(personas, key=lambda x: x.hora_llegada): #se organizan las personas por tiempo de llegada
        cola.encolar(persona)
    
    tiempo_actual = 0 #inicia el dia de trabajo
    total_tiempo_espera = 0 #tiempo de espera de las personas empieza en 0
    while tiempo_actual < 28800 or not cola.esta_vacia(): #verifica que se pueda trabajar
        for agente in agentes:
            if agente.disponible_desde <= tiempo_actual and not cola.esta_vacia(): #verifica que el agente este disponible y que haya personas en la fila
                if cola.personas[0].hora_llegada <= tiempo_actual: #empieza con la primera persona de la fila
                    persona = cola.desencolar() #la quita de la fila
                    persona.tiempo_espera = tiempo_actual - persona.hora_llegada
                    total_tiempo_espera += persona.tiempo_espera
                    agente.tiempo_total_ocupado += persona.tiempo_servicio
                    agente.disponible_desde = tiempo_actual + persona.tiempo_servicio
                    print(f"Atendiendo a Persona {persona.id_persona} con tiempo de llegada {persona.hora_llegada} y tiempo de servicio {persona.tiempo_servicio}: Por {agente.id_agente}")
        tiempo_actual += 1
    
    for agente in agentes:
        tiempo_total_ocupado = agente.tiempo_total_ocupado
        promedio_ocupacion = (tiempo_total_ocupado / (N * 28800)) * 100 
        promedio_espera = total_tiempo_espera / M
        
        print(f'% Tiempo ocupado {agente.id_agente}: {promedio_ocupacion:.2f}%')
    print(f'Tiempo promedio de espera: {promedio_espera} segundos')
    

    print("\nEstado Final de la Cola:")
    print(cola)
    print(f'Tiempo promedio ocupado de agentes: {promedio_ocupacion:.2f}%')
    for agente in agentes:
        print(agente)
    
    return promedio_ocupacion, promedio_espera

    
def optimizar_agentes():
    M = int(input('Por favor indique el numero de personas para el cual desea optimizar el numero de agentes: '))
    N=M
    while True:
        promedio_ocupacion, promedio_espera = simular(M, N)
        print(f"Probando con {N} agentes: Promedio tiempo ocupado = {promedio_ocupacion}%, Tiempo de espera promedio = {promedio_espera} segundos")
      
        if promedio_espera <= 60 and promedio_ocupacion >50:
            print(f"El numero optimo de agentes es : {N}, Tiempo ocupado promedio: {promedio_ocupacion}%, Tiempo espera promedio: {promedio_espera} segundos")
            break
        else:
            N -= 1
            if N <= 0:
                print("No se pudo encontrar un numero optimo de agentes")
                break


    

def main():
    M = int(input("Ingrese la cantidad de personas: "))
    N = int(input("Ingrese la cantidad de agentes: "))
    simular(M, N)
main()
