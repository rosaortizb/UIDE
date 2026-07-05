import random
import string


# ============================================================
# FUNCIONALIDAD 1: Ingreso y validación de longitud
# ============================================================
def validar_longitud():
    """
    Le pide al usuario la longitud de la contraseña y repite la
    pregunta hasta que el dato sea válido (igual que el rombo
    de validaciones en el diagrama, con sus 3 "No" que regresan
    a 'Solicitar longitud').
    """
    while True:
        entrada = input("Ingresa la longitud de la contraseña (o 'salir' para terminar): ")

        # ¿El usuario quiere salir?
        if entrada.lower() == "salir":
            return None

        # ¿Es número?
        if not entrada.isdigit():
            print("Error: Debe ingresar un número")
            continue

        longitud = int(entrada)

        # ¿Longitud > 0?
        if longitud <= 0:
            print("Error: Debe ser mayor a 0")
            continue

        # ¿Longitud <= 20?
        if longitud > 20:
            print("Error: Máximo permitido es 20")
            continue

        # Si pasó las 3 validaciones -> "Longitud válida"
        return longitud


# ============================================================
# FUNCIONALIDAD 2: Generación de contraseña
# ============================================================
def generar_contrasena(longitud):
    """
    Recibe la longitud válida y va agregando caracteres
    aleatorios uno por uno hasta completar la longitud
    (el rombo "¿Se completó la longitud?" del diagrama).
    """
    # Definir conjunto de caracteres: mayúsculas, minúsculas, números, símbolos
    caracteres = string.ascii_uppercase + string.ascii_lowercase + string.digits + "!@#$%^&*"

    contrasena = ""  # Inicializar contraseña vacía

    while len(contrasena) < longitud:  # ¿Se completó la longitud? -> No
        caracter = random.choice(caracteres)
        contrasena += caracter

    return contrasena  # Sí -> Contraseña generada


# ============================================================
# FUNCIONALIDAD 3: Mostrar resultado
# ============================================================
def mostrar_resultado(contrasena):
    """Recibe la contraseña generada y la muestra en pantalla."""
    print("Tu contraseña generada es:", contrasena)


# ============================================================
# DIAGRAMA GENERAL: une las 3 funcionalidades en orden
# ============================================================
def main():
    print("Bienvenido al generador de contraseñas")  # Mensaje de bienvenida

    while True:
        longitud = validar_longitud()           # Funcionalidad 1

        # Si el usuario escribió "salir", longitud será None
        if longitud is None:
            break

        contrasena = generar_contrasena(longitud)  # Funcionalidad 2
        mostrar_resultado(contrasena)            # Funcionalidad 3
        print()  # Línea en blanco para separar cada contraseña generada

    print("Fin del programa")


if __name__ == "__main__":
    main()
