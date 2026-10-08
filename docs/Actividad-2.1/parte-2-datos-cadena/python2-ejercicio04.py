#parte 2 : datos de cadena
#Ejercicio 4
#Planteamiento del problema: 
#Los teléfonos de una empresa tienen el formato prefijo-número-extensión (ejemplo +52-913724710-56).
#Escribir un programa que pida un número con este formato y muestre únicamente el número sin el prefijo ni la extensión.

telefono = input("Introduce un número de teléfono (formato +52-número-extensión): ")
partes = telefono.split("-")
numero_principal = partes[1]

print(f"El número de teléfono sin prefijo ni extensión es: {numero_principal}")

#Explicación: 
# El método .split("-") fragmenta la cadena tomando el guión como delimitador y genera una lista. 
# Posteriormente se extrae el elemento del índice 1 que almacena el número de teléfono deseado.
