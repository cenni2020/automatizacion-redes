# parte 1: Tipos de Datos Simples
# Ejercicio 8
# Planteamiento del problema: 
# Pedir al usuario dos números enteros n y m, 
# y mostrar por pantalla un mensaje indicando el cociente c y el resto r de la división entera de n entre m.

n = int(input("Introduce el dividendo (n): "))
m = int(input("Introduce el divisor (m): "))
c = n // m
r = n % m
print(f"{n} entre {m} da un cociente {c} y un resto {r}")

# Explicación:
# Emplea el operador // para calcular el cociente entero 
# y el operador módulo % para obtener el residuo de la división entre dos enteros.