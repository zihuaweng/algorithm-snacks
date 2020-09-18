#!/usr/bin/env python3
# coding: utf-8

class VehicleType(Enum):
  CAR, TRUCK, ELECTRIC, VAN, MOTORBIKE = 1, 2, 3, 4, 5


class ParkingSpotType(Enum):
  HANDICAPPED, COMPACT, LARGE, MOTORBIKE, ELECTRIC = 1, 2, 3, 4, 5


class AccountStatus(Enum):
  ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, UNKNOWN = 1, 2, 3, 4, 5, 6


class ParkingTicketStatus(Enum):
  ACTIVE, PAID, LOST = 1, 2, 3


class Address:
  def __init__(self, street, city, state, zip_code, country):
    self.__street_address = street
    self.__city = city
    self.__state = state
    self.__zip_code = zip_code
    self.__country = country


class Person():
  def __init__(self, name, address, email, phone):
    self.__name = name
    self.__address = address
    self.__email = email
    self.__phone = phone



# 第二部分：

class Account:
  def __init__(self, user_name, password, person, status=AccountStatus.Active):
    self.__user_name = user_name
    self.__password = password
    self.__person = person
    self.__status = status

  def reset_password(self):
    None


class Admin(Account):
  def __init__(self, user_name, password, person, status=AccountStatus.Active):
    super().__init__(user_name, password, person, status)

  def add_parking_floor(self, floor):
    None

  def add_parking_spot(self, floor_name, spot):
    None

  def add_parking_display_board(self, floor_name, display_board):
    None

  def add_customer_info_panel(self, floor_name, info_panel):
    None

  def add_entrance_panel(self, entrance_panel):
    None

  def add_exit_panel(self, exit_panel):
    None


class ParkingAttendant(Account):
  def __init__(self, user_name, password, person, status=AccountStatus.Active):
    super().__init__(user_name, password, person, status)

  def process_ticket(self, ticket_number):
    None


# 第三部分
class ParkingSpot(ABC):
  def __init__(self, number, parking_spot_type):
    self.__number = number
    self.__free = True
    self.__vehicle = None
    self.__parking_spot_type = parking_spot_type

  def is_free(self):
    return self.__free

  def assign_vehicle(self, vehicle):
    self.__vehicle = vehicle
    free = False

  def remove_vehicle(self):
    self.__vehicle = None
    free = True


class HandicappedSpot(ParkingSpot):
  def __init__(self, number):
    super().__init__(number, ParkingSpotType.HANDICAPPED)


class CompactSpot(ParkingSpot):
  def __init__(self, number):
    super().__init__(number, ParkingSpotType.COMPACT)


class LargeSpot(ParkingSpot):
  def __init__(self, number):
    super().__init__(number, ParkingSpotType.LARGE)


class MotorbikeSpot(ParkingSpot):
  def __init__(self, number):
    super().__init__(number, ParkingSpotType.MOTORBIKE)


class ElectricSpot(ParkingSpot):
  def __init__(self, number):
    super().__init__(number, ParkingSpotType.ELECTRIC)


# 第四部分
from abc import ABC, abstractmethod

class Vehicle(ABC):
  def __init__(self, license_number, vehicle_type, ticket=None):
    self.__license_number = license_number
    self.__type = vehicle_type
    self.__ticket = ticket

  def assign_ticket(self, ticket):
    self.__ticket = ticket


class Car(Vehicle):
  def __init__(self, license_number, ticket=None):
    super().__init__(license_number, VehicleType.CAR, ticket)


class Van(Vehicle):
  def __init__(self, license_number, ticket=None):
    super().__init__(license_number, VehicleType.VAN, ticket)


class Truck(Vehicle):
  def __init__(self, license_number, ticket=None):
    super().__init__(license_number, VehicleType.TRUCK, ticket)


# Similarly we can define classes for Motorcycle and Electric vehicles


# 第五部分
class ParkingFloor:
  def __init__(self, name):
    self.__name = name
    self.__handicapped_spots = {}
    self.__compact_spots = {}
    self.__large_spots = {}
    self.__motorbike_spots = {}
    self.__electric_spots = {}
    self.__info_portals = {}
    self.__display_board = ParkingDisplayBoard()

  def add_parking_spot(self, spot):
    switcher = {
      ParkingSpotType.HANDICAPPED: self.__handicapped_spots.put(spot.get_number(), spot),
      ParkingSpotType.COMPACT: __compact_spots.put(spot.get_number(), spot),
      ParkingSpotType.LARGE: __large_spots.put(spot.get_number(), spot),
      ParkingSpotType.MOTORBIKE: __motorbike_spots.put(spot.get_number(), spot),
      ParkingSpotType.ELECTRIC: __electric_spots.put(spot.get_number(), spot),
    }
    switcher.get(spot.get_type(), 'Wrong parking spot type')

    # we can also use
    import collections.defaultdict
    d = defaultdict(lambda: 'Wrong parking spot type', switcher)
    return d[ParkingSpotType.HANDICAPPED]

  def assign_vehicleToSpot(self, vehicle, spot):
    spot.assign_vehicle(vehicle)
    switcher = {
      ParkingSpotType.HANDICAPPED: self.update_display_board_for_handicapped(spot),
      ParkingSpotType.COMPACT: self.update_display_board_for_compact(spot),
      ParkingSpotType.LARGE: self.update_display_board_for_large(spot),
      ParkingSpotType.MOTORBIKE: self.update_display_board_for_motorbike(spot),
      ParkingSpotType.ELECTRIC: self.update_display_board_for_electric(spot),
    }
    switcher(spot.get_type(), 'Wrong parking spot type!')

  def update_display_board_for_handicapped(self, spot):
    if self.__display_board.get_handicapped_free_spot().get_number() == spot.get_number():
      # find another free handicapped parking and assign to display_board
      for key in self.__handicapped_spots:
        if self.__handicapped_spots.get(key).is_free():
          self.__display_board.set_handicapped_free_spot(
            self.__handicapped_spots.get(key))

      self.__display_board.show_empty_spot_number()

  def update_display_board_for_compact(self, spot):
    if self.__display_board.get_compact_free_spot().get_number() == spot.get_number():
      # find another free compact parking and assign to display_board
      for key in self.__compact_spots.key_set():
        if self.__compact_spots.get(key).is_free():
          self.__display_board.set_compact_free_spot(
            self.__compact_spots.get(key))

      self.__display_board.show_empty_spot_number()

  def free_spot(self, spot):
    spot.remove_vehicle()
    switcher = {
      ParkingSpotType.HANDICAPPED: self.__free_handicapped_spot_count += 1,
      ParkingSpotType.COMPACT: self.__free_compact_spot_count += 1,
      ParkingSpotType.LARGE: self.__free_large_spot_count += 1,
      ParkingSpotType.MOTORBIKE: self.__free_motorbike_spot_count += 1,
      ParkingSpotType.ELECTRIC: self.__free_electric_spot_count += 1,
    }

    switcher(spot.get_type(), 'Wrong parking spot type!')


# 第六部分
class ParkingDisplayBoard:
  def __init__(self, id):
    self.__id = id
    self.__handicapped_free_spot = None
    self.__compact_free_spot = None
    self.__large_free_spot = None
    self.__motorbike_free_spot = None
    self.__electric_free_spot = None

  def show_empty_spot_number(self):
    message = ""
    if self.__handicapped_free_spot.is_free():
      message += "Free Handicapped: " + self.__handicapped_free_spot.get_number()
    else:
      message += "Handicapped is full"
    message += "\n"

    if self.__compact_free_spot.is_free():
      message += "Free Compact: " + self.__compact_free_spot.get_number()
    else:
      message += "Compact is full"
    message += "\n"

    if self.__large_free_spot.is_free():
      message += "Free Large: " + self.__large_free_spot.get_number()
    else:
      message += "Large is full"
    message += "\n"

    if self.__motorbike_free_spot.is_free():
      message += "Free Motorbike: " + self.__motorbike_free_spot.get_number()
    else:
      message += "Motorbike is full"
    message += "\n"

    if self.__electric_free_spot.is_free():
      message += "Free Electric: " + self.__electric_free_spot.get_number()
    else:
      message += "Electric is full"

    print(message)


# 第七部分
import threading

class ParkingLot:
  # singleton ParkingLot to ensure only one object of ParkingLot in the system,
  # all entrance panels will use this object to create new parking ticket: get_new_parking_ticket(),
  # similarly exit panels will also use this object to close parking tickets
  instance = None

  class __OnlyOne:
    def __init__(self, name, address):
      # 1. initialize variables: read name, address and parking_rate from database
      # 2. initialize parking floors: read the parking floor map from database,
      #    this map should tell how many parking spots are there on each floor. This
      #    should also initialize max spot counts too.
      # 3. initialize parking spot counts by reading all active tickets from database
      # 4. initialize entrance and exit panels: read from database

      self.__name = name
      self.__address = address
      self.__parking_rate = ParkingRate()

      self.__compact_spot_count = 0
      self.__large_spot_count = 0
      self.__motorbike_spot_count = 0
      self.__electric_spot_count = 0
      self.__max_compact_count = 0
      self.__max_large_count = 0
      self.__max_motorbike_count = 0
      self.__max_electric_count = 0

      self.__entrance_panels = {}
      self.__exit_panels = {}
      self.__parking_floors = {}

      # all active parking tickets, identified by their ticket_number
      self.__active_tickets = {}

      self.__lock = threading.Lock()

  def __init__(self, name, address):
    if not ParkingLot.instance:
      ParkingLot.instance = ParkingLot.__OnlyOne(name, address)
    else:
      ParkingLot.instance.__name = name
      ParkingLot.instance.__address = address

  def __getattr__(self, name):
    return getattr(self.instance, name)

  def get_new_parking_ticket(self, vehicle):
    if self.is_full(vehicle.get_type()):
      raise Exception('Parking full!')
    # synchronizing to allow multiple entrances panels to issue a new
    # parking ticket without interfering with each other
    self.__lock.acquire()
    ticket = ParkingTicket()
    vehicle.assign_ticket(ticket)
    ticket.save_in_DB()
    # if the ticket is successfully saved in the database, we can increment the parking spot count
    self.__increment_spot_count(vehicle.get_type())
    self.__active_tickets.put(ticket.get_ticket_number(), ticket)
    self.__lock.release()
    return ticket

  def is_full(self, type):
    # trucks and vans can only be parked in LargeSpot
    if type == VehicleType.Truck or type == VehicleType.Van:
      return self.__large_spot_count >= self.__max_large_count

    # motorbikes can only be parked at motorbike spots
    if type == VehicleType.Motorbike:
      return self.__motorbike_spot_count >= self.__max_motorbike_count

    # cars can be parked at compact or large spots
    if type == VehicleType.Car:
      return (self.__compact_spot_count + self.__large_spot_count) >= (self.__max_compact_count + self.__max_large_count)

    # electric car can be parked at compact, large or electric spots
    return (self.__compact_spot_count + self.__large_spot_count + self.__electric_spot_count) >= (self.__max_compact_count + self.__max_large_count
                                                                                                  + self.__max_electric_count)

  # increment the parking spot count based on the vehicle type
  def increment_spot_count(self, type):
    if type == VehicleType.Truck or type == VehicleType.Van:
      large_spot_count += 1
    elif type == VehicleType.Motorbike:
      motorbike_spot_count += 1
    elif type == VehicleType.Car:
      if self.__compact_spot_count < self.__max_compact_count:
        compact_spot_count += 1
      else:
        large_spot_count += 1
    else:  # electric car
      if self.__electric_spot_count < self.__max_electric_count:
        electric_spot_count += 1
      elif self.__compact_spot_count < self.__max_compact_count:
        compact_spot_count += 1
      else:
        large_spot_count += 1

  def is_full(self):
    for key in self.__parking_floors:
      if not self.__parking_floors.get(key).is_full():
        return False
    return True

  def add_parking_floor(self, floor):
    # store in database
    None

  def add_entrance_panel(self, entrance_panel):
    # store in database
    None

  def add_exit_panel(self,  exit_panel):
    # store in database
    None


