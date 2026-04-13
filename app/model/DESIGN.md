HotelService Design
1. Decisión de diseño

Se implementó la clase HotelService como una dataclass.
Tome la decisión de crearlo como dataclass porque la clase representa principalmente datos simples (nombre, precio y descripción), sin requerir lógica compleja.

El uso de dataclass permite reducir código repetitivo y mantener consistencia con otras clases del modelo como Guest y Reservation.

2. Responsabilidad de la clase

La clase HotelService tiene solamente responsabilidad como las de: representar los servicios adicionales que ofrece el hotel, como por ejemplo:

* Servicio a la habitación
* Spa
* Transporte
* Lavandería

Cada objeto de esta clase encapsula la información de un servicio específico.

3. Integración con el modelo

Se decidió integrar HotelService con la clase Reservation, ya que los servicios están directamente asociados a una estadía del cliente.

Para ello:

Se agregó el atributo services en Reservation como una lista de servicios.
Se implementaron los métodos:
add_service(): agrega un servicio a la reserva
remove_service(): elimina un servicio
total_services_cost(): calcula el costo total de los servicios

Además, en la clase Hotel se agregó el método:

add_service_to_reservation()

Esto permite gestionar los servicios desde el nivel del hotel, manteniendo coherencia con otros métodos como add_guest().

4. Principios de Programación Orientada a Objetos

Se aplicaron los siguientes principios:

Single Responsibility Principle (SRP):
La clase HotelService solo se encarga de representar servicios.
Encapsulación:
La gestión de servicios se realiza dentro de Reservation, evitando acceso directo a estructuras internas.
Alta cohesión:
Los servicios están asociados a la reserva, que es donde realmente tienen sentido.
Consistencia del diseño:
Se siguió el mismo patrón utilizado para huéspedes (Guest), lo que hace el sistema más entendible y mantenible.


5. Conclusión

La solución propuesta integra los servicios de manera natural dentro del modelo existente, manteniendo claridad, cohesión y aplicando buenas prácticas de diseño orientado a objetos.