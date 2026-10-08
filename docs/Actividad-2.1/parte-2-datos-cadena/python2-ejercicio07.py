#practica 2 : datos de cadena
#Ejercicio 7
#Planteamiento del problema: 
# Preguntar el correo electrónico del usuario 
# y mostrar por pantalla otro correo con el mismo nombre de usuario 
# (antes del @) pero con el dominio utmatamoros.edu.mx.

correo = input("Introduce tu correo electrónico: ")
nombre_usuario = correo.split("@")[0]
nuevo_correo = nombre_usuario + "@utmatamoros.edu.mx"

print(f"Tu nuevo correo institucional es: {nuevo_correo}")

# Explicación: 
# Se divide la cadena a partir del carácter @ con .split("@"), 
# extrayendo la posición 0 (nombre de usuario) 
# y concatenándola con la nueva extensión del dominio institucional.