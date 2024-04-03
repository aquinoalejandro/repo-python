#Ejercicio 4: Palindrome_Reorder
def palindrome_reorder(texto):
    # Contamos la frecuencia de cada carácter
    frecuencias = {}
    for caracter in texto:
        if caracter in frecuencias:
            frecuencias[caracter] += 1
        else:
            frecuencias[caracter] = 1

    # Construimos la mitad izquierda del palíndromo
    medio_palindromo = []
    caracter_diferente = ""
    for caracter in frecuencias:
        while frecuencias[caracter] >= 2:
            medio_palindromo.append(caracter)
            frecuencias[caracter] -= 2
        if frecuencias[caracter] == 1:
            if caracter_diferente:
                return "NO SOLUTION"
            caracter_diferente = caracter

    # Construimos el palíndromo completo
    palindromo_completo = medio_palindromo + [caracter_diferente] + medio_palindromo[::-1]

    return "".join(palindromo_completo)

# Pruebas
assert palindrome_reorder("aabbc") == "abcba", "Error en el caso de prueba"