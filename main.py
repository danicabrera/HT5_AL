# This is a sample Python script.
from random import *


import simpy
import math

class proceso():
    instrucciones = randint(0, 10)
    estado = "New"
    memoriaNecesitada = randint(0, 10)

    def setInstruc(self, instruc):
        self.instrucciones = instruc

    def setEstado(self, nuevo):
        self.estado = nuevo

class procesador():
    numInstrucciones = 3
    tiempo = 0

    def modificar(self, ins):
        self.numInstrucciones = ins



env = simpy.core.Environment(initial_time=0)

RAM = simpy.Container(env, init=100, capacity=100)
numProcesos = int(input("Ingrese el numero de procesos a hacer: "))
waitList = []
readyList = []

def crearProceso():
    process = proceso()
    return process

CPU = procesador()
CPU.numInstrucciones = int(input("Ingrese el numero de capacidad del procesador: "))
def asignar(numero):

    for i in range(numero):
        procesoN = crearProceso()
        numRand = randint(0, 10)
        procesoN.setInstruc(numRand)
        if procesoN.memoriaNecesitada != 0:
            if procesoN.memoriaNecesitada > RAM.capacity:
                print("No hay suficiente espacio en memoria.")
            else:
                procesoN.estado = "Ready"
                readyList.append(procesoN)
                RAM.get(procesoN.memoriaNecesitada)

asignar(numProcesos)

while(numProcesos>0):
    procesoActual = proceso()
    procesoNext = proceso()
    ##Proceso del procesador
    try:
        procesoNext = readyList.pop()
        procesoNext.estado = "Waiting"
        waitList.append(procesoNext)
    except:
        asignar(1)

    try:
        procesoActual = waitList.pop()
        procesoActual.estado = "Running"
    except:
        print("No hay en waitlist")


    instrucRestantes = procesoActual.instrucciones - CPU.numInstrucciones
    CPU.tiempo = CPU.tiempo + 1
    if(instrucRestantes <= 0):
        procesoActual.instrucciones = instrucRestantes
        procesoActual.estado = "Terminated"
        RAM.put(procesoActual.memoriaNecesitada)
        numProcesos = numProcesos - 1
    else:
        procesoActual.instrucciones = instrucRestantes
        decis = randint(1, 2)
        if decis == 1:
            procesoActual.estado = "Waiting"
            waitList.append(procesoActual)
        else:
            procesoActual.estado = "Ready"
            readyList.append(procesoActual)


print("El número de unidades de tiempo es de: ", CPU.tiempo)
