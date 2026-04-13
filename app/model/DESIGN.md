Clase adicional: HotelService

1. Idea general

La clase HotelService la usé para representar los servicios extra que puede ofrecer el hotel, como spa, lavandería, minibar o transporte. La idea es que estos servicios no dependan de la habitación, pero sí puedan asociarse a una reserva.

2. Cómo la diseñé

La implementé como una dataclass porque básicamente es una clase que solo guarda información.

No tiene lógica compleja ni comportamiento avanzado, solo datos como el nombre del servicio, el precio y una descripción opcional. Usar dataclass hace que el código sea más limpio y evita escribir constructores innecesarios.

3. Atributos
name: nombre del servicio (ej: “Spa”).
price: costo del servicio.
description: descripción opcional. Si no se envía, queda como “Sin descripción”.

4. Método principal

__str__: lo usé para que el servicio se pueda imprimir de forma sencilla, por ejemplo:

Spa ($50)

5. Integración con el sistema

La clase se conecta directamente con Reservation.

Cada reserva puede tener varios servicios, por eso agregué:

services: list[HotelService] y el método: add_service(service)

Esto permite que una reserva vaya acumulando servicios consumidos durante la estadía.

También desde la clase Hotel se puede agregar un servicio a una reserva usando el método:

add_service_to_reservation(...)

6. Decisiones importantes
Los servicios pertenecen a una reserva, no al hotel en general, porque son consumos del huésped.
Mantuve HotelService como una clase independiente para que se pueda reutilizar sin depender de Reservation o Hotel.
La lógica de manejo de servicios se mantiene simple para no mezclar responsabilidades.

7. Principios de POO aplicados
Responsabilidad única: HotelService solo representa servicios, nada más.
Encapsulación: los servicios se gestionan desde la reserva, no desde fuera directamente.
Bajo acoplamiento: la clase no depende del resto del sistema.
Alta cohesión: todo dentro de la clase tiene relación directa con un servicio.