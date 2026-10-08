# parte 1 : Tipos de Datos Simples
# Ejercicio 10
# Planteamiento del problema: 
# Calcular el peso total de un paquete que contendrá payasos (112 g cada uno) 
# y muñecas (75 g cada una) a partir de las cantidades vendidas ingresadas por el usuario.

cantidad_payasos = int(input("Introduce la cantidad de payasos vendidos: "))
cantidad_munecas = int(input("Introduce la cantidad de muñecas vendidas: "))
peso_total = (cantidad_payasos * 112) + (cantidad_munecas * 75)
print(f"El peso total del paquete es: {peso_total} g")

# Explicación:
# Se emplea la función int() para convertir la entrada del usuario en números enteros.
# Se calcula el peso total multiplicando la cantidad de payasos por su peso individual y sumando el resultado a la multiplicación de la cantidad de muñecas por su peso individual. Finalmente, se muestra el resultado en pantalla.
