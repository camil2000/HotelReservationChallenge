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
    name: str
    price: float
    description: str = "Sin descripción"
    def __str__(self) -> str:
        return f"{self.name} (${self.price})"

class Guest:

    REGULAR: ClassVar[str] = "regular"
    VIP: ClassVar[str] = "vip"
    name: str
    email: str
    type_: str = "regular"
    def __str__(self) -> str:
        return f"Guest {self.name} ({self.email}) of type {self.type_}"

@dataclass
class Reservation:

    guest_name: str
    description: str
    check_in: date
    check_out: date

    guests: list[Guest] = field(default_factory=list, init=False)
    services: list[HotelService] = field(default_factory=list, init=False)
    id: str = field(default_factory=generate_unique_id)
    def add_guest(self, name: str, email: str, type_: str = "regular"):
        nuevo_huesped = Guest(name, email, type_)
        self.guests.append(nuevo_huesped)
    def delete_guest(self, guest_index: int):
        if 0 <= guest_index < len(self.guests):
            self.guests.pop(guest_index)
        else:
            guest_not_found_error()
    def add_service(self, service: HotelService):

        self.services.append(service)
    def __len__(self) -> int:
        return (self.check_out - self.check_in).days
    def __str__(self) -> str:
        return (f"ID: {self.id}\n"
                f"Guest: {self.guest_name}\n"
                f"Description: {self.description}\n"
                f"Dates: {self.check_in} - {self.check_out}")

class Room:
    def __init__(self, number: int, type_: str, price_per_night: float):
        self.number = number
        self.type_ = type_
        self.price_per_night = price_per_night
        self.availability: dict[date, str | None] = {}
        self._init_availability()
    def _init_availability(self):
        hoy = datetime.now().date()
        for i in range(365):
            fecha = hoy + timedelta(days=i)
            self.availability[fecha] = None
    def book(self, reservation_id: str, check_in: date, check_out: date):

        temp_date = check_in
        while temp_date < check_out:
            if self.availability.get(temp_date) is not None:
                room_not_available_error()
                return
            temp_date += timedelta(days=1)

        temp_date = check_in
        while temp_date < check_out:
            self.availability[temp_date] = reservation_id
            temp_date += timedelta(days=1)

    def release(self, reservation_id: str):
        released = False
        for d, saved_id in self.availability.items():
            if saved_id == reservation_id:
                self.availability[d] = None
                released = True
        if not released:
            reservation_not_found_error()
    def update_booking(self, reservation_id: str, check_in: date, check_out: date):
        for d in self.availability:
            if self.availability[d] == reservation_id:
                self.availability[d] = None
        current = check_in
        while current < check_out:
            if self.availability.get(current) is not None:
                room_not_available_error()
            else:
                self.availability[current] = reservation_id
            current += timedelta(days=1)