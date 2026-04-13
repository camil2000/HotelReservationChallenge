from dataclasses import dataclass, field
from datetime import datetime, timedelta, date
import uuid

def generate_unique_id():
    return str(uuid.uuid4())

def guest_not_found_error():
    raise Exception("Guest not found")

def room_not_available_error():
    raise Exception("Room not available for selected dates")

def reservation_not_found_error():
    raise Exception("Reservation not found")

def room_already_exists_error():
    raise Exception("Room already exists")

def room_not_found_error():
    raise Exception("Room not found")

def date_lower_than_today_error():
    raise Exception("Check-in date cannot be earlier than today")

def service_not_found_error():
    raise Exception("Service not found")

@dataclass
class Guest:
    REGULAR = "regular"
    VIP = "vip"

    name: str
    email: str
    type_: str = REGULAR

    def __str__(self):
        return f"Guest {self.name} ({self.email}) of type {self.type_}"

@dataclass
class HotelService:
    name: str
    price: float
    description: str = ""

@dataclass
class Reservation:
    guest_name: str
    description: str
    check_in: date
    check_out: date

    guests: list = field(default_factory=list)
    services: list = field(default_factory=list)
    id: str = field(default_factory=generate_unique_id)

    def add_guest(self, name, email, type_):
        guest = Guest(name, email, type_)
        self.guests.append(guest)

    def delete_guest(self, guest_index: int):
        if 0 <= guest_index < len(self.guests):
            self.guests.pop(guest_index)
        else:
            guest_not_found_error()

    def add_service(self, service: HotelService):
        self.services.append(service)

    def remove_service(self, index: int):
        if 0 <= index < len(self.services):
            self.services.pop(index)
        else:
            service_not_found_error()

    def total_services_cost(self):
        return sum(s.price for s in self.services)

    def __len__(self):
        return (self.check_out - self.check_in).days

    def __str__(self):
        return (
            f"\nID: {self.id}\n"
            f"Guest: {self.guest_name}\n"
            f"Description: {self.description}\n"
            f"Dates: {self.check_in} - {self.check_out}\n"
            f"Nights: {len(self)}\n"
            f"Guests: {len(self.guests)}\n"
            f"Services Cost: ${self.total_services_cost()}\n"
        )
class Room:
    def __init__(self, number: int, type_: str, price_per_night: float):
        self.number = number
        self.type_ = type_
        self.price_per_night = price_per_night
        self.availability = {}

        self._init_availability()

    def _init_availability(self):
        today = datetime.now().date()
        for i in range(365):
            self.availability[today + timedelta(days=i)] = None

    def book(self, reservation_id: str, check_in, check_out):
        current = check_in

        # validar primero
        while current < check_out:
            if self.availability.get(current) is not None:
                room_not_available_error()
            current += timedelta(days=1)

        # asignar
        current = check_in
        while current < check_out:
            self.availability[current] = reservation_id
            current += timedelta(days=1)

    def release(self, reservation_id: str):
        released = False
        for d, saved_id in self.availability.items():
            if saved_id == reservation_id:
                self.availability[d] = None
                released = True
        if not released:
            reservation_not_found_error()

    def update_booking(self, reservation_id: str, check_in, check_out):
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

class Hotel:
    def __init__(self):
        self.rooms = {}
        self.reservations = {}

    def add_room(self, number, type_, price_per_night):
        if number in self.rooms:
            room_already_exists_error()

        self.rooms[number] = Room(number, type_, price_per_night)

    def make_reservation(self, guest_name, description, room_number, check_in, check_out):
        today = datetime.now().date()

        if check_in < today:
            date_lower_than_today_error()

        if room_number not in self.rooms:
            room_not_found_error()

        reservation = Reservation(guest_name, description, check_in, check_out)

        room = self.rooms[room_number]
        room.book(reservation.id, check_in, check_out)

        self.reservations[reservation.id] = reservation

        return reservation.id

    def add_guest(self, reservation_id, name, email, type_):
        reservation = self.reservations.get(reservation_id)
        if not reservation:
            reservation_not_found_error()

        reservation.add_guest(name, email, type_)

    def delete_guest(self, reservation_id, index):
        reservation = self.reservations.get(reservation_id)
        if not reservation:
            reservation_not_found_error()

        reservation.delete_guest(index)

    def add_service_to_reservation(self, reservation_id, service):
        reservation = self.reservations.get(reservation_id)
        if not reservation:
            reservation_not_found_error()

        reservation.add_service(service)

    def find_available_rooms(self, check_in, check_out):
        available_rooms = []

        for number, room in self.rooms.items():
            current = check_in
            available = True

            while current < check_out:
                if room.availability.get(current) is not None:
                    available = False
                    break
                current += timedelta(days=1)

            if available:
                available_rooms.append(number)

            return available_rooms

    def cancel_reservation(self, reservation_id: str):
        if reservation_id not in self.reservations:
            reservation_not_found_error()

        self.reservations.pop(reservation_id)

        for room in self.rooms.values():
            if reservation_id in room.availability.values():
                room.release(reservation_id)
                break

    def list_reservations(self):
        for r in self.reservations.values():
            print(r)

