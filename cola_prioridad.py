class Camion:
    def __init__(self, nombre, prioridad):
            self.nombre = nombre
            self.prioridad = prioridad

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
        nuevo_nodo = Camion(nombre,prioridad)
        if self.estaLlena():
            print("El camión no puede entrar a la zona de carga en este momento. Intentelo más tarde")
        else:
            if prioridad == 3:
                    self.arr[self.size] = nuevo_nodo
            elif prioridad == 2 or prioridad == 1:
                pos = 0
                while pos < self.size and self.arr[pos].prioridad == True:
                    pos += 1
                i = self.size
                while i > pos:
                    self.arr[i] = self.arr[i-1]
                    i -= 1
                self.arr[pos] = nuevo_nodo
            self.size += 1

    def sacar(self):
        if self.estaVacia():
            print("¡No hay Camiones en cola!")
            return
        for i in range(1, self.size):
            self.arr[i - 1] = self.arr[i]
        self.size -= 1

    def obtenerFrente(self):
        if self.estaVacia():
            print("¡No hay Camiones en cola!")
            return -1
        return self.arr[0].nombre
        
    def obtenerUltimo(self):
        if self.estaVacia():
           print("¡No hay Camiones en cola!")
           return -1
        return self.arr[self.size - 1].nombre
    
    def imprimirCola(self):
        if self.estaVacia():
           print("¡No hay Camiones en cola!")
           return -1
        else: 
            for i in range(1, self.size+1):
                print(self.arr[i - 1].nombre, self.arr[i - 1].prioridad)

if __name__ == '__main__':
    q = colaPrioridad(6)

    q.ingresar('refrigerados/perecederos', 1)
    q.ingresar('documentos/paquetería pequeña', 3)
    q.ingresar('carga pesada', 2)
    q.ingresar('documentos/paquetería pequeña', 3)
    q.ingresar('refrigerados/perecederos', 1)
    q.ingresar('carga pesada', 2)
    q.ingresar('carga pesada', 2)
    q.imprimirCola()
    
    print(f'frente: {q.obtenerFrente()}')
    
    q.imprimirCola()

    q.sacar()
    
    q.imprimirCola()

    print(f'frente: {q.obtenerFrente()}')

    print(f'ultimo: {q.obtenerUltimo()}')