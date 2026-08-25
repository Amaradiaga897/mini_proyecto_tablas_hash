

class Operador:

    def __init__(
        self,
        idd=None,
        nombre=None,
        correo=None,
        password=None,
        ultimoAcceso=None
    ):
        self.id = idd
        self.nombre = nombre
        self.correo = correo
        self.password = password
        self.ultimoAcceso = ultimoAcceso

    def convertir(self, cadena: str):

        # La cadena debe tener 5 elementos
        informacion = cadena.split('|')

        if len(informacion) != 5:
            print('La cantidad de atributos es incorrecta.')
            return

        self.id, self.nombre, self.correo, self.password, self.ultimoAcceso = informacion

    def convertir_str(self):

        return f'{self.id}|{self.nombre}|{self.correo}|{self.password}|{self.ultimoAcceso}'

if __name__ == '__main__':

    operador = Operador()
    operador.convertir('123|haniel|haniel06hernandez@gmail.com|hola0600|hashas')

    print(operador.nombre)

