

def convertirCadenaANumero(idd : str):
    valor = 0
    for caracter in idd:
        valor = valor * 31 + ord(caracter)
    return valor

def calcularHash(idd: str, M : int = 13):
    if M <= 0:
        print('M debe ser mayor a 0.')
        return None

    if isinstance(idd, str) and idd.isdigit():
        valorNumerico = int(idd)          
    else:
        valorNumerico = convertirCadenaANumero(str(idd))
    dispersion = convertirCadenaANumero(str(valorNumerico))
    return dispersion % M

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