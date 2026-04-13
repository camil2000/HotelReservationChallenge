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
