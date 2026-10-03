## Pruebas finales

Realizar las pruebas necesarias para comprobar el funcionamiento de la topología. Registrar:

| Prueba                    | Resultado                              | Evidencia                 |
| :------------------------ | :------------------------------------- | :------------------------ |
| **R1 → R2**               | 80% de éxito (4/5); 20% de pérdida     | Ping de R1 a `10.1.1.2`   |
| **R2 → R1**               | 100% de éxito (5/5); 0% de pérdida     | Ping de R2 a `10.1.1.1`   |
| **Estado de interfaces**  | Gi0/0 y Loopback0 de R1 aparecen up/up | `show ip interface brief` |
| **Vecino OSPF**           | Vecino `2.2.2.2` en estado FULL/BDR    | `show ip ospf neighbor`   |
| **Tabla de enrutamiento** | Ruta OSPF `2.2.2.2/32` vía `10.1.1.2`  | `show ip route`           |