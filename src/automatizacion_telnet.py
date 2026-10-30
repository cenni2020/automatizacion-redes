import getpass
import telnetlib

# Dirección IP configurada en la interfaz Gi0/0 de tu router R1 en GNS3
HOST = "192.168.42.70"

# Solicita las credenciales de Telnet de forma segura
user = input("Enter your Telnet username: ")
password = getpass.getpass()

# Establece la conexión Telnet con el router
tn = telnetlib.Telnet(HOST)

# Interacción con el login del router
tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

# Comandos de configuración automatizada en el router
tn.write(b"enable\n")
tn.write(b"cisco\n")  # Contraseña del modo enable configurada en R1
tn.write(b"configure terminal\n")

# Creación de interfaces Loopback
tn.write(b"interface loopback 0\n")
tn.write(b"ip address 1.1.1.1 255.255.255.255\n")
tn.write(b"interface loopback 1\n")
tn.write(b"ip address 2.2.2.2 255.255.255.255\n")

# Configuración del protocolo OSPF
tn.write(b"router ospf 1\n")
tn.write(b"network 0.0.0.0 255.255.255.255 area 0\n")

# Finalizar y salir
tn.write(b"end\n")
tn.write(b"exit\n")

# Imprimir la salida completa de la ejecución en la terminal de VS Code
print(tn.read_all().decode('ascii'))