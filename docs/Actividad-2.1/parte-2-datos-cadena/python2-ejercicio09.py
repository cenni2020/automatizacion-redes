# #prate 2 : datos de cadena
# Ejercicio 9
# Planteamiento del problema: 
# Preguntar la fecha de nacimiento en formato dd/mm/aaaa y mostrar el día, mes y año por separado. 
# Adaptar el programa para que funcione aunque el día o el mes se introduzcan con un solo carácter.

fecha = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")
dia, mes, anio = fecha.split("/")

dia = dia.zfill(2)
mes = mes.zfill(2)

print(f"Día: {dia}")
print(f"Mes: {mes}")
print(f"Año: {anio}")

#Explicación: 
# Separa la cadena con .split("/") y aplica el método .zfill(2) 
# para rellenar con ceros a la izquierda en caso de que las entradas de día o mes contengan un único carácter.