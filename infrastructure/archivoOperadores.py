from operador import Operador
from operador.tablaHash import TablaHash


class ArchivoOperadores:

    def __init__(self, nombreArchivo: str = "operadores.txt"):

        self.nombreArchivo = nombreArchivo


    def guardar(self, operador: Operador):

        with open(self.nombreArchivo, "a", encoding="utf-8") as archivo:

            archivo.write(str(operador) + "\n")


    def cargar(self, tabla: TablaHash):

        try:

            with open(self.nombreArchivo, "r", encoding="utf-8") as archivo:

                for linea in archivo:

                    linea = linea.strip()

                    if not linea:
                        continue

                    datos = linea.split("|")

                    if len(datos) < 4:
                        continue

                    operador = Operador(
                        datos[0] if len(datos) > 0 else None,
                        datos[1] if len(datos) > 1 else None,
                        datos[2] if len(datos) > 2 else None,
                        datos[3] if len(datos) > 3 else None,
                        datos[4] if len(datos) > 4 and datos[4] != '' and datos[4] != 'None' else None
                    )

                    tabla.insertar(operador)

        except FileNotFoundError:

            # Si el archivo todavía no existe,
            # simplemente no hay operadores que cargar.
            pass


    def actualizar(self, operador: Operador):

        try:

            with open(
                self.nombreArchivo,
                "r",
                encoding="utf-8"
            ) as archivo:

                lineas = archivo.readlines()

        except FileNotFoundError:

            return False


        actualizado = False

        for i in range(len(lineas)):

            linea = lineas[i].strip()

            if not linea:
                continue

            datos = linea.split("|")

            if len(datos) < 4:
                continue

            if datos[0] == operador.id:

                lineas[i] = str(operador) + "\n"

                actualizado = True

                break


        if actualizado:

            with open(
                self.nombreArchivo,
                "w",
                encoding="utf-8"
            ) as archivo:

                archivo.writelines(lineas)

        return actualizado

if __name__ == '__main__':
    archivo = ArchivoOperadores()

    operador = Operador(
        "OP-1001",
        "Juan Perez",
        "juan@gmail.com",
        "12345"
    )

    archivo.guardar(operador)