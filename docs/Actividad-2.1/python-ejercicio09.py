# parte 1 : Tipos de Datos Simples
# Ejercicio 9
# Planteamiento del problema: 
# Preguntar al usuario una cantidad a invertir, el interés anual (%) y el número de años, 
# y mostrar por pantalla el capital obtenido en la inversión.

cantidad = float(input("Introduce la cantidad a invertir: "))
interes_anual = float(input("Introduce el interés anual (%): "))
años = int(input("Introduce el número de años: "))
capital_obtenido = cantidad * (1 + interes_anual / 100) ** años
print(f"El capital obtenido después de {años} años es: ${capital_obtenido:.2f}")    

# Explicación:
# Se utiliza la fórmula del interés compuesto para calcular el capital obtenido.    
