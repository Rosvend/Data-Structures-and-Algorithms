import datetime
import random

class Persona:
    def __init__(self, id_persona, hora_llegada: datetime.datetime, tiempo_servicio,tiempo_espera):
        self.id_persona = id_persona
        self.hora_llegada = hora_llegada
        self.tiempo_servicio = tiempo_servicio  
        self.tiempo_espera = datetime.timedelta()  

    def __str__(self):
        return f"ID Persona: {self.id_persona}, Hora de Llegada: {self.hora_llegada.strftime('%Y-%m-%d %H:%M')}, Tiempo de Servicio: {self.tiempo_servicio} mins, Tiempo de Espera: {self.tiempo_espera.total_seconds()/60:.2f} mins"

class Agente:
    def __init__(self, id_agente):
        self.id_agente = id_agente
        self.tiempo_total_ocupado = datetime.timedelta()  
    

    def atender(self,persona):
        print(f"Atendiendo a {persona} por {self.id_agente}")
        self.tiempo_total_ocupado = persona.tiempo_servicio
        return self.tiempo_total_ocupado

    def __str__(self):
        return f"ID Agente: {self.id_agente}, Tiempo Total Ocupado: {self.tiempo_total_ocupado.total_seconds()/60:.2f} mins"

class Cola:
    def __init__(self):
        self.personas = []

    def encolar(self, persona):
        self.personas.append(persona)

    def desencolar(self):
        return self.personas.pop(0) if self.personas else None

    def actualizar_tiempos_espera(self, tiempo_pasado: datetime.timedelta):
        for persona in self.personas:
            persona.tiempo_espera += tiempo_pasado

    def __str__(self):
        return "\n".join(str(persona) for persona in self.personas)

def simular_sistema_servicio(M,N):
    for i in range(0,28800):
    # Simulación con manejo de tiempo y múltiples N
        cola_servicio = Cola()
        NAgentes = []

        agente1.atender(persona)
        

        

        while cola_servicio.personas:
            for agente in NAgentes:
                if not cola_servicio.personas:
                    break
                persona_actual = cola_servicio.desencolar()
                print(f"Atendiendo a {persona_actual} por {agente.id_agente}")
                agente.tiempo_total_ocupado += datetime.timedelta(minutes=persona_actual.tiempo_servicio)
                cola_servicio.actualizar_tiempos_espera(datetime.timedelta(minutes=persona_actual.tiempo_servicio))

        # Estado final de la cola y los N
        print("Estado Final de la Cola:")
        print(cola_servicio)
        for agente in NAgentes:
            print("Estado del Agente:", agente)


def main():
    M = int(input("Ingrese la cantidad de personas: "))
    N = int(input("Ingrese la cantidad de agentes: "))

    cola_servicio = Cola()
    NAgentes = []  # Múltiples N

    for i in range(0,M+1):  
        persona1 = Persona(i + 1, random.randint(0, 28800), random.randint(300, 3601),0)
        cola_servicio.encolar(persona1)

    for i in range(0,N+1):
        agente = Agente('A'+str(i+1)+'')
        NAgentes.append(agente)

    simular_sistema_servicio(M,N)


main()