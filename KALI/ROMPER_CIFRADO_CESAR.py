import string
from langdetect import detect

ALFABETO = string.ascii_lowercase + string.digits

def algoritmo_descifrado(texto_cifrado, clave, direccion):
    """direccion = 1  -> desplazamiento positivo  direccion = -1 -> desplazamiento negativo
    """
    texto_plano = ""
    desplazamiento = clave * direccion

    for caracter in texto_cifrado:
        if caracter not in ALFABETO:
            texto_plano += caracter
        else:
            indice = ALFABETO.index(caracter)
            nuevo_indice = (indice - desplazamiento) % len(ALFABETO)
            texto_plano += ALFABETO[nuevo_indice]

    return texto_plano


def fuerza_bruta(texto_cifrado):
    espacio_claves = range(len(ALFABETO))

    for direccion in [1, -1]:
        for clave in espacio_claves:
            texto_plano = algoritmo_descifrado(texto_cifrado, clave, direccion)

            lenguaje = detect(texto_plano)

            if lenguaje == "es":
                sentido = "derecha" if direccion == 1 else "izquierda"

                print("\nTexto descifrado:", texto_plano)
                print("Clave encontrada:", clave)
                print("Dirección utilizada:", sentido)
                return

    print("No se encontró una combinación válida.")


if __name__ == "__main__":
    texto_cifrado = input("Introduce el texto cifrado: ").lower()
    fuerza_bruta(texto_cifrado)