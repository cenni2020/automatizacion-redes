# Práctica 5: Automatización de Redes con Python y Telnet

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

## 6. Estructura del Repositorio de la Práctica
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