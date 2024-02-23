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

class taller1:
    def simular(M, N):
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
            tiempo_actual += 1

        total_ocupado = sum(agente.tiempo_total_ocupado for agente in agentes)
        promedio_ocupacion = (total_ocupado / (N * 28800)) * 100
        promedio_espera = total_tiempo_espera / M

        return promedio_ocupacion, promedio_espera

def optimizar_agentes(M):
    N = 1  # Start with 1 agent
    while True:
        promedio_ocupacion, promedio_espera = taller1.simular(M, N)
        print(f"Testing with {N} agents: Occupancy = {promedio_ocupacion}%, Average Wait = {promedio_espera} seconds")
        if promedio_ocupacion > 50 and promedio_espera < 60:
            break
        N += 1
    return N, promedio_ocupacion, promedio_espera

def main():
    taller1 = taller1()
    M = int(input("Ingrese la cantidad de personas: "))
    N_optimo, ocupacion, espera = taller1.optimizar_agentes(M)
    print(f"Número óptimo de agentes: {N_optimo}")
    print(f"Porcentaje de ocupación: {ocupacion}%")
    print(f'Tiempo medio de espera: {espera} segundos')
