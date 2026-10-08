#parte 1: Tipos de Datos Simples
#Ejercicio 5
#Planteamiento del problema: 
# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el costo por hora,
# y muestre en pantalla la paga correspondiente.

horas = float(input("Introduce el número de horas trabajadas: "))
costo = float(input("Introduce el costo por hora: "))
paga = horas * costo
print(f"La paga que te corresponde es: ${paga:.2f}")

# Explicación: La función float() convierte la entrada ingresada en input() de texto a un número decimal. 
# Se calcula el producto de ambas variables con * y se formatea la salida con el especificador :.2f.