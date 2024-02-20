import random
import datetime
 

class Persona:
    def __init__(self, id_persona, tiempo_llegada):
        self.id_persona = id_persona
        self.tiempo_llegada = tiempo_llegada
        self.tiempo_servicio = random.randint(300, 3600) #tiempo_servicio
        self.tiempo_espera = datetime.timedelta() #datetime.timedelta() #Inicializa el tiempo
    
    def __str__(self):
        return f"Persona {self.id_persona}: Llegada={self.tiempo_llegada}s, Servicio={self.tiempo_servicio}s, Espera={self.tiempo_espera}s"
        #return f"Id de la persona: {self.id_persona}, Tiempo de llegada:{self.tiempo_llegada.strftime('%Y-%m-%d %H:%M'),Tiempo de servicio:{self.tiempo_servicio} minutos, Tiempo de espera:{self.tiempo_espera.total_seconds()/60:.2f} minutos"  
class Agente:
    def __init__(self):
        self.tiempo_ocupado = 0
    
    def __str__(self):
        return f"Agente: Tiempo Ocupado={self.tiempo_ocupado}s"

class Fila:
    def __init__(self):
        self.personas = []
    
    def agregar_persona(self, persona):
        self.personas.append(persona)
    def desencolar(self):
        return self.personas.pop(0) if self.personas else None
    def actualizar_tiempos_espera(self, tiempo_pasado: datetime.timedelta):
        for persona in self.personas:
            persona.tiempo_espera += tiempo_pasado
    
    def siguiente_persona(self):
        if self.personas:
            return self.personas.pop(0)
        else:
            return None

class Taller1:
    def __init__(self):
        self.personas = []
        self.agentes = []
        self.fila = Fila()

    def inicializar_personas(self, M):
        for i in range(M):
            tiempo_llegada = random.randint(0, 28800)
            persona = Persona(i+1, tiempo_llegada)
            self.personas.append(persona)
            self.fila.agregar_persona(persona)
    
    def inicializar_agentes(self, N):
        for _ in range(N):
            agente = Agente()
            self.agentes.append(agente)
    
    def core_simulacion(self):
        tiempo_actual = 0
        while tiempo_actual <= 28800:
            for agente in self.agentes:
                if tiempo_actual >= agente.tiempo_ocupado:
                    persona_atendida = self.fila.siguiente_persona()
                    if persona_atendida:
                        persona_atendida.tiempo_espera = tiempo_actual - persona_atendida.tiempo_llegada
                        agente.tiempo_ocupado = tiempo_actual + persona_atendida.tiempo_servicio
            tiempo_actual += 1
    
    def obtener_resultados(self):
        tiempo_total_ocupado = sum(agente.tiempo_ocupado for agente in self.agentes)
        tiempo_promedio_espera = sum(persona.tiempo_espera for persona in self.personas) / len(self.personas)
        return tiempo_total_ocupado, tiempo_promedio_espera

# Test
taller = Taller1()
taller.inicializar_personas(10)
taller.inicializar_agentes(2)
taller.core_simulacion()
tiempo_total_ocupado, tiempo_promedio_espera = taller.obtener_resultados()
print(f"Tiempo total ocupado por los agentes: {tiempo_total_ocupado}s")
print(f"Tiempo promedio de espera en la fila: {tiempo_promedio_espera}s")