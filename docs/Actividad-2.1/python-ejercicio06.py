# Parte 1 : Tipos de Datos Simples
#Ejercicio 6
#Planteamiento del problema: 
#Leer un entero positivo $n$ e imprimir la suma de todos los enteros desde 1 
#hasta n utilizando la fórmula text{suma} = frac{n(n + 1)}{2}.

n = int(input("Introduce un número entero positivo (n): "))
suma = (n * (n + 1)) // 2
print(f"La suma de los enteros desde 1 hasta {n} es: {suma}")

# Explicación: 
# int() castea el texto a número entero. 
# Se aplica la fórmula matemática utilizando la división entera 
# para garantizar que la variable de resultado conserve un tipo de dato entero.