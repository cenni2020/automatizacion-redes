# Práctica 2.4: Exploración de Cisco DevNet y las certificaciones de Cisco

## 1. Datos del Equipo y Asignatura
* **Universidad:** Universidad Tecnológica de Matamoros (UT BIS)
* **Carrera:** Técnico Superior Universitario / Ingeniería en Tecnologías de la Información
* **Asignatura:** Automatización de Infraestructura Digital I
* **Unidad Temática:** II. Entornos de desarrollo y automatización de redes
* **Integrantes:** 
  * Christian
  * César
  * Samuel Ceniceros Dorantes
* **Fecha:** Octubre 2026

---

## 2. Propósito y Objetivos de la Práctica
* **Objetivo General:** Explorar la plataforma Cisco DevNet, identificar la estructura y ruta de las certificaciones de Cisco (orientadas a redes y desarrollo/automatización), así como analizar su aplicación directa en el proyecto integrador de automatización de infraestructura digital.
  
* **Objetivos Específicos:**
  1. Explorar el ecosistema y recursos disponibles en Cisco DevNet (API Documentation, Code Exchange, Sandbox, Learning Labs).
  2. Mapear y comparar el mapa de certificaciones de Cisco (CCNA, DevNet Associate, CCNP Enterprise, DevNet Professional, etc.).
  3. Identificar los conocimientos, habilidades y herramientas requeridas para la automatización de redes.
  4. Determinar la aplicabilidad técnica de las herramientas de DevNet en la topología y desarrollo del proyecto integrador.

---

## 3. Exploración de Cisco DevNet
Cisco DevNet es la plataforma y comunidad oficial de desarrolladores de Cisco diseñada para ayudar a los ingenieros de red y desarrolladores a integrar la automatización, las API y la programación en la infraestructura de TI.

### Recursos Clave de DevNet Identificados:
* **DevNet Sandbox:** Entornos virtuales de laboratorio en la nube gratuitos para probar código y APIs con hardware y software real de Cisco sin riesgo.
* **Code Exchange:** Repositorio comunitario de código abierto con scripts, librerías y colecciones de Postman listos para usarse.
* **API Documentation:** Documentación técnica detallada y referencias interactivas de API REST, NETCONF, RESTCONF y SDKs.
* **Learning Labs:** Tutoriales guiados e interactivos paso a paso para aprender desde fundamentos de Python hasta automatización avanzada de red.

---

## 4. Mapa de Certificaciones de Cisco

| Nivel / Ruta | Redes Tradicionales / Infraestructura | Automatización y Desarrollo (DevNet) |
| :--- | :--- | :--- |
| **Associate** | **CCNA** (Cisco Certified Network Associate) | **DevNet Associate** (DEVASC 200-901) |
| **Professional** | **CCNP Enterprise** (Core + Concentration) | **DevNet Professional** (DEVCOR + Specialty) |
| **Expert** | **CCIE Enterprise Infrastructure** | **DevNet Expert** |

### Conocimientos y Habilidades Requeridas (DevNet Associate / Professional):
* **Lenguajes y Programación:** Python, procesamiento de formatos de datos (JSON, XML, YAML).
* **Comprensión y Uso de APIs:** REST APIs, llamadas HTTP (GET, POST, PUT, DELETE), autenticación (Bearer Tokens, Basic Auth, API Keys) y uso de Postman.
* **Control de Versiones y Métodos:** Git, GitHub, integración continua y despliegue continuo (CI/CD).
* **Modelado de Datos y Protocolos:** Modelos YANG, protocolos NETCONF y RESTCONF.
* **Plataformas de Control de Red:** Cisco DNA Center (catalyst Center), SD-WAN, ACI y Meraki Dashboard API.
* **Infraestructura como Código (IaC) y Contenedores:** Docker, Ansible, Terraform y Jinja2 templates.

---

## 5. Aplicación al Proyecto Integrador
Las herramientas y metodologías aprendidas en Cisco DevNet se aplican de la siguiente manera al desarrollo de nuestro proyecto integrador:

1. **Gestión de Configuración y Código:** Uso de Git y GitHub para el control de versiones de los scripts de Python y archivos de topología.
2. **Pruebas en Sandbox / GNS3:** Simulación de equipos de red y pruebas de automatización con llamadas API sin afectar entornos de producción real.
3. **Automatización con Python:** Creación de scripts modularizados en `src/` para extraer información de los dispositivos, validar estados de interfaces y aplicar configuraciones masivas.
4. **Documentación Estructurada:** Uso de JSON/YAML para almacenar el inventario y estado de los dispositivos de red.

---

## 6. Evidencia de Consultas y Capturas de Pantalla

> **Ubicación de archivos:** Las imágenes de evidencia se encuentran dentro de la carpeta `docs/practica-02-4/evidencias/`.

### Evidencia 1: Exploración del Portal Cisco DevNet
*Portal principal de Cisco DevNet y navegación por las secciones de Learning Labs y Sandbox.*  
![Navegación DevNet]

### Evidencia 2: Consulta del Mapa de Certificaciones
*Estructura de la ruta de certificación DevNet y comparación con certificaciones tradicionales.*  
![Certificaciones Cisco]

---

## 7. Conclusiones Individuales

### Conclusión - Christian
> *"La exploración de Cisco DevNet me permitió entender el cambio de paradigma en la administración de redes. La transición de configurar dispositivo por dispositivo mediante CLI a manipular infraestructuras completas mediante APIs y código es fundamental. Identificar la certificación DevNet Associate nos da una hoja de ruta clara de las habilidades de Python, JSON y Git que debemos dominar para enriquecer nuestro proyecto integrador."*

### Conclusión - César
> *"Al analizar el mapa de certificaciones de Cisco, queda claro que las competencias híbridas (redes + desarrollo) son las más demandadas hoy en día. DevNet Sandbox resulta ser una herramienta sumamente útil para realizar pruebas sin costo de APIs y soluciones de red antes de implementarlas en nuestros entornos locales como GNS3 o VMware, lo cual acelera el proceso de aprendizaje y resolución de fallas."*

### Conclusión - Samuel Ceniceros Dorantes
> *"Esta práctica nos demuestra la importancia de estandarizar nuestras habilidades bajo los marcos de referencia de Cisco. Integrar herramientas como Postman, Git y Python no solo nos ayuda a resolver las actividades de la asignatura, sino que sienta la base para construir proyectos de automatización escalables, documentados y alineados a estándares internacionales de la industria."*

---

## 8. Referencias Bibliográficas
1. Cisco Systems, Inc. (2026). *Cisco DevNet: Developer Network*. Recuperado de https://developer.cisco.com/
2. Cisco Systems, Inc. (2026). *Cisco Training & Certifications*. Recuperado de https://www.cisco.com/c/en/us/training-events/resources/learning-services/certifications.html
3. DevNet Associate Exam Topic (200-901 DEVASC). Cisco Learning Network.