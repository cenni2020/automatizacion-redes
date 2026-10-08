#parte 2 : datos de cadena
#Ejercicio 6
# #Planteamiento del problema: 
# Pedir una frase y una vocal, 
# y mostrar por pantalla la misma frase pero con la vocal introducida convertida en mayúscula

frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal: ")

frase_modificada = frase.replace(vocal.lower(), vocal.upper()).replace(vocal.upper(), vocal.upper())
print(f"Resultado: {frase_modificada}")

#Explicación: 
# Aplica el método .replace() 
# sustituyendo las apariciones de la vocal por su equivalente en mayúscula obtenido mediante .upper().