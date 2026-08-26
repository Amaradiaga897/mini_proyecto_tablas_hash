

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

        # La cadena debe tener al menos 4 elementos
        informacion = cadena.split('|')

        if len(informacion) < 4:
            print('La cantidad de atributos es incorrecta.')
            return

        self.id = informacion[0] if len(informacion) > 0 else None
        self.nombre = informacion[1] if len(informacion) > 1 else None
        self.correo = informacion[2] if len(informacion) > 2 else None
        self.password = informacion[3] if len(informacion) > 3 else None
        self.ultimoAcceso = informacion[4] if len(informacion) > 4 and informacion[4] != '' and informacion[4] != 'None' else None

    def __str__(self):
        ultimo = self.ultimoAcceso if self.ultimoAcceso is not None else ""
        return f'{self.id}|{self.nombre}|{self.correo}|{self.password}|{ultimo}'



if __name__ == '__main__':

    operador = Operador()
    operador.convertir('123|haniel|haniel06hernandez@gmail.com|hola0600|hashas')

    print(operador.nombre)

