#parte 2 : datos de cadena
# Ejercicio 5
# problema: 
# Pedir al usuario que introduzca una frase en la consola y mostrar por pantalla la frase invertida.

frase = input("Introduce una frase: ")
frase_invertida = frase[::-1]

print(f"Frase invertida: {frase_invertida}")

# Explicación: 
# Utiliza la notación de rebanado de cadenas (slicing) con la sintaxis [inicio:fin:paso]. 
# Al asignar un paso negativo de -1, 
# se invierte por completo el orden de la secuencia de caracteres.