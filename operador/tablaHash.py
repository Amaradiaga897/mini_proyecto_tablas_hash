from .hash import calcularHash
from .operador import Operador
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

    # Función para comprobar el conflicto de Id's duplicados
    # Esto significa mismo Id misma posición

    def buscarIDConMismaPosicion(self, idOriginal):

        posicionOriginal = calcularHash(idOriginal, self.M)

        numero = 1

        while True:

            idPrueba = f'OP-10{numero}'

            if idPrueba != idOriginal:

                posicionPrueba = calcularHash(idPrueba, self.M)

                if posicionPrueba == posicionOriginal:
                    return idPrueba

            numero += 1

    
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

    idOriginal = 'OP-1001'

    idConflicto = tabla.buscarIDConMismaPosicion(idOriginal)

    print('ID original:', idOriginal)
    print('Posición:', calcularHash(idOriginal))

    print('ID conflicto:', idConflicto)
    print('Posición:', calcularHash(idConflicto))

    operador2 = Operador(
    idConflicto,
    'Maria Lopez',
    'maria@gmail.com',
    'abc123'
    )

    tabla.insertar(operador2)