import string
ALFABETO = string.ascii_lowercase

def algoritmo_descifrado(texto_cifrado, clave_descifrado):
    """Esta funcion descifra el texto cifrado 
    a partir de una clave de descifrado"""

    texto_plano = ""
    for letra in texto_cifrado:
        if letra not in ALFABETO:
            texto_plano += letra
        else:
            indice_letra_cifrada = ALFABETO.index(letra)
            indice_letra_descifrada =  indice_letra_cifrada - clave_descifrado
            texto_plano += ALFABETO[indice_letra_descifrada]
    return texto_plano

if __name__ == "__main__":
    texto_cifrado = input("Por favor introduce el texto cifrado: ").lower()
    clave_descifrado = int(input("Por favor introduzca clave de descifrado: "))
    texto_plano = algoritmo_descifrado(texto_cifrado, clave_descifrado)
    print(texto_plano)