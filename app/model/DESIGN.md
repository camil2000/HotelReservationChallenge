Clase adicional: HotelService

1. Qué representa

La clase HotelService la usé para representar los servicios extras que puede ofrecer el hotel, como spa, lavandería, minibar o transporte. La idea es que estos servicios no hagan parte directa de la habitación o la reserva, pero sí puedan asociarse a ellas.

2. Decisión de diseño

Decidí hacer HotelService como una dataclass porque básicamente es una clase que guarda información.

No necesita lógica compleja, solo almacena datos como el nombre, el precio y una descripción opcional. Usar dataclass hace que el código sea más simple y fácil de leer, sin tener que escribir constructores manuales.

3. Atributos
name: nombre del servicio.
price: costo del servicio.
description: descripción opcional (por defecto es "Sin descripción").
4. Métodos

__str__: lo usé para que cuando se imprima el servicio se vea algo sencillo como:

Spa ($50)
5. Cómo se conecta con el resto del sistema

La conexión principal es con Reservation, donde agregué una lista de servicios:

services: list[HotelService]

También añadí el método:

add_service(service)

para poder ir agregando servicios a una reserva.

Desde Hotel también se puede agregar un servicio a una reserva con un método que busca la reserva por ID.

6. Ideas y principios usados
Cada clase tiene su función clara (los servicios no mezclan lógica de reservas).
Los servicios están dentro de la reserva, lo cual tiene sentido porque son consumidos por el huésped.
HotelService es independiente, no depende de otras clases.
Todo está organizado para que cada cosa se encargue de lo suyo.
