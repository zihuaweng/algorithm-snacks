#!/usr/bin/env python3
# coding: utf-8


class ReservationStatus(Enum):
  REQUESTED, PENDING, CONFIRMED, CHECKED_IN, CANCELED, ABANDONED = 1, 2, 3, 4, 5, 6


class SeatType(Enum):
  REGULAR, KID, ACCESSIBLE, OTHER = 1, 2, 3, 4


class OrderStatus(Enum):
  RECEIVED, PREPARING, COMPLETED, CANCELED, NONE = 1, 2, 3, 4, 5


class TableStatus(Enum):
  FREE, RESERVED, OCCUPIED, OTHER = 1, 2, 3, 4


class AccountStatus(Enum):
  ACTIVE, CLOSED, CANCELED, BLACKLISTED, BLOCKED = 1, 2, 3, 4, 5


class PaymentStatus(Enum):
  UNPAID, PENDING, COMPLETED, FILLED, DECLINED, CANCELLED, ABANDONED, SETTLING, SETTLED, REFUNDED = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10


class Address:
  def __init__(self, street, city, state, zip_code, country):
    self.__street_address = street
    self.__city = city
    self.__state = state
    self.__zip_code = zip_code
    self.__country = country







# For simplicity, we are not defining getter and setter functions. The reader can
# assume that all class attributes are private and accessed through their respective
# public getter methods and modified only through their public methods function.


class Account:
  def __init__(self, id, password, address, status=AccountStatus.Active):
    self.__id = id
    self.__password = password
    self.__address = address
    self.__status = status

  def reset_password(self):
    None


# from abc import ABC, abstractmethod
class Person(ABC):
  def __init__(self, name, email, phone):
    self.__name = name
    self.__email = email
    self.__phone = phone


# from abc import ABC, abstractmethod
class Employee(ABC, Person):
  def __init__(self, id, account, name, email, phone):
    super().__init__(name, email, phone)
    self.__employee_id = id
    self.__date_joined = datetime.date.today()
    self.__account = account


class Receptionist(Employee):
  def __init__(self, id, account, name, email, phone):
    super().__init__(id, account, name, email, phone)

  def create_reservation(self):
    None

  def search_customer(self, name):
    None


class Manager(Employee):
  def __init__(self, id, account, name, email, phone):
    super().__init__(id, account, name, email, phone)

  def add_employee(self):
    None


class Chef(Employee):
  def __init__(self, id, account, name, email, phone):
    super().__init__(id, account, name, email, phone)

  def take_order(self):
    None








class Kitchen:
  def __init__(self, name):
    self.__name = name
    self.__chefs = []

  def assign_chef(self, chef):
    None


class Branch:
  def __init__(self, name, location, kitchen):
    self.__name = name
    self.__location = location
    self.__kitchen = kitchen

  def add_table_chart(self):
    None


class Restaurant:
  def __init__(self, name):
    self.__name = name
    self.__branches = []

  def add_branch(self, branch):
    None


class TableChart:
  def __init__(self, id):
    self.__table_chart_id = id
    self.__table_chart_image = []

  def print(self):
    None





class Table:
  def __init__(self, id, max_capacity, location_identifier, status=TableStatus.FREE):
    self.__table_id = id
    self.__max_capacity = max_capacity
    self.__location_identifier = location_identifier
    self.__status = status
    self.__seats = []

  def is_table_free(self):
    None

  def add_reservation(self):
    None

  def search(self, capacity, start_time):
    # return all tables with the given capacity and availability
    None


class TableSeat:
  def __init__(self):
    self.__table_seat_number = 0
    self.__type = SeatType.REGULAR

  def update_seat_type(self, seat_type):
    None


class Reservation:
  def __init__(self, id, people_count, notes, customer):
    self.__reservation_id = id
    self.__time_of_reservation = datetime.datetime.now()
    self.__people_count = people_count
    self.__status = ReservationStatus.REQUESTED
    self.__notes = notes
    self.__checkin_time = datetime.datetime.now()
    self.__customer = customer
    self.__tables = []
    self.__notifications = []

  def update_people_count(self, count):
    None







class MenuItem:
  def __init__(self, id, title, description, price):
    self.__menu_item_id = id
    self.__title = title
    self.__description = description
    self.__price = price

  def update_price(self,  price):
    None


class MenuSection:
  def __init__(self, id, title, description):
    self.__menu_section_id = id
    self.__title = title
    self.__description = description
    self.__menu_items = []

  def add_menu_item(self, menu_item):
    None


class Menu:
  def __init__(self, id, title, description):
    self.__menu_id = id
    self.__title = title
    self.__description = description
    self.__menu_sections = []

  def add_menu_section(self, menu_section):
    None

  def print(self):
    None








class MealItem:
  def __init__(self, id, quantity, menu_item):
    self.__meal_item_id = id
    self.__quantity = quantity
    self.__menu_item = menu_item

  def update_quantity(self, quantity):
    None


class Meal:
  def __init__(self, id, seat):
    self.__meal_id = id
    self.__seat = seat
    self.__menu_items = []

  def add_meal_item(self, meal_item):
    None


class Order:
  def __init__(self, id, status, table, waiter, chef):
    self.__order_id = id
    self.__OrderStatus = status
    self.__creation_time = datetime.datetime.now()

    self.__meals = []
    self.__table = table
    self.__waiter = waiter
    self.__chef = chef
    self.__check = Check()

  def add_meal(self, meal):
    None

  def remove_meal(self, meal):
    None

  def get_status(self):
    return self.__OrderStatus

  def set_status(self, status):
    None