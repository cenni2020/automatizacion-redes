# parte 2 : datos de cadena
#Ejercicio 11
# Planteamiento del problema: 
# Preguntar el nombre de un producto, su precio unitario y el número de unidades. 
# Mostrar por pantalla una cadena formateada con el nombre del producto, 
# el precio unitario (6 dígitos enteros y 2 decimales), las unidades (3 dígitos) 
# y el costo total (8 dígitos enteros y 2 decimales).

producto = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio unitario: "))
unidades = int(input("Introduce el número de unidades: "))

costo_total = precio * unidades

print(f"{producto}: {precio:09.2f}$ x {unidades:03d} unidades = {costo_total:011.2f}$")

#Explicación: 
# # Emplea especificadores avanzados de formato en f-strings:
# :09.2f define un ancho total de 9 caracteres (6 enteros, 1 punto, 2 decimales) rellenando con ceros a la izquierda.
# :03d formatea un entero ocupando 3 posiciones numéricas.
# :011.2f asigna un ancho de 11 caracteres (8 enteros, 1 punto, 2 decimales) con relleno de ceros.