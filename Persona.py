class Persona:
    def __init__(self, id, llegada, servicio):
        self.id = id
        self.llegada = llegada
        self.servicio = servicio
        self.espera = 0  # To be calculated during simulation
