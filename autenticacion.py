
from datetime import datetime
 
from operador import Operador
 
 
def _mostrarOperador(operador):
    print("\n================================")
    print("        INFORMACIÓN DE ACCESO")
    print("================================")
    print(f"ID:             {operador.id}")
    print(f"Nombre:         {operador.nombre}")
    print(f"Correo:         {operador.correo}")
    print(f"Último acceso:  {operador.ultimoAcceso}")
    print("================================\n")
 
 
def _registrarNuevoOperador(tabla, archivo, idOperador):
    print(f"\nNo se encontró información para el ID '{idOperador}'.")
    respuesta = input("¿Desea registrar este operador nuevo? (s/n): ").strip().lower()
 
    if respuesta != 's':
        print("Registro cancelado.")
        return None
 
    nombre = input("Nombre completo: ").strip()
    correo = input("Correo: ").strip()
    password = input("Contraseña: ").strip()
 
    nuevoOperador = Operador(
        idd=idOperador,
        nombre=nombre,
        correo=correo,
        password=password,
        ultimoAcceso=None
    )
 
    insertado = tabla.insertar(nuevoOperador)
 
    if not insertado:
        # TablaHash.insertar ya imprimió el mensaje de conflicto de hash.
        print("No fue posible almacenar al nuevo operador (llave sinónima).")
        return None
 
    archivo.guardar(nuevoOperador)
    print(f"Operador '{idOperador}' registrado correctamente.")
    print("Vuelva a iniciar sesión con sus credenciales para continuar.\n")
    return None
 
 
def iniciarSesion(tabla, archivo, maxIntentos=3):
    """
    Ejecuta el flujo completo de login.
    Devuelve el objeto Operador autenticado, o None si no se pudo
    autenticar (credenciales inválidas, cancelado, etc.)
    """
 
    idOperador = input("\nIngrese su ID de operador: ").strip()
 
    operador = tabla.buscar(idOperador)
 
    if operador is None:
        _registrarNuevoOperador(tabla, archivo, idOperador)
        return None
 
    intentos = 0
    while intentos < maxIntentos:
        password = input("Ingrese su contraseña: ").strip()
 
        if password == operador.password:
            operador.ultimoAcceso = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            archivo.actualizar(operador)
 
            print("\nLOGIN EXITOSO")
            _mostrarOperador(operador)
            return operador
 
        intentos += 1
        restantes = maxIntentos - intentos
        if restantes > 0:
            print(f"Credenciales inválidas. Intentos restantes: {restantes}")
        else:
            print("Credenciales inválidas. Acceso denegado.")
 
    return None
 