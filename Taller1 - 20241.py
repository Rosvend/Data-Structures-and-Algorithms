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

def simular(M, N):
    personas = [Persona(i + 1, random.randint(0, 28800), random.randint(300, 3601)) for i in range(M)]
    agentes = [Agente(f'A{i + 1}') for i in range(N)]
    cola = Cola()
    for persona in sorted(personas, key=lambda x: x.hora_llegada):
        cola.encolar(persona)
    
    tiempo_actual = 0
    while tiempo_actual < 28800 or not cola.esta_vacia():
        for agente in agentes:
            if agente.disponible_desde <= tiempo_actual and not cola.esta_vacia():
                if cola.personas[0].hora_llegada <= tiempo_actual:
                    persona = cola.desencolar()
                    persona.tiempo_espera = tiempo_actual - persona.hora_llegada
                    agente.tiempo_total_ocupado += persona.tiempo_servicio
                    agente.disponible_desde = tiempo_actual + persona.tiempo_servicio
                    print(f"Atendiendo a ID Persona: {persona.id_persona} por {agente.id_agente}")
        tiempo_actual += 1

    # Print final states
    print("\nEstado Final de la Cola:")
    print(cola)
    for agente in agentes:
        print(agente)

def main():
    M = int(input("Ingrese la cantidad de personas: "))
    N = int(input("Ingrese la cantidad de agentes: "))
    simular(M, N)

main()
