class SimuladorFila:
    def __init__(self, N, personas, max_time):
        self.N = N
        self.personas = sorted(personas, key=lambda x: x.llegada)
        self.max_time = max_time
        self.tiempo_ocupado = [0] * N  # Track occupation tim e for each agent
        self.tiempo_inicio = [0] * N  # Track start time for each agent's next available moment
        self.total_espera = 0

    def correrSimulation(self):
        # Initialize simulation variables
        cola = []

        # Run simulation
        for t in range(self.max_time + 1):
            # Add new arrivals to queue
            while self.personas and self.personas[0].llegada == t:
                cola.append(self.personas.pop(0))
            
            # Assign agents to personas in queue if available
            for i in range(self.N):
                if t >= self.tiempo_inicio[i] and cola:
                    persona = cola.pop(0)
                    self.total_espera += t - persona.llegada
                    self.tiempo_ocupado[i] += persona.servicio
                    self.tiempo_inicio[i] = t + persona.servicio

        # Calculate total occupied time
        self.total_tiempo_ocupado = sum(self.tiempo_ocupado)

    def getPromedioOcupacion(self):
        cola = []  # Declare the variable "cola"
        total_personas = len(self.personas) + len(cola)
        return (self.total_espera / total_personas) if total_personas > 0 else 0
