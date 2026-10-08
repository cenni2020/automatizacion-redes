#parte 2 : datos de cadena
#Ejercicio 8
#Planteamiento del problema: 
# Preguntar el precio de un producto en euros con dos decimales 
# y mostrar por separado el número de euros y el número de céntimos.

precio = input("Introduce el precio del producto en euros (ej. 15.75): ")
euros, centimos = precio.split(".")

print(f"Número de euros: {euros}")
print(f"Número de céntimos: {centimos}")

# Explicación: 
# Se procesa la entrada como una cadena y se separa por el punto decimal mediante .split("."), 
# desempaquetando la lista de dos elementos directamente en las variables euros y centimos.
