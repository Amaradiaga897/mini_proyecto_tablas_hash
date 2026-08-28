
from operador import Operador, TablaHash
from infrastructure import ArchivoOperadores
from autenticacion import iniciarSesion
 
from cola_prioridad import colaPrioridad
from pila_visitantes import PilaVisitantes
 
M = 13
CAPACIDAD_CARGA = 7      # límite de la cola de prioridades (área de carga)
 
def menuAreaCarga(cola):
    while True:
        print("\n-------- ÁREA DE CARGA Y DESCARGA (cola con prioridades) --------")
        print("1. Ingresar camión")
        print("2. Sacar camión (finalizó carga / se traslada)")
        print("3. Ver frente de la cola")
        print("4. Ver último de la cola")
        print("5. Ver toda la cola")
        print("6. Volver al menú principal")
 
        opcion = input("Seleccione una opción: ").strip()
 
        if opcion == "1":
            nombre = input("Nombre/placa del camión: ").strip()
            print("Prioridad -> 1: Alta (refrigerados/perecederos)")
            print("             2: Media (carga pesada)")
            print("             3: Baja (documentos/paquetería pequeña)")
            try:
                prioridad = int(input("Prioridad (1-3): ").strip())
            except ValueError:
                print("Prioridad inválida.")
                continue
            if prioridad not in (1, 2, 3):
                print("Prioridad inválida.")
                continue
            cola.ingresar(nombre, prioridad)
 
        elif opcion == "2":
            cola.sacar()
 
        elif opcion == "3":
            print(f"Frente de la cola: {cola.obtenerFrente()}")
 
        elif opcion == "4":
            print(f"Último de la cola: {cola.obtenerUltimo()}")
 
        elif opcion == "5":
            cola.imprimirCola()
 
        elif opcion == "6":
            break
 
        else:
            print("Opción inválida.")
 
 
def menuVisitantes(estacionamiento):
    while True:
        print("\n-------- ESTACIONAMIENTO DE VISITAS - Torre 1 (pila) --------")
        print("1. Ingresar vehículo")
        print("2. Sacar vehículo (retiro normal, tope de la pila)")
        print("3. Ver último vehículo ingresado")
        print("4. Ver tamaño del estacionamiento")
        print("5. Ver todos los vehículos")
        print("6. Reprogramar salida (mover un vehículo dentro de la pila)")
        print("7. Volver al menú principal")
 
        opcion = input("Seleccione una opción: ").strip()
 
        if opcion == "1":
            nombre = input("Nombre/placa del vehículo: ").strip()
            estacionamiento.ingresarVehiculo(nombre)
 
        elif opcion == "2":
            estacionamiento.sacarVehiculo()
 
        elif opcion == "3":
            print(f"Último vehículo: {estacionamiento.ultimoElemento()}")
 
        elif opcion == "4":
            estacionamiento.tamanioPila()
 
        elif opcion == "5":
            estacionamiento.mostrarPila()
 
        elif opcion == "6":
            if len(estacionamiento.pila) == 0:
                print("El estacionamiento está vacío.")
                continue
            print(f"Posiciones actuales (1:fondo ... {estacionamiento.tamanioPila()}:tope):")
            estacionamiento.mostrarPila()
            try:
                posicion = int(input("¿Qué vehículo desea reprogramar? (ingrese su posición): ").strip())
            except ValueError:
                print("Posición inválida.")
                continue
            estacionamiento.moverVehiculo(posicion)
 
        elif opcion == "7":
            break
 
        else:
            print("Opción inválida.")
 
 
def menuPrincipal(operador, cola, estacionamiento):
    while True:
        print("\n================================")
        print("     ESTACIONAMIENTO INTELIGENTE")
        print("================================")
        print(f"Operador: {operador.nombre} ({operador.id})")
        print()
        print("1. Área de carga y descarga")
        print("2. Estacionamiento de visitantes")
        print("3. Información del operador")
        print("4. Cerrar sesión / Salir")
 
        opcion = input("\nSeleccione una opción: ").strip()
 
        if opcion == "1":
            menuAreaCarga(cola)
 
        elif opcion == "2":
            menuVisitantes(estacionamiento)
 
        elif opcion == "3":
            print("\n========== OPERADOR ==========")
            print(f"ID:            {operador.id}")
            print(f"Nombre:        {operador.nombre}")
            print(f"Correo:        {operador.correo}")
            print(f"Último acceso: {operador.ultimoAcceso}")
 
        elif opcion == "4":
            print("\nSesión finalizada.")
            break
 
        else:
            print("\nOpción inválida.")
 
 
def main():
    tabla = TablaHash(M)
    archivo = ArchivoOperadores('operadores.txt')
    archivo.cargar(tabla)
 
    operador = None
    while operador is None:
        operador = iniciarSesion(tabla, archivo)
        if operador is None:
            reintentar = input("\n¿Desea intentarlo de nuevo? (s/n): ").strip().lower()
            if reintentar != 's':
                print("Saliendo del sistema.")
                return
 
    # Estructuras de datos de los vehículos, vivas durante la sesión.
    colaCarga = colaPrioridad(CAPACIDAD_CARGA)
    estacionamientoVisitas = PilaVisitantes()
 
    menuPrincipal(operador, colaCarga, estacionamientoVisitas)
 
 
if __name__ == "__main__":
    main()
 