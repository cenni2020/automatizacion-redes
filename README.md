# Mi estación de automatización de redes

## 1. Datos del equipo
    - Integrantes: 
        Samuel Ceniceros Dorantes
        Christian Noe Esparza Meza
        Cesar Alexander Fuentes Garcia
    - Grupo: 
        3IRI1V
    - Asignatura: 
        Automatización de Infraestructura Digital I
    - Fecha:
        Jueves 24 de septiembre 2026 

## 2. Propósito de la práctica

Documentar la preparación y configuración de una estación de trabajo para automatizar tareas de administración y operación de redes.

## 3. Herramientas instaladas

    - Sistema operativo: 
        windows 10 pro
    - Python: 
        python 3
    - Git: 
        cuenta de GitHub 
        cenni2020 , 
        71Alex1
    - Editor o IDE: 
        Visual Studio Code 
    - Librerías y herramientas adicionales: 
        Python 3 y modulo 'venv' para entornos virtuales
        Visual Studio Code (con extensiones de Python)
        postman (cuenta y interfaz)
        Broadcom (cuenta)
        OpenConnect GUI
        Docker Desktop (con soporte WSL 2)
        Vmware Workstation Pro
        GNS3 GUI y GNS3 VM

## 4. Configuración realizada

1. Instalación de las herramientas necesarias.
2. Configuración de las variables de entorno.
3. Creación y activación del entorno virtual.
4. Instalación de las dependencias del proyecto.
5. Configuración del acceso a los dispositivos de red.

## 5. Verificación del entorno

- [ si ] El sistema operativo está actualizado.
- [ si ] Python y Git responden correctamente.
- [ si ] El entorno virtual está configurado.
- [ si ] Las dependencias se instalaron sin errores.
- [ si ] Se validó la conectividad con los dispositivos de red.

## 6. Estructura del repositorio

    ```text
    automatizacion-redes/
    ├── README.md
    ├── requirements.txt
    ├── scripts/
    ├── configuraciones/
    └── docs/
    ```

## 7. Conclusiones

    La estación de trabajo quedó preparada para desarrollar, ejecutar y verificar automatizaciones de red de forma organizada y reproducible.

    Samuel: La configuración del entorno de desarrollo local con Python 3, el módulo venv y Visual Studio Code, combinada con la integración de Git y GitHub, me permitió comprender la importancia de trabajar con entornos aislados y control de versiones estructurado. Esto garantiza que los scripts de automatización se desarrollen de manera limpia, reproducible y colaborativa desde la raíz del repositorio.

    Christian: La importación e integración exitosa de la GNS3 VM sobre VMware Workstation Pro y su vinculación con GNS3 GUI y Docker Desktop demostraron la relevancia de la virtualización y la contenerización en la automatización de redes. Lograr que el servidor virtualizado responda correctamente permite simular topologías y escenarios complejos sin poner en riesgo la infraestructura real.

    Cesar: La incorporación de clientes de API y redes como Postman y OpenConnect GUI, sumada a las pruebas de verificación del sistema y conectividad, dejó la estación de trabajo totalmente preparada para consumir servicios web, probar APIs REST y gestionar dispositivos de forma remota y segura.

## Evidencias
![Python](docs/Practica-01/Evidencias/01-python-version.png)
![VS Code](docs/Practica-01/Evidencias/02-Visual-Studio-Code.png)
![VS Code y Python](docs/Practica-01/Evidencias/03-python-vscode.png)
![Entorno Virtual](docs/Practica-01/Evidencias/04-entorno-virtual.png)
![Hola Mundo](docs/Practica-01/Evidencias/04-entorno-virtual.png)
![Git Versión](docs/Practica-01/Evidencias/06-Git-version.png)
![Git Identidad](docs/Practica-01/Evidencias/07-git-identidad.png)
![GitHub Repo](docs/Practica-01/Evidencias/08-repositorio.png)
![Postman](docs/Practica-01/Evidencias/09-postman.png)
![OpenConnect](docs/Practica-01/Evidencias/10-OpennConect.png)
![Docker](docs/Practica-01/Evidencias/11-Docker.png)
![GNS3 GUI](docs/Practica-01/Evidencias/12-GNS3.png)
![GNS3 VM](docs/Practica-01/Evidencias/13-VMware.png)
![VMware Workstation](docs/Practica-01/Evidencias/14-Vmware-ova.png)
![Importación GNS3 VM](docs/Practica-01/Evidencias/15-VMW-GNS3.png)
![Integración GNS3](docs/Practica-01/Evidencias/16-VMW-GNS3-ambos-funcionando.png)

## Avance del proyecto integrador

### Práctica 1
Preparación de la estación de automatización de redes.
Estado: Completada.
![Topologia01](docs/practica-02/topologia-01/topologia-01.png)
![Evidencia](docs/practica-02/topologia-01/evidencias/topologia-01-pings-entre-pcs.png)

### Práctica 2
Construcción de la red simulada en GNS3.
Estado: Completada.
![Topologia02](docs/practica-02/topologia-02/topologia-02.png)
![Evidencia](docs/practica-02/topologia-02/evidencias/t2-ospf-neighbor.png)

Infraestructura construida:
- Topología básica PC-Switch-PC.
- Topología con dos routers y un switch multicapa.
- Direccionamiento IP.
- Conectividad entre dispositivos.
- Protocolo OSPF.
- Verificación de tablas de enrutamiento.

## Pruebas finales

Realizar las pruebas necesarias para comprobar el funcionamiento de la topología. Registrar:

| Prueba                    | Resultado                              | Evidencia                 |
| :------------------------ | :------------------------------------- | :------------------------ |
| **R1 → R2**               | 80% de éxito (4/5); 20% de pérdida     | Ping de R1 a `10.1.1.2`   |
| **R2 → R1**               | 100% de éxito (5/5); 0% de pérdida     | Ping de R2 a `10.1.1.1`   |
| **Estado de interfaces**  | Gi0/0 y Loopback0 de R1 aparecen up/up | `show ip interface brief` |
| **Vecino OSPF**           | Vecino `2.2.2.2` en estado FULL/BDR    | `show ip ospf neighbor`   |
| **Tabla de enrutamiento** | Ruta OSPF `2.2.2.2/32` vía `10.1.1.2`  | `show ip route`           |

### Bitácora de Problemas y Soluciones

Durante la práctica, se registraron los siguientes inconvenientes y sus respectivas soluciones:

| Problema encontrado                                | Posible causa                                                         | Solución aplicada                                      | Resultado                                            |
| :------------------------------------------------- | :-------------------------------------------------------------------- | :----------------------------------------------------- | :--------------------------------------------------- |
| **IP duplicada al configurar PC2**                 | Se intentó usar `10.1.1.1`, ya asignada a PC1                         | Se cambió PC2 a `10.1.1.2/24`                          | PC2 quedó configurada correctamente                  |
| **Comando IP inválido en R1**                      | Se escribió `ip address` fuera del modo de interfaz                   | Se ingresó a `interface gi0/0` y se repitió el comando | Gi0/0 quedó con `10.1.1.1/24` y en estado up/up      |
| **Primer ping de R2 a R1 falló**                   | La conectividad todavía no estaba completamente establecida           | Se revisó la configuración y se repitió la prueba      | El segundo ping obtuvo 100% de éxito (5/5)           |
| **Primer ping de R1 a R2 perdió un paquete**       | La comunicación y resolución ARP acababan de establecerse             | Se verificaron interfaces y conectividad               | Resultado final de la prueba: 80% (4/5)              |
| **OSPF requería comprobar la adyacencia**          | Era necesario verificar que ambos routers fueran vecinos              | Se ejecutó el comando `show ip ospf neighbor`          | Vecino `2.2.2.2` quedó confirmado en estado FULL/BDR |
| **Conservar las configuraciones tras el reinicio** | Los cambios no quedan guardados solo con configurarlos en memoria RAM | Se ejecutó el comando `write` en routers y switch      | Configuraciones guardadas correctamente en NVRAM     |



## Conclusiones
conclusiones del equipo:

Christian Noe Esparza Meza: Durante esta actividad aprendí a crear y configurar diferentes topologías de red utilizando GNS3. 
También pude asignar direcciones IP a los dispositivos y comprobar su correcta configuración. 
Las pruebas de ping permitieron verificar que existiera comunicación entre los equipos de la red. 
Además, la configuración de OSPF permitió establecer comunicación y compartir rutas entre los routers. Esta práctica me ayudó a comprender mejor cómo se configura y verifica una red simulada. 
 
Samuel Ceniceros Dorantes : La práctica permitió aplicar de manera práctica conocimientos sobre direccionamiento IP y enrutamiento. 
Durante el procedimiento se presentaron algunos errores de configuración que tuvieron que ser corregidos. 
Esto ayudó a comprender la importancia de revisar las interfaces, comandos y direcciones configuradas. 
También se utilizaron comandos para verificar vecinos OSPF, interfaces y tablas de enrutamiento. Con estas pruebas fue posible comprobar que la topología funcionaba correctamente. 
 
Cesar Alexander Fuentes García:
Esta actividad también permitió preparar una infraestructura que podrá utilizarse para automatización de redes. 
Las configuraciones y evidencias realizadas fueron organizadas para llevar un registro del procedimiento. 
Además, se documentó el trabajo realizado y se almacenaron las evidencias correspondientes del proyecto. 
La red creada servirá posteriormente para probar scripts sin afectar dispositivos o redes reales

## Conclusiones Elaboradas
Las conclusiones elaboradas deben sintetizar los logros técnicos alcanzados, los desafíos resueltos y el impacto metodológico de la práctica:

Estandarización y Entornos Aislados: 
La preparación del entorno local con Python 3 y el módulo venv, en conjunto con Visual Studio Code, demostró la necesidad crítica de mantener entornos de desarrollo limpios y aislados. Esto evita conflictos de dependencias y garantiza que los programas de automatización sean completamente reproducibles entre diferentes miembros del equipo y servidores.

Simulación de Alta Fidelidad mediante Virtualización:
La correcta integración de GNS3 GUI con la máquina virtual GNS3 VM en VMware Workstation Pro demuestra que es posible desplegar e interconectar infraestructuras de red complejas ejecutando sistemas operativos reales (como Cisco IOS) sin requerir hardware físico dedicado.

Trazabilidad y Trabajo Colaborativo: 
El flujo de trabajo establecido mediante Git y GitHub asegura un historial estructurado de cambios, permitiendo guardar la evolución de las configuraciones y los scripts en el repositorio automatizacion-redes.

## Reflexión sobre la Relación de la Práctica con el Proyecto Integrador
El Proyecto Integrador requiere un entorno real o simulado donde se ejecuten y validen las automatizaciones. Esta práctica se vincula directamente de las siguientes maneras:

Laboratorio de Pruebas Seguro (Sandbox): La red virtual construida en GNS3 actúa como el escenario de pruebas del proyecto. Desarrollar y ejecutar scripts de Python directamente sobre equipos de producción reales implicaría el riesgo de provocar caídas de servicio (outages) o bloqueos de acceso remoto. El entorno virtualizado permite fallar, corregir y validar la lógica del código de manera segura.

Puente de Conexión entre Código e Infraestructura: Mediante el uso de nodos Cloud o NAT en GNS3, la computadora host (donde se ejecutan VS Code y los scripts de Python) puede comunicarse por IP directamente con los routers y switches simulados. Esto permite probar librerías de automatización (como Netmiko, Paramiko o NAPALM) mediante conexiones SSH/Telnet o APIs.

Escenario para Tareas Automatizables del Proyecto: La topología montada servirá como destino para ejecutar scripts que realicen:

Asignación masiva de direcciones IP, hostnames y VLANs.

Despliegue de protocolos de enrutamiento (como OSPF).

Extracción automática de información del estado de la red (show ip interface brief, tablas de vecinos OSPF).

Generación periódica y automática de respaldos (backups) de los archivos running-config.

## Tres Posturas (Perspectivas de los Integrantes) para la Práctica
Para reflejar el trabajo en equipo y el aporte individual dentro de la práctica, se presentan las tres posturas del equipo de trabajo:

Postura 1 (Samuel Ceniceros Dorantes – Enfoque en Entornos de Desarrollo y Control de Versiones):

    "Mi postura sobre la práctica se centra en la importancia de la estructura y el control del proyecto. Configurar correctamente el entorno virtual de Python (venv) y sincronizar la estructura de carpetas mediante Git y GitHub garantiza que cualquier script de automatización desarrollado sea modular, seguro y fácil de mantener a lo largo de todas las fases del proyecto integrador".

Postura 2 (Christian Noe Esparza Meza – Enfoque en Virtualización e Infraestructura Simulada):

    "Desde el punto de vista de la infraestructura, la integración de GNS3 VM sobre el hipervisor VMware Workstation Pro constituye el pilar operativo del laboratorio. Garantizar que la máquina virtual gestione eficientemente los recursos de CPU y RAM permite emular topologías complejas con rendimiento óptimo, lo que resulta indispensable para simular escenarios reales de red sin depender de equipo físico".

Postura 3 (Cesar Alexander Fuentes Garcia – Enfoque en Conectividad, Pruebas y Consumo de Servicios):

    "Mi perspectiva se orienta hacia la verificación funcional y la interoperabilidad de la red. La incorporación de herramientas como Postman y OpenConnect, sumada a la validación de la conectividad básica (ping, adyacencias OSPF e interfaces), confirma que la topología no solo está activa visualmente, sino que está lista para responder a solicitudes de lectura y modificación enviadas por nuestros futuros scripts automatizados".

Próximo paso:
Desarrollo de scripts y herramientas para automatizar tareas sobre la infraestructura de red.

