

def convertirCadenaANumero(idd : str):

    valor = 0

    for caracter in idd:
        valor = valor * 31 + ord(caracter)

    return valor

def calcularHash(idd: str, M : int = 13):

    valorNumerico = convertirCadenaANumero(idd)

    if(M <= 0):
        print('M debe ser mayor a 0.')
        return None

    valorNumerico = valorNumerico % M

    return valorNumerico

if __name__ == '__main__':

    ids = [
        'OP-1001',
        'OP-1002',
        'OP-1003',
        'EMP-2024',
        'EMP-2025'
    ]

    for idd in ids:
        print(idd, '->', calcularHash(idd))