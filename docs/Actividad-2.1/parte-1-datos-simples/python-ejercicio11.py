# parte 1 : Tipos de Datos Simples
# Ejercicio 11
# Planteamiento del problema: 
# Un depósito inicial en una cuenta de ahorros genera 4% de interés al año. 
# Calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer año, redondeando a dos decimales.

deposito = float(input("Introduce la cantidad de dinero depositada: "))
interes = 0.04

anio_1 = deposito * (1 + interes)
anio_2 = anio_1 * (1 + interes)
anio_3 = anio_2 * (1 + interes)

print(f"Ahorros tras el primer año: ${round(anio_1, 2):.2f}")
print(f"Ahorros tras el segundo año: ${round(anio_2, 2):.2f}")
print(f"Ahorros tras el tercer año: ${round(anio_3, 2):.2f}")

# Explicación:
# Se calcula el interés compuesto para cada año utilizando la fórmula: cantidad_final = cantidad_inicial
# * (1 + tasa_de_interés). Se redondea el resultado a dos decimales utilizando la función round() y se formatea la salida con el especificador :.2f.