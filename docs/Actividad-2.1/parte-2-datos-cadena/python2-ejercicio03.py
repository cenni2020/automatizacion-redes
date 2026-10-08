# #parte 2 : datos de cadena
# Ejercicio 3
# problema: 
# Preguntar el nombre del usuario y mostrar por pantalla
# "<NOMBRE> tiene <N> letras", donde <NOMBRE> se muestra en mayúsculas y <N> es el conteo de letras que contiene.

nombre = input("Introduce tu nombre: ")
numero_letras = len(nombre.replace(" ", ""))

print(f"{nombre.upper()} tiene {numero_letras} letras")

# Explicación: 
# Se aplica .upper() sobre la cadena de entrada 
# y la función len() para obtener la longitud total del texto,
# filtrando espacios en blanco mediante .replace(" ", "").