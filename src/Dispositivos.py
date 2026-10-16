# # aqui definimos las variables
# nombre = "R1" 
# tipo = "Router"
# ip = "10.1.1.1"
# loopback = "1.1.1.1"
# interfaz = "GigabitEthernet0/0"
# estado = "Acivo"
# nombre2 = "R2" 
# tipo2 = "Router"
# ip2 = "10.1.1.2"
# loopback2 = "10.1.1.2"
# interfaz2 = "GigabitEthernet0/0"
# estado2 = "Acivo"
# print("Nombre:", nombre)
# print("Tipo:", tipo)
# print("Direccion, IP:", ip)
# print("Loopback:", loopback)
# print("Interfaz:", interfaz)
# print("Estado:", estado)
# print("")
# print("Nombre:", nombre2)
# print("Tipo:", tipo2)
# print("Direccion, IP:", ip2)
# print("Loopback:", loopback2)
# print("Interfaz:", interfaz2)
# print("Estado:", estado2)

# parte 4 : uso de diccionario 

# router1 = {
#     "nombre": "R1",
#     "tipo": "Router",
#     "ip": "10.1.1.1",
#     "loopback": "1.1.1.1",
#     "interfaz": "GigabitEthernet0/0",
#     "estado": "Activo"
# }

# print("Dispositivo:" , router1["nombre"])
# print("Direccion IP:", router1["ip"])
# print("Estado:", router1["estado"])

# parte 7 : cracion de funciones
Dispositivo = [
    {
        "nombre": "R1",
        "tipo": "Router",
        "ip": "10.1.1.1",
        "loopback": "1.1.1.1",
        "interfaz": "GigabitEthernet0/0",
        "estado": "Activo",
        "fabricante": "Cisco",
        "protocolo": "OSPF"
    },
    {
        "nombre": "R2",
        "tipo": "Router",
        "ip": "10.1.1.2",
        "loopback": "1.1.1.1",
        "interfaz": "GigabitEthernet0/1",
        "estado": "Activo",
        "fabricante" : "Cisco",
        "protocolo": "OSPF"
    }, 
    {
        "nombre": "S1",
        "tipo": "Switch",
        "ip": "10.1.1.3",
        "estado": "fuera de servicio",
        "fabricante" : "Cisco",
        "protocolo": "OSPF"
    }
]

def mostrar_dispositivos(Dispositivos):
    print("Nombre:", Dispositivos["nombre"])
    print("Tipo:", Dispositivos["tipo"])
    print("Direccion IP:", Dispositivos["ip"])
    print("Estado:", Dispositivos["estado"])
    print("Fabricante:", Dispositivos["fabricante"])
    print("Protocolo:", Dispositivos["protocolo"])
    print("")

for dispositivo in Dispositivo:
    mostrar_dispositivos(dispositivo)

    if dispositivo["estado"] == "Activo":
        print("El dispositivo", dispositivo["nombre"], "está activo.")
    else:
        print("El dispositivo", dispositivo["nombre"], "está inactivo.")

#reto final

def buscar_dispositivo(lista_dispositivos):
    print("--- BÚSQUEDA DE DISPOSITIVOS ---")
    buscado = input("Ingrese el nombre del dispositivo a buscar: ")
    encontrado = False
    
    for disp in lista_dispositivos:
        if disp["nombre"].lower() == buscado.strip().lower():
            print("¡Dispositivo encontrado!")
            mostrar_dispositivos(disp)
            encontrado = True
            break
            
    if not encontrado:
        print(f"\n[Error]: El dispositivo '{buscado}' no se encuentra en el registro.")

# Ejecutar la función de búsqueda interactiva
buscar_dispositivo(Dispositivo)

