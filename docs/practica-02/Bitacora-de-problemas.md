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