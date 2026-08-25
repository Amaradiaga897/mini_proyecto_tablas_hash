from hash import calcularHash
from operador import Operador
class TablaHash:

    def __init__(self, M=13):
        self.M = M
        self.tabla = [None] * M

    def insertar(self, operador):

        posicion = calcularHash(operador.id, self.M)

        if self.tabla[posicion] is None:

            self.tabla[posicion] = operador

            print(
                f'Operador {operador.id} almacenado '
                f'en la posición {posicion}.'
            )

            return True

        print(
            f'Conflicto de hash: la posición {posicion} '
            f'ya está ocupada por {self.tabla[posicion].id}.'
        )

        return False

    def buscar(self, id):
    
        posicion = calcularHash(id, self.M)

        operador = self.tabla[posicion]

        if operador is not None and operador.id == id:
            return operador

        return None

    def mostrarTabla(self):

        print('\n========== TABLA HASH ==========')

        for posicion in range(self.M):

            operador = self.tabla[posicion]

            if operador is None:

                print(f'[{posicion}] -> VACIO')

            else:

                print(
                    f'[{posicion}] -> '
                    f'{operador.id} | '
                    f'{operador.nombre}'
                )

        print('================================\n')

    
if __name__ == '__main__':
    tabla = TablaHash()

    operador1 = Operador(
    'OP-1001',
    'Juan Perez',
    'juan@gmail.com',
    '12345'
    )

    resultado = tabla.insertar(operador1)

    tabla.mostrarTabla()

    operador = tabla.buscar('OP-1001')

    if operador is not None:

        print('Operador encontrado:')
        print('ID:', operador.id)
        print('Nombre:', operador.nombre)
        print('Correo:', operador.correo)

    else:

        print('Operador no encontrado.')