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
*(Nota: Asegúrate de colocar tus capturas en la carpeta de evidencias y enlazar correctamente las rutas)*
- **Evidencia 1 (Estructura del repositorio):** Captura de la jerarquía de carpetas en VS Code.
- **Evidencia 2 y 3 (Código y Ejecución inicial):** Creación de variables y salida en consola con `print()`.
- **Evidencia 4 (Dispositivos de Práctica 2):** Adaptación de datos con parámetros de GNS3 (R1, R2).
- **Evidencia 5 y 6 (Listas, diccionarios y ciclos):** Implementación de estructuras de datos y bucle `for`.
- **Evidencia 7 (Función y condicionales):** Modularización con `def` y validaciones de estado `if`.
- **Evidencia 8 (Reto Final):** Funcionamiento de la función de búsqueda interactiva por teclado con `input()`.
- **Evidencia 9 (Repositorio en GitHub):** Vista del repositorio actualizado con los cambios de la Práctica 3.

---

## 7. Conclusiones Individuales

### Conclusión - Samuel Ceniceros Dorantes
Durante el desarrollo de esta práctica logré consolidar conceptos fundamentales de programación en Python aplicados directamente al modelado de infraestructura de redes. Aprendí a utilizar estructuras de datos avanzadas como diccionarios y listas para organizar atributos técnicos complejos, así como a implementar bucles iterativos, estructuras condicionales y funciones modulares. Representé los dispositivos de la red estructurando la información topológica obtenida de GNS3 en diccionarios anidados dentro de listas. Una de las principales dificultades que encontré fue un error de tipo `KeyError` debido a la ausencia de ciertos atributos en el switch, además de conflictos por nombrar igual a la lista y al iterador. Solucioné estos inconvenientes unificando el esquema de datos de todos los equipos y aplicando un control estricto de nombres en el ciclo `for`. La relación entre Python y la automatización de redes radica en que los scripts necesitan un modelo de datos lógico antes de poder enviar comandos o peticiones a los equipos mediante protocolos de red. Finalmente, este programa sirve como la base lógica para construir en etapas posteriores herramientas capaces de conectarse a los routers y switches simulados para automatizar su gestión de manera eficiente.

### Conclusión - Christian Noe Esparza Meza
Esta práctica me permitió comprender cómo el software y la programación estructurada facilitan la representación de sistemas complejos de telecomunicaciones. Aprendí a manejar diccionarios para agrupar propiedades de hardware y software, listas para colecciones de nodos, y funciones para reutilizar bloques de código de impresión. La representación de la red se basó en abstraer los routers y switches de nuestra topología de GNS3 en estructuras de pares clave-valor que reflejan sus direcciones IP, estados y protocolos. Durante la codificación enfrenté dificultades menores con la validación de claves en elementos heterogéneos y en la estructuración de la función de búsqueda interactiva por consola. Los problemas se resolvieron estandarizando las llaves de los diccionarios y aplicando métodos de comparación insensible a mayúsculas. Existe una relación directa entre Python y la automatización, ya que el lenguaje provee la lógica necesaria para procesar inventarios de red antes de ejecutar despliegues automatizados. Este programa evolucionará en el proyecto integrador para convertirse en el núcleo de procesamiento que alimentará scripts de configuración masiva en el entorno virtualizado.

### Conclusión - Cesar Alexander Fuentes Garcia
El desarrollo de esta actividad reforzó mis habilidades en lógica de programación y modelado de datos orientados al ámbito de redes informáticas. Aprendí a implementar y combinar variables, diccionarios, listas, ciclos `for`, sentencias `if` y funciones con parámetros para procesar información de forma automatizada. Para representar la red, estructuré los parámetros de los dispositivos de la Práctica 2 en diccionarios limpios que simulan registros de configuración de equipos reales. Una dificultad que se presentó fue el manejo de excepciones cuando un dispositivo no poseía todos los atributos estándar definidos en la función de impresión. Esto lo solucioné completando los metadatos de los equipos y comprendiendo la importancia de la consistencia en las estructuras de datos. La automatización de redes depende enteramente de la capacidad de Python para interpretar y manipular estructuras de esta naturaleza de forma programática. En las siguientes etapas del proyecto integrador, este programa base será fundamental para evolucionar hacia scripts que extraigan información directamente desde la red y ejecuten tareas operativas de manera autónoma.