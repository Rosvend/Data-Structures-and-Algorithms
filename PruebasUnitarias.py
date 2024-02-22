import math
from Persona import Persona
from SimuladorFilas import SimuladorFila

def igualdadDoubles(a:float, b:float) -> bool:
      return math.fabs(a-b)<1E-10

def testCase1():
    personas:list[Persona] = [ Persona(0, 0, 5) ]
    sim:SimuladorFila = SimuladorFila(1, personas, 10)
    sim.correrSimulation()
    assert igualdadDoubles(sim.getPromedioOcupacion(), 50.0)
    assert igualdadDoubles(sim.getPromedioEspera(), 0.0)

def testCase2():
    personas:list[Persona] = [ Persona(2, 0, 5), Persona(4, 0, 3) ]
    sim:SimuladorFila = SimuladorFila(1, personas, 10)
    sim.correrSimulation()
    assert igualdadDoubles(sim.getPromedioOcupacion(), 80.0)
    assert igualdadDoubles(sim.getPromedioEspera(), 3.0/2)

def testCase3():
    personas:list[Persona] = [ 
        Persona(llegada=0, id=0, servicio=5), 
        Persona(llegada=5, id=1, servicio=5) 
    ]
    sim:SimuladorFila = SimuladorFila(1, personas, 10)
    sim.correrSimulation()
    assert igualdadDoubles(sim.getPromedioOcupacion(), 100.0)
    assert igualdadDoubles(sim.getPromedioEspera(), 0.0)

def testCase4():
    personas:list[Persona] = [ 
        Persona(llegada=0, id=0, servicio=5), 
        Persona(llegada=5, id=1, servicio=5) 
    ]
    sim:SimuladorFila = SimuladorFila(2, personas, 10)
    sim.correrSimulation()
    assert igualdadDoubles(sim.getPromedioOcupacion(), 50.0)
    assert igualdadDoubles(sim.getPromedioEspera(), 0.0)

def testCase5():
    personas:list[Persona] = [ 
        Persona(llegada=0, id=0, servicio=2), 
        Persona(llegada=0, id=1, servicio=2), 
        Persona(llegada=0, id=2, servicio=2) 
    ]
    sim:SimuladorFila = SimuladorFila(1, personas, 10)
    sim.correrSimulation()
    assert igualdadDoubles(sim.getPromedioOcupacion(), 60.0)
    assert igualdadDoubles(sim.getPromedioEspera(), 2.0)


if __name__ == "__main__":
    testCase1()
    testCase2()
    testCase3()
    testCase4()
    testCase5()
