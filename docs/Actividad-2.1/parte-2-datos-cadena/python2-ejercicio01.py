#parte 2 : Ejercicios de cadenas
# Ejercicio 1
# Planteamiento del problema:
# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla
# el nombre del usuario tantas veces como el número introducido.

nombre = input("Introduce tu nombre: ")
n = int(input("Introduce un número entero: "))

print((nombre + "\n") * n)

# Explicación: 
# Hace uso de la concatenación del carácter especial de salto de línea \n al texto del nombre 
# y el operador de multiplicación de cadenas * para duplicar la secuencia n veces sin usar bucles explícitos.
