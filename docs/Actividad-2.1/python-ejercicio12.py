#parte 1 : Tipos de Datos Simples
# Ejercicio 12
# Planteamiento del problema:
# Planteamiento del problema: 
# Una panadería vende barras de pan a $3.49 cada una. 
# El pan no fresco tiene un 60% de descuento. 
# Leer la cantidad de barras no frescas vendidas y mostrar el precio habitual, el descuento aplicado y el coste final total.

cantidad_barras = int(input("Introduce la cantidad de barras de pan no frescas vendidas: "))
precio_habitual = cantidad_barras * 3.49
descuento = precio_habitual * 0.60
coste_final = precio_habitual - descuento

print(f"Precio habitual: ${precio_habitual:.2f}")
print(f"Descuento aplicado: ${descuento:.2f}")
print(f"Coste final total: ${coste_final:.2f}")

# Explicación:
# Se calcula el precio habitual multiplicando la cantidad de barras por el precio unitario.
# Luego, se calcula el descuento aplicando el 60% al precio habitual y finalmente se
# calcula el coste final restando el descuento al precio habitual. Los resultados se muestran en pantalla con dos decimales utilizando el especificador :.2f.

