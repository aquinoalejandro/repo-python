#Ejercicio 2 “Missing Number”
#Pido el limite de numeros que va a contener mi arreglo
n = int(input("Ingrese un numero entero mayor a 0: "))

#Compruebo si el numero es mayor a 0
if n <= 0:
    #Si el numero es menor o igual a cero salgo del programa
    print("El numero debe ser mayor a 0")
    exit()
else:
    #Si el numero es mayor a 0 continuo
    arreglo = list(map(int, input("Ingresa los números separados por espacios: ").split()))

#Defino una funcion para encontrar el numero perdido
def missing_number(n, arreglo):
    for i in range(1, n+1):
        if i not in arreglo:
            return i
            
#Pruebo si funciona, si no funciona devuelve error y no continua
assert missing_number(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"
print("El algoritmo funciono correctamente el numero perdido es:",  missing_number(n, arreglo))