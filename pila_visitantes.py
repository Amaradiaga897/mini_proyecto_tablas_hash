#FUNCIONES DE PILA
def pilaVacia(self):
    if len(self) == 0:
        print('No hay ningún visitante')
    else:
        print('Ya hay autos en el parqueo de visitantes')
        
def pilaLlena(self):
    if len(self) == 9:
        return True

def ingresarVehiculo(self, nombre):
    if not pilaLlena(self):
        self.append(nombre)
        print(f'Se ingresó el vehiculo {nombre} en la posicion {len(self)}')
    else:
        print(f'No se puede ingresar el vehículo {nombre}. El estacionamiento está lleno.')

def sacarVehiculo(self):
    if len(self) > 0:
        print(f'Se retiró el vehiculo {ultimoElemento(self)} del estacionamiento')
        self.pop()
    else:
        pilaVacia()

def ultimoElemento(self):
    if len(self) !=0:
        return self[-1]

def tamanioPila(self):
    print(f'El tamaño de la pila es {len(self)}')
    
def sacarEnMedio(self, posicion):
    pilaAux = []
    if len(self) > 0 and posicion <=len(self):
        while len(self) != posicion:
            ingresarVehiculo(pilaAux,self[-1])
            sacarVehiculo(self)
        sacarVehiculo(self)    
        while len(pilaAux) !=0:
            ingresarVehiculo(self,pilaAux[-1])
            sacarVehiculo(pilaAux)    

    
estacionamiento = []    
ingresarVehiculo(estacionamiento,'Hyundai')
ingresarVehiculo(estacionamiento,'Mazda')
ingresarVehiculo(estacionamiento,'Honda')
ingresarVehiculo(estacionamiento,'Nissan')
ingresarVehiculo(estacionamiento,'Mitsubishi')
ingresarVehiculo(estacionamiento,'Toyota')
ingresarVehiculo(estacionamiento,'Kia')
ingresarVehiculo(estacionamiento,'Daewoo')
ingresarVehiculo(estacionamiento,'Chrysler')
tamanioPila(estacionamiento)
print(estacionamiento)

sacarVehiculo(estacionamiento)
sacarVehiculo(estacionamiento)
sacarVehiculo(estacionamiento)
print(estacionamiento)
ingresarVehiculo(estacionamiento,'Mercedes-Benz')
print(estacionamiento)

sacarEnMedio(estacionamiento, 3)
print(estacionamiento)

sacarEnMedio(estacionamiento, 2)
print(estacionamiento)