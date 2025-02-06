
# . Ordenación de caracteres en una palabra: Dada una palabra, ordénala alfabéticamente utilizando
# el método de inserción.

def insercion_palabra(palabra):
    palabra = list(palabra)
    for i in range(1, len(palabra)):
        clave = palabra[i]
        j = i - 1
        while j >= 0 and palabra[j] > clave:
            palabra[j + 1] = palabra[j]
            j -= 1
        palabra[j + 1] = clave
    return ''.join(palabra)


palabra = "PROGRAMADOR"
print("Palabra original:", palabra)
print("Palabra ordenada alfabéticamente:", insercion_palabra(palabra))

