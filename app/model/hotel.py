from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from typing import ClassVar  # Importante para definir variables de clase puras
# Importación de utilidades según el requerimiento del ejercicio
from app.services.util import (
    generate_unique_id, guest_not_found_error, room_not_available_error,
    reservation_not_found_error, room_already_exists_error,
    date_lower_than_today_error, room_not_found_error
)

@dataclass
class HotelService:
    """
    Representa servicios extra (Spa, Minibar, etc.).
    Se usa dataclass por ser una entidad principalmente de datos.
    """
    name: str
    price: float
    description: str = "Sin descripción"
    def __str__(self) -> str:
        return f"{self.name} (${self.price})"

class Guest:
    # Usamos ClassVar para que no entren al constructor y no causen el TypeError
    REGULAR: ClassVar[str] = "regular"
    VIP: ClassVar[str] = "vip"
    name: str          # Obligatorio
    email: str         # Obligatorio
    type_: str = "regular"  # Opcional (con valor por defecto)
    def __str__(self) -> str:
        return f"Guest {self.name} ({self.email}) of type {self.type_}"
