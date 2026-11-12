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

## Próximo paso:
Desarrollo de scripts y herramientas para automatizar tareas sobre la infraestructura de red.

# Práctica 3: Primer programa de Python para representar información de dispositivos

## Datos Generales
  - **Asignatura:** Automatización de Infraestructura Digital I
  - **Grupo:** 3IRI1V
  - **Integrantes del Equipo:** 
    - Samuel Ceniceros Dorantes
    - Christian Noe Esparza Meza
    - Cesar Alexander Fuentes Garcia
  - **Fecha:** Octubre de 2026

---

## 1. Propósito
 Desarrollar un programa inicial en Python capaz de almacenar, organizar, modificar y mostrar información básica de los dispositivos de red simulados en la topología de GNS3 (Práctica 2). El propósito fundamental es comprender cómo estructurar datos de infraestructura mediante variables, diccionarios, listas, bucles, condiciones y funciones antes de implementar bibliotecas de automatización o conexiones directas mediante APIs y protocolos de red.

    ---

## 2. Conceptos Utilizados
  - **Variables:** Espacios de memoria para almacenar valores individuales de los equipos (nombre, dirección IP, estado).
  - **Tipos de datos:** Manejo de cadenas de texto (`str`), enteros y valores lógicos.
  - **Función `print()`:** Mecanismo básico para mostrar información formateada en la consola.
  - **Diccionarios:** Estructuras de datos clave-valor (`key-value`) que agrupan de forma estructurada todas las propiedades de un dispositivo específico.
  - **Listas:** Colecciones ordenadas que permiten almacenar múltiples diccionarios de dispositivos para representar una infraestructura completa.
  - **Ciclo `for`:** Estructura de control iterativa utilizada para recorrer la lista de equipos de manera automatizada.
  - **Condicional `if-else`:** Estructura de toma de decisiones para evaluar el estado operativo de los dispositivos (activo o fuera de servicio).
  - **Funciones (`def`):** Bloques de código reutilizables diseñados para modularizar tareas repetitivas, como la impresión de detalles de red.

  ---

## 3. Dispositivos Representados
A continuación se detalla la infraestructura simulada basada en la Práctica 2 y representada en el script `Dispositivos.py`:

| Dispositivo | Tipo | Dirección IP | Estado | Función / Detalles |
| :--- | :--- | :--- | :--- | :--- |
| **R1** | Router | 10.1.1.1 | Activo | Enrutamiento (Cisco / OSPF / Loopback: 1.1.1.1) |
| **R2** | Router | 10.1.1.2 | Activo | Enrutamiento (Cisco / OSPF / Loopback: 1.1.1.1) |
| **S1** | Switch | 10.1.1.3 | Fuera de servicio | Conectividad de Capa 2 / Acceso |
---

## 4. Preguntas de Análisis

  1. **¿Por qué es útil representar la información de los dispositivos mediante un programa?**  
     Permite centralizar y estructurar los datos de la red en un formato legible por software, facilitando su manipulación masiva, procesamiento lógico y futura automatización sin depender de consultas manuales constantes.
  2. **¿Qué ventaja ofrece utilizar un diccionario para representar un dispositivo?**  
     Permite asociar múltiples atributos heterogéneos (nombre, IP, fabricante, protocolo, estado) bajo un mismo contenedor mediante claves descriptivas, simulando un objeto de configuración estructurado.
  3. **¿Qué ventaja ofrece utilizar una lista para representar varios dispositivos?**  
     Facilita la agrupación de múltiples elementos de red en una sola variable ordenada, permitiendo recorrerlos y operarlos de forma masiva mediante bucles en lugar de procesar cada equipo de manera individual.
  4. **¿Qué tarea permite realizar el ciclo `for`?**  
     Automatiza el recorrido secuencial a través de la lista de dispositivos, aplicando las mismas operaciones (impresión, validaciones o llamadas a funciones) a cada equipo de la topología sin duplicar código.
  5. **¿Para qué se utilizó la estructura `if`?**  
     Para evaluar condiciones lógicas en tiempo de ejecución, específicamente verificar si el estado operacional de un dispositivo es "Activo" o requiere atención técnica.
  6. **¿Qué ventaja tiene utilizar una función?**  
     Promueve la modularidad, la reutilización de código y el mantenimiento limpio, evitando la repetición de bloques de instrucciones cada vez que se requiere mostrar u operar la información de un equipo.
  7. **¿Qué información de los dispositivos podría obtener automáticamente un programa en una etapa posterior?**  
     Tablas de enrutamiento, consumo de CPU y memoria, estado actual de las interfaces (UP/DOWN), versiones de firmware, contadores de tráfico y vecinos de protocolos como OSPF o CDP/LLDP.
  8. **¿Qué diferencia existe entre representar información de un dispositivo y obtener esa información directamente desde el dispositivo?**  
     Representarla implica declarar los datos manualmente de forma estática dentro del código, mientras que obtenerla directamente requiere interactuar en tiempo real con el equipo físico o simulado mediante protocolos de gestión (SSH, NETCONF, APIs).
  9. **¿Cómo podría evolucionar este programa para convertirse en una herramienta de automatización de redes?**  
     Integrando bibliotecas de conexión remota (como Paramiko o Netmiko) o APIs REST para extraer y modificar configuraciones directamente en los equipos de la red simulada en GNS3.
  10. **¿Qué relación existe entre esta práctica, la Práctica 2 y las siguientes prácticas del proyecto integrador?**  
      La Práctica 2 construyó el escenario físico/lógico (GNS3), esta práctica enseña a modelar lógicamente esa infraestructura en código Python, y las siguientes prácticas utilizarán este modelo para interactuar y automatizar dichos equipos.

  ---

## 5. Bitácora de Problemas y Soluciones

| Problema Encontrado | Posible Causa | Solución Aplicada | Resultado |
| :--- | :--- | :--- | :--- |
| `KeyError: 'fabricante'` al procesar el switch S1. | El diccionario del switch no contenía las llaves de fabricante y protocolo definidas en los routers. | Se agregaron los campos correspondientes a todos los elementos de la lista con valores adecuados (`"Cisco"`, `"N/A"`). | El script recorre la lista completa sin arrojar excepciones de claves faltantes. |
| Confusión en los nombres de las variables del ciclo (`for Dispositivo in Dispositivo:`). | Uso idéntico del nombre de la lista plural con la variable singular del iterador, generando conflictos de alcance. | Se renombró la variable temporal a un nombre diferenciado (ej. `for item in Dispositivo:` o `for disp in lista`). | El intérprete de Python procesó correctamente la iteración sin sobrescribir la estructura principal. |
 ---

## 6. Evidencias de la Práctica

- **Evidencia 1 (Estructura del repositorio):** Captura de la jerarquía de carpetas en VS Code. 
- ![Evidencia03](docs/practica-03/evidencia03/Captura%20de%20pantalla%202026-10-16%20110801.png)
- 
- **Evidencia 2 y 3 (Código y Ejecución inicial):** Creación de variables y salida en consola con `print()`.- ![Evidencia03](docs/practica-03/evidencia03/Captura%20de%20pantalla%202026-10-15%20182037.png)

- **Evidencia 4 (Dispositivos de Práctica 2):** Adaptación de datos con parámetros de GNS3 (R1, R2).
- ![Evidencia04](docs/practica-03/evidencia03/Captura%20de%20pantalla%202026-10-15%20183530.png)

- **Evidencia 5 y 6 (Listas, diccionarios y ciclos):** Implementación de estructuras de datos y bucle `for`.
- - ![Evidencia05y6](docs/practica-03/evidencia03/Captura%20de%20pantalla%202026-10-15%20192659.png)

- **Evidencia 7 (Función y condicionales):** Modularización con `def` y validaciones de estado `if`.
- - ![Evidencia07](docs/practica-03/evidencia03/Captura%20de%20pantalla%202026-10-15%20194027.png)

- **Evidencia 8 (Reto Final):** Funcionamiento de la función de búsqueda interactiva por teclado con `input()`.
- - ![Evidencia08](docs/practica-03/evidencia03/Captura%20de%20pantalla%202026-10-15%20202606.png)
- - ![Evidencia08](docs/practica-03/evidencia03/Captura%20de%20pantalla%202026-10-15%20202704.png)

- **Evidencia 9 (Repositorio en GitHub):** Vista del repositorio actualizado con los cambios de la Práctica 3.
- - - ![Evidencia08](docs/practica-03/evidencia03/Captura%20de%20pantalla%202026-10-16%20110801.png)

---

## 7. Conclusiones Individuales

### Conclusión - Samuel Ceniceros Dorantes
Durante el desarrollo de esta práctica logré consolidar conceptos fundamentales de programación en Python aplicados directamente al modelado de infraestructura de redes. Aprendí a utilizar estructuras de datos avanzadas como diccionarios y listas para organizar atributos técnicos complejos, así como a implementar bucles iterativos, estructuras condicionales y funciones modulares. Representé los dispositivos de la red estructurando la información topológica obtenida de GNS3 en diccionarios anidados dentro de listas. Una de las principales dificultades que encontré fue un error de tipo `KeyError` debido a la ausencia de ciertos atributos en el switch, además de conflictos por nombrar igual a la lista y al iterador. Solucioné estos inconvenientes unificando el esquema de datos de todos los equipos y aplicando un control estricto de nombres en el ciclo `for`. La relación entre Python y la automatización de redes radica en que los scripts necesitan un modelo de datos lógico antes de poder enviar comandos o peticiones a los equipos mediante protocolos de red. Finalmente, este programa sirve como la base lógica para construir en etapas posteriores herramientas capaces de conectarse a los routers y switches simulados para automatizar su gestión de manera eficiente.

### Conclusión - Christian Noe Esparza Meza
Esta práctica me permitió comprender cómo el software y la programación estructurada facilitan la representación de sistemas complejos de telecomunicaciones. Aprendí a manejar diccionarios para agrupar propiedades de hardware y software, listas para colecciones de nodos, y funciones para reutilizar bloques de código de impresión. La representación de la red se basó en abstraer los routers y switches de nuestra topología de GNS3 en estructuras de pares clave-valor que reflejan sus direcciones IP, estados y protocolos. Durante la codificación enfrenté dificultades menores con la validación de claves en elementos heterogéneos y en la estructuración de la función de búsqueda interactiva por consola. Los problemas se resolvieron estandarizando las llaves de los diccionarios y aplicando métodos de comparación insensible a mayúsculas. Existe una relación directa entre Python y la automatización, ya que el lenguaje provee la lógica necesaria para procesar inventarios de red antes de ejecutar despliegues automatizados. Este programa evolucionará en el proyecto integrador para convertirse en el núcleo de procesamiento que alimentará scripts de configuración masiva en el entorno virtualizado.

### Conclusión - Cesar Alexander Fuentes Garcia
El desarrollo de esta actividad reforzó mis habilidades en lógica de programación y modelado de datos orientados al ámbito de redes informáticas. Aprendí a implementar y combinar variables, diccionarios, listas, ciclos `for`, sentencias `if` y funciones con parámetros para procesar información de forma automatizada. Para representar la red, estructuré los parámetros de los dispositivos de la Práctica 2 en diccionarios limpios que simulan registros de configuración de equipos reales. Una dificultad que se presentó fue el manejo de excepciones cuando un dispositivo no poseía todos los atributos estándar definidos en la función de impresión. Esto lo solucioné completando los metadatos de los equipos y comprendiendo la importancia de la consistencia en las estructuras de datos. La automatización de redes depende enteramente de la capacidad de Python para interpretar y manipular estructuras de esta naturaleza de forma programática. En las siguientes etapas del proyecto integrador, este programa base será fundamental para evolucionar hacia scripts que extraigan información directamente desde la red y ejecuten tareas operativas de manera autónoma.

**Próximo paso:** Desarrollar programas que permitan procesar, consultar y automatizar información directamente relacionada con la infraestructura de red.

##### Práctica 4
Exploración de comunidades, documentación y recursos de colaboración. **Estado:** Completada.  
Se identificaron y analizaron recursos de documentación y comunidades relacionados con Python, GNS3 y la automatización de redes. Se organizó una base de conocimiento técnica para apoyar la resolución de problemas durante las siguientes etapas del proyecto integrador.  

## 1. Propósito de la práctica
Conocer y evaluar recursos técnicos de documentación oficial, herramientas de redes y comunidades de colaboración para establecer una base de conocimiento sólida orientada a la resolución de problemas en el proyecto integrador.

## 2. Relación con el proyecto integrador
Permite que el equipo adquiera habilidades de investigación estructurada, evaluación de fuentes confiables y resolución de incidencias en scripts de Python y topologías de GNS3.

## 3. Recursos consultados: síntesis y enlaces
* **Documentación de Python:** [https://www.python.org/](https://www.python.org/) / [https://docs.python.org/es/3/](https://docs.python.org/es/3/)
* **Documentación y recursos de redes:** [Cisco DevNet](https://developer.cisco.com/docs/), [Network to Code](https://networktocode.com/community/open-source/), [Red Hat Ansible](https://www.redhat.com/es/technologies/management/ansible/network-automation).
* **Comunidades:** [Stack Overflow en español](https://es.stackoverflow.com/) y [Comunidad de Python](https://www.python.org/community/).

## 7. Conclusiones individuales

### Christian Noe Esparza Meza
Durante esta práctica aprendí la importancia de consultar documentación oficial y comunidades de programación. Comprendí que la documentación oficial ofrece información confiable, mientras que las comunidades comparten experiencias y soluciones de otros usuarios. Para saber si una fuente es confiable, es importante revisar quién la publica, cuándo fue actualizada y si contiene información correcta. Las comunidades pueden ayudarme a resolver errores de Python mediante ejemplos y respuestas de otros programadores. También aprendí que GitHub permite guardar y organizar las soluciones encontradas. Esto facilita que los integrantes del equipo puedan consultar la información cuando la necesiten. Además, estos recursos nos ayudarán a solucionar problemas relacionados con GNS3 y la automatización de redes. Considero que lo aprendido será de gran utilidad para desarrollar las siguientes prácticas del proyecto integrador.

### Samuel Ceniceros Dorantes
Con esta actividad comprendí que existen diferentes recursos que pueden ayudarnos durante el desarrollo de un proyecto. La documentación oficial proporciona instrucciones y explicaciones sobre las herramientas, mientras que las comunidades ofrecen respuestas a problemas específicos. Para elegir una fuente confiable debemos verificar que tenga información actualizada, ejemplos claros y un autor reconocido. En Python, las comunidades pueden ser útiles cuando encontramos errores que no sabemos cómo solucionar. Podemos buscar preguntas similares y revisar las soluciones que otros usuarios han compartido. También es importante documentar en GitHub los problemas encontrados y los pasos que seguimos para resolverlos. De esta manera evitamos repetir errores y mantenemos un registro del trabajo realizado. Estos conocimientos nos permitirán trabajar de manera más organizada y mejorar nuestros programas de automatización de redes.

### Cesar Alexander Fuentes García
Al realizar esta investigación conocí herramientas y comunidades que facilitan el aprendizaje de Python y la configuración de redes. Aprendí que la documentación oficial contiene información técnica de las herramientas, mientras que las comunidades permiten intercambiar conocimientos. Considero importante comprobar que las fuentes sean confiables, estén actualizadas y tengan ejemplos que podamos verificar. Cuando tenga dificultades con un programa de Python, podré consultar Stack Overflow o la documentación oficial para encontrar posibles soluciones. Sin embargo, antes de utilizar cualquier código será necesario comprobar que funcione correctamente en nuestro proyecto. GitHub nos ayudará a almacenar los archivos y registrar las soluciones para que todo el equipo tenga acceso a ellas. También podremos utilizar Cisco DevNet, GNS3 y otros recursos para investigar problemas de configuración y automatización. En conclusión, esta práctica me enseñó que investigar, comprobar y documentar la información es fundamental para desarrollar correctamente el proyecto integrador.


**Próximo paso:** Continuar el desarrollo de programas en Python y utilizar los recursos técnicos investigados para resolver problemas durante su implementación.

# Práctica 5: Automatización de Redes con Python y Telnet

Automatización de despliegue de configuraciones en router vía Telnet con Python. **Estado:** Completada.  
Se desarrolló e implementó un script en Python capaz de conectarse vía Telnet a un router simulado en GNS3 para automatizar la creación de interfaces Loopback y la configuración del protocolo OSPF, validando su correcta aplicación en el dispositivo.  


## 1. Datos del equipo
- **Integrantes:** 
  - Samuel Ceniceros Dorantes
  - Christian Noe Esparza Meza
  - Cesar Alexander Fuentes Garcia
- **Grupo:** 3IRI1V
- **Asignatura:** Automatización de Infraestructura Digital I
- **Fecha:** Octubre 2026

## 2. Propósito de la práctica
Automatizar el despliegue de configuraciones en un router dentro de un entorno simulado (GNS3), específicamente la creación de interfaces Loopback y la habilitación del protocolo de enrutamiento dinámico OSPF, utilizando un script en Python mediante el protocolo Telnet.

## 3. Desarrollo y Explicación
El script desarrollado se conecta de forma remota al dispositivo de red utilizando las capacidades de Python. Su funcionamiento general comprende:
1. **Establecimiento de conexión:** Uso de credenciales (usuario y contraseña) para acceder a la consola del router mediante Telnet.
2. **Envío de comandos interactivos:** Envío automatizado de secuencias de comandos para entrar al modo de configuración privilegiada (`enable`), acceder a la configuración global (`configure terminal`), crear las interfaces virtuales y configurar OSPF.
3. **Lectura y cierre:** Captura de la respuesta del equipo para validar el procesamiento de las instrucciones y cierre seguro de la conexión.

## 4. Verificación de Resultados
Se validó la aplicación correcta de la automatización ejecutando comandos de verificación directamente en el router:
- **Interfaces Loopback:** Se comprobó mediante `show ip interface brief` que las interfaces lógicas fueron creadas y se encuentran activas.
- **Enrutamiento OSPF:** Se verificó el funcionamiento del protocolo mediante `show ip ospf neighbor` y `show ip route`.


## 5. Conclusiones

### Samuel Ceniceros Dorantes
Durante esta práctica comprendí la enorme ventaja que representa la automatización frente a la configuración manual por CLI. El uso de scripts en Python para interactuar con equipos de red mediante Telnet permite ahorrar tiempo y reduce drásticamente el margen de error humano al desplegar configuraciones repetitivas. Aprendí a estructurar la secuencia de comandos y a lidiar con los tiempos de respuesta del dispositivo para asegurar que cada instrucción se ejecute en el orden correcto. Esta herramienta será fundamental para optimizar las siguientes fases del proyecto integrador, permitiéndome gestionar infraestructuras complejas de forma programática.

### Christian Noe Esparza Meza
La realización de esta práctica me permitió visualizar de forma práctica cómo el software y las redes convergen mediante la automatización. Implementar un script que configure de manera autónoma interfaces y protocolos de enrutamiento como OSPF en un router simulado abre un panorama completamente nuevo para la administración de infraestructura. Enfrentamos algunos retos con los tiempos de espera y la sincronización al enviar los comandos, lo cual solucioné ajustando las pausas del script. Considero que este tipo de habilidades técnicas son indispensables para cualquier especialista en redes hoy en día.

### Cesar Alexander Fuentes Garcia
Esta práctica integró los conocimientos de programación en Python con los fundamentos de redes de datos vistos previamente. Entendí cómo establecer sesiones interactivas remotas desde un script y cómo validar que las configuraciones impacten positivamente al equipo de red. Las dificultades encontradas al autenticar y enviar comandos por Telnet nos enseñaron la importancia de depurar paso a paso el código. En el futuro del proyecto integrador, este tipo de scripts automatizados facilitarán enormemente la implementación y el mantenimiento de topologías de red escalables.

## 7. Estructura del Repositorio de la Práctica
```text
automatizacion-redes/
├── src/
│   └── automatizacion_telnet.py
└── docs/
    └── practica-05/
        ├── README.md
        └── evidencias/
            ├── 01-ejecucion-script.png
            ├── 02-interfaces-r1.png
            └── 03-ospf-routing.png

**Próximo paso:** Continuar con el desarrollo de scripts avanzados de automatización para la gestión integral de la infraestructura de red.

##Actividad 2.7: Gestión colaborativa de versiones con Git y GitHub . Cierre y reflexión

1. **¿Qué beneficios ofrece Git para administrar proyectos de software?**
   Ofrece un control de versiones distribuido que facilita la colaboración en equipo sin riesgo de sobrescribir el trabajo de otros, mantiene un historial detallado y trazable de cada modificación (quién, cuándo y qué se cambió), y permite la recuperación rápida de versiones anteriores estables cuando un cambio introduce un error.

2. **¿Qué función desempeñan el directorio de trabajo, el área de preparación y el repositorio local?**
   * **Directorio de trabajo:** Es el espacio en el disco duro donde se editan, crean y modifican los archivos del proyecto en tiempo real.
   * **Área de preparación (Staging Area):** Funciona como un puente o zona intermedia donde se seleccionan y agrupan de forma controlada los archivos que formarán parte de la próxima confirmación.
   * **Repositorio local:** Es la base de datos interna de Git en la computadora que almacena de manera permanente el historial completo de los commits y versiones del proyecto.

3. **¿Cuál es la diferencia entre un commit y una rama?**
   * Un **commit** es una confirmación o instantánea (*snapshot*) que guarda de forma permanente el estado de los archivos en un momento específico del proyecto.
   * Una **rama (branch)** es una línea de desarrollo independiente que permite experimentar, desarrollar nuevas características o corregir errores de forma aislada sin alterar la rama principal (`main` o `master`) hasta que el trabajo esté listo para integrarse.

4. **¿Por qué es importante revisar los cambios antes de integrarlos?**
   Es fundamental para verificar que el código o los archivos modificados funcionen correctamente, evitar conflictos de contenido con el trabajo de otros compañeros, detectar posibles errores de sintaxis u omisiones, y asegurar que la rama principal permanezca siempre estable.

5. **¿Cómo podrían aplicar lo aprendido en futuros proyectos colaborativos?**
   Implementando un flujo de trabajo estructurado basado en ramas específicas para cada tarea o integrante, realizando commits frecuentes con mensajes claros y descriptivos, y aplicando buenas prácticas de integración y revisión antes de fusionar los cambios en el repositorio compartido.