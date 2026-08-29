from datetime import datetime

class Camion:
    def __init__(self, nombre, prioridad):
            self.nombre = nombre
            self.prioridad = prioridad
            self.horaIngreso = datetime.now()

class colaPrioridad:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [0] * capacity
        self.size = 0

    def estaVacia(self):
        return self.size == 0

    def estaLlena(self):
        return self.size == self.capacity

    def ingresar(self, nombre, prioridad):
        self.reasignarPrioridad()
        nuevo_nodo = Camion(nombre,prioridad)
        if self.estaLlena():
            print("El camión no puede entrar a la zona de carga en este momento. Intentelo más tarde")
        else:
            if prioridad == 3:
                    self.arr[self.size] = nuevo_nodo
            elif prioridad == 2 or prioridad == 1:
                pos = 0
                while pos < self.size and self.arr[pos].prioridad <= prioridad:
                    pos += 1
                i = self.size
                while i > pos:
                    self.arr[i] = self.arr[i-1]
                    i -= 1
                self.arr[pos] = nuevo_nodo
            self.size += 1
            
    def reasignarPrioridad(self):
        ahora = datetime.now()
        i = 0
        while i < self.size:
            camion = self.arr[i]
            tiempoEspera = (ahora - camion.horaIngreso).total_seconds()
            if (tiempoEspera >= 300 and camion.prioridad == 3) or (tiempoEspera >= 180 and camion.prioridad == 2):
                for j in range(i, self.size - 1):
                    self.arr[j] = self.arr[j + 1]
                self.size -= 1

                camion.prioridad -= 1

                pos = 0
                while pos < self.size and self.arr[pos].prioridad <= camion.prioridad:
                    pos += 1

                for j in range(self.size, pos, -1):
                    self.arr[j] = self.arr[j - 1]
                self.arr[pos] = camion
                self.size += 1
                i=0
            else:
                i+=1

    def sacar(self):
        if self.estaVacia():
            print("¡No hay Camiones en cola!")
            return
        for i in range(1, self.size):
            print(f'Se retiró el camión {self.arr[0].nombre} (Prioridad: {self.arr[0].prioridad}) de la cola de carga/descarga.')
            self.arr[i - 1] = self.arr[i]
        self.size -= 1

    def obtenerFrente(self):
        self.reasignarPrioridad()
        if self.estaVacia():
            print("¡No hay Camiones en cola!")
            return -1
        return self.arr[0].nombre
        
    def obtenerUltimo(self):
        self.reasignarPrioridad()
        if self.estaVacia():
           print("¡No hay Camiones en cola!")
           return -1
        return self.arr[self.size - 1].nombre
    
    def imprimirCola(self):
        self.reasignarPrioridad()
        if self.estaVacia():
           print("¡No hay Camiones en cola!")
           return -1
        else: 
            for i in range(1, self.size+1):
                print(f'{i}. {self.arr[i - 1].nombre} (Prioridad: {self.arr[i - 1].prioridad})')