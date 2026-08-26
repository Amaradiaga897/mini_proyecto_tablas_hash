from operador import Operador
from operador import TablaHash
from infrastructure import ArchivoOperadores
from datetime import datetime


def main():

    # 1. Crear la estructura que se pide M = 13

    tabla = TablaHash(13)

    archivo = ArchivoOperadores('operadores.txt')

    # 2. Se cargaran los operadores que ya han sido guardados
    archivo.cargar(tabla)

    # 3. Aquí va el Login simulado

    idOperador = "OP-1001"

    operador = tabla.buscar(idOperador)


    if operador is None:

        print("El operador no existe.")

        return

    # Simulando que ingreso la contraseña correcta

    print("\n================================")
    print("       LOGIN EXITOSO")
    print("================================")

    print(f"ID:       {operador.id}")
    print(f"Nombre:   {operador.nombre}")
    print(f"Correo:   {operador.correo}")

    # 4. Actualizar último acceso


    operador.ultimoAcceso = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    archivo.actualizar(operador)

    print(f"Último acceso: {operador.ultimoAcceso}")

    menuPrincipal(operador)

def menuPrincipal(operador):

    while True:

        print("\n================================")
        print("     ESTACIONAMIENTO INTELIGENTE")
        print("================================")

        print(f"Operador: {operador.nombre}")
        print()
        print("1. Área de carga y descarga")
        print("2. Estacionamiento de visitantes")
        print("3. Información del operador")
        print("4. Salir")

        opcion = input("\nSeleccione una opción: ")


        if opcion == "1":

            print("\nÁrea de carga y descarga")
            print("Aquí estará la Cola con Prioridad.")


        elif opcion == "2":

            print("\nEstacionamiento de visitantes")
            print("Aquí estará la Pila de Visitantes.")


        elif opcion == "3":

            print("\n========== OPERADOR ==========")
            print(f"ID:       {operador.id}")
            print(f"Nombre:   {operador.nombre}")
            print(f"Correo:   {operador.correo}")
            print(f"Último acceso: {operador.ultimoAcceso}")


        elif opcion == "4":

            print("\nSesión finalizada.")
            break


        else:

            print("\nOpción inválida.")

if __name__ == "__main__":
    main()