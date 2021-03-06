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

RAM = simpy.Container(env, init=200, capacity=200)
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
def procesoMortal(numProcesos):
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


    print("El n??mero de unidades de tiempo es de: ", CPU.tiempo)
    return CPU.tiempo

op =2
while op != 0:
    print("Elige una de las siguientes opciones: ")
    print("1. Simulacion")
    print("2. Estad??sticas")
    print("3. Salida")

    op = int(input("Elige la opcion que deseas: "))

    if op == 1:
        final = procesoMortal(numProcesos)
        print(final)
    elif op == 2:
        num1 = procesoMortal(numProcesos)
        num2 = procesoMortal(numProcesos)
        num3 = procesoMortal(numProcesos)
        num4 = procesoMortal(numProcesos)
        num5 = procesoMortal(numProcesos)

        numFinal = (num1 + num2 + num3 + num4 + num5) / 5

        print("La media es de: ", numFinal)
    elif op == 3:
        print("Saliendo...")
        op = 0;
    else:
        print("Equivocado intente de nuevo")

