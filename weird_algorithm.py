#Ejercicio 1 "Weird Algorithm"
n = int(input("Ingrese un numero entero mayor a 0: "))
arreglo = []

def weird_algorithm(n):
    arreglo.append(n)

    if n > 0:
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            arreglo.append(n)
    else:
        print("El numero debe ser mayor a 0")
    return arreglo

assert weird_algorithm(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"
print("El algoritmo funcionó correctamente")