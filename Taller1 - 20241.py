import random

class Persona:
    def __init__(self, id_persona, hora_llegada, tiempo_servicio):
        self.id_persona = id_persona
        self.hora_llegada = hora_llegada
        self.tiempo_servicio = tiempo_servicio
        self.tiempo_espera = 0

    def __str__(self):
        return f"ID Persona: {self.id_persona}, Hora de Llegada: {self.hora_llegada} sec, Tiempo de Servicio: {self.tiempo_servicio} sec, Tiempo de Espera: {self.tiempo_espera} sec"

class Agente:
    def __init__(self, id_agente):
        self.id_agente = id_agente
        self.tiempo_total_ocupado = 0
        self.disponible_desde = 0
        

    def __str__(self):
        return f"ID Agente: {self.id_agente}, Tiempo Total Ocupado: {self.tiempo_total_ocupado} sec"

class Cola:
    def __init__(self):
        self.personas = []

    def encolar(self, persona):
        self.personas.append(persona)

    def desencolar(self):
        return self.personas.pop(0) if self.personas else None

    def esta_vacia(self):
        return len(self.personas) == 0

    def __str__(self):
        return "\n".join(str(persona) for persona in self.personas)


def simular(M, N): #Arreglar que cada agente solo puede atender una persona
    personas = [Persona(i + 1, random.randint(0, 28800), random.randint(300, 3601)) for i in range(M)]
    agentes = [Agente(f'A{i + 1}') for i in range(N)]
    cola = Cola()
    for persona in sorted(personas, key=lambda x: x.hora_llegada):
        cola.encolar(persona)
    
    tiempo_actual = 0
    total_tiempo_espera = 0
    while tiempo_actual < 28800 or not cola.esta_vacia():
        for agente in agentes:
            if agente.disponible_desde <= tiempo_actual and not cola.esta_vacia():
                if cola.personas[0].hora_llegada <= tiempo_actual:
                    persona = cola.desencolar()
                    persona.tiempo_espera = tiempo_actual - persona.hora_llegada
                    total_tiempo_espera += persona.tiempo_espera
                    agente.tiempo_total_ocupado += persona.tiempo_servicio
                    agente.disponible_desde = tiempo_actual + persona.tiempo_servicio
                    print(f"Atendiendo a Persona {persona.id_persona} con tiempo de llegada {persona.hora_llegada}: Por {agente.id_agente}")
        tiempo_actual += 1
    
    for agente in agentes:
        tiempo_total_ocupado = agente.tiempo_total_ocupado
        promedio_ocupacion = (tiempo_total_ocupado / (N * 28800)) * 100 #Arreglar valores de tiempo espera total y %tiempo ocupado
        promedio_espera = total_tiempo_espera / M
        
        print(f'% Tiempo ocupado {agente.id_agente}: {promedio_ocupacion:.2f}%')
    print(f'Tiempo promedio de espera: {promedio_espera} segundos')
    

    print("\nEstado Final de la Cola:")
    print(cola)
    print(f'Tiempo ocupado de agentes: {promedio_ocupacion:.2f}%')
    for agente in agentes:
        print(agente)

    
def optimizar_agentes(M):
    N = 1
    while True:
        promedio_ocupacion, promedio_espera = simular(M, N)
        print(f"Testing with {N} agents: Occupancy = {promedio_ocupacion}%, Average Wait = {promedio_espera} seconds")
        if promedio_ocupacion < 50: 
            N-=1
            if promedio_ocupacion <50 and promedio_espera < 60:
                break
                
        elif promedio_ocupacion > 50:
            N+=1
            if promedio_ocupacion > 50 and promedio_espera < 60:
                break

    return N, promedio_ocupacion, promedio_espera


    

def main():
    M = int(input("Ingrese la cantidad de personas: "))
    N = int(input("Ingrese la cantidad de agentes: "))
    simular(M, N)
    optimizar_agentes(M)
main()
