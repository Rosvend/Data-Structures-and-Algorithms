import math

class SimuladorFila:
    def __init__(self, N, personas, max_time):
        self.N = N  # Number of agents
        self.personas = sorted(personas, key=lambda x: x.llegada)  # Ensure personas are sorted by arrival time
        self.max_time = max_time
        self.tiempo_ocupado = 0  # Total occupied time across all agents
        self.total_espera = 0  # Total wait time across all personas

    def correrSimulation(self):
        tiempo_actual = 0
        cola = []
        agentes_ocupados = 0  # Number of currently busy agents

        while tiempo_actual < self.max_time or cola:
            # Release agents if they finished serving at current time
            agentes_ocupados = max(0, agentes_ocupados - 1)

            # Enqueue personas arriving at the current time
            while self.personas and self.personas[0].llegada <= tiempo_actual:
                cola.append(self.personas.pop(0))

            # Assign available agents to waiting personas
            while agentes_ocupados < self.N and cola:
                persona = cola.pop(0)
                self.total_espera += max(0, tiempo_actual - persona.llegada)
                self.tiempo_ocupado += persona.servicio
                agentes_ocupados += 1
                # Simulate serving the persona immediately
                tiempo_actual += persona.servicio

        # Ensure all personas are served
        while cola:
            persona = cola.pop(0)
            self.total_espera += max(0, tiempo_actual - persona.llegada)
            self.tiempo_ocupado += persona.servicio
            tiempo_actual += persona.servicio

    def getPromedioOcupacion(self):
        # Calculate total potential work time for all agents
        total_potential_work_time = self.N * self.max_time
        return (self.tiempo_ocupado / total_potential_work_time) * 100

    def getPromedioEspera(self):
        total_personas_atendidas = len(self.personas)
        return (self.total_espera / total_personas_atendidas) if total_personas_atendidas > 0 else 0
