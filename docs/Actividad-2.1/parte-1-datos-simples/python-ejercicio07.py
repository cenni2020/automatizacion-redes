# Parte 1 : Tipos de Datos Simples
# Ejercicio 7 
# Planteamiento del problema: 
# Pedir al usuario su peso en kg y estatura en metros, 
# calcular el Índice de Masa Corporal (text{IMC} = frac{text{peso}}{text{estatura}^2}) 
# y mostrar la frase "Tu índice de masa corporal es <imc>", redondeado con dos decimales.

peso = float(input("Introduce tu peso en kg: "))
estatura = float(input("Introduce tu estatura en metros: "))
imc = peso / (estatura ** 2)
print(f"Tu índice de masa corporal es {round(imc, 2)}")

# Explicación: 
# Se eleva la estatura al cuadrado usando ** 2 y se efectúa la división con /. 
# La función nativa round(imc, 2) redondea el resultado flotante al número deseado de decimales.
