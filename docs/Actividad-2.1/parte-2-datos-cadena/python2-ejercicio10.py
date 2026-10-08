# parte 2 : datos de cadena
#Ejercicio 10
# Planteamiento del problema: 
# Preguntar por consola por los productos de una cesta de la compra separados por comas, 
# y mostrar cada uno en una línea distinta.

cesta = input("Introduce los productos de la cesta de la compra separados por comas: ")
productos = cesta.split(",")

for producto in productos:
    print(producto.strip())

# Explicación: 
# Fragmenta la cadena introducida mediante .split(",") produciendo una lista de productos. 
# Un bucle for recorre los elementos 
# y los imprime eliminando espacios sobrantes en las orillas con .strip().