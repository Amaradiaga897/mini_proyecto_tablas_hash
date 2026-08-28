class PilaVisitantes:
    capacity = 9

    def __init__(self):
        self.pila = []


    #sirve como un pilaVacia para decir si su tamaño es igual a 0.
    #en caso de tener elementos, los imprime en pantalla
    def mostrarPila(self):
        if len(self.pila) == 0:
            print("El estacionamiento de visitas está vacío.")
            return
        for i in range(len(self.pila), 0, -1):
            print(f'{i}. {self.pila[i - 1]}')


    # devuelve true si el tamaño de la pila es igual a 9
    def pilaLlena(self):
        return len(self.pila) == self.capacity


    # ingresa un vehiculo a la pila solo si hay espacio
    def ingresarVehiculo(self, nombre):
        if not self.pilaLlena():
            self.pila.append(nombre)
            print(f'Se ingresó el vehiculo {nombre} en la posicion {len(self.pila)}')
        else:
            print(f'No se puede ingresar el vehículo {nombre}. El estacionamiento está lleno.')


    #saca el vehiculo (tope) del estacionamiento
    def sacarVehiculo(self):
        if len(self.pila) > 0:
            print(f'Se retiró el vehiculo {self.ultimoElemento()} del estacionamiento.')
            self.pila.pop()
        else:
            self.mostrarPila()


    # devuelve el tope de la pila
    def ultimoElemento(self):
        if len(self.pila) != 0:
            return self.pila[-1]


    # devuelve el tamaño de la pila
    def tamanioPila(self):
        return len(self.pila)


    # mueve el vehiculo de la posicion ingresada al tope de la pila para su salida
    # simula el mover carros fuera del estacionamiento y el reordenarlos para dejar el que nos interesa como el tope
    def moverVehiculo(self, posicion):
        if len(self.pila) == 0 or posicion < 1 or posicion > len(self.pila):
            print('Posición inválida.')
            return
        pilaAux = []
        while len(self.pila) != posicion:
            pilaAux.append(self.pila.pop())
        vehiculo = self.pila.pop()
        while len(pilaAux) != 0:
            self.pila.append(pilaAux.pop())
        self.pila.append(vehiculo)
        print(f'Se reprogramó la salida de {vehiculo}, ahora está en el tope.')
