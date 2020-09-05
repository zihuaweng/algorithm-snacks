#!/usr/bin/env python3
# coding: utf-8

class Address:
  def __init__(self, street, city, state, zip_code, country):
    self.__street_address = street
    self.__city = city
    self.__state = state
    self.__zip_code = zip_code
    self.__country = country


class OrderStatus(Enum):
  UNSHIPPED, PENDING, SHIPPED, COMPLETED, CANCELED, REFUND_APPLIED = 1, 2, 3, 4, 5, 6


class AccountStatus(Enum):
  ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, UNKNOWN = 1, 2, 3, 4, 5, 6


class ShipmentStatus(Enum):
  PENDING, SHIPPED, DELIVERED, ON_HOLD = 1, 2, 3, 4


class PaymentStatus(Enum):
  UNPAID, PENDING, COMPLETED, FILLED, DECLINED, CANCELLED, ABANDONED, SETTLING, SETTLED, REFUNDED = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10


# 第二部分
# For simplicity, we are not defining getter and setter functions. The reader can
# assume that all class attributes are private and accessed through their respective
# public getter methods and modified only through their public methods function.


class Account:
  def __init__(self, user_name, password, name, email, phone, shipping_address, status=AccountStatus):
    self.__user_name = user_name
    self.__password = password
    self.__name = name
    self.__email = email
    self.__phone = phone
    self.__shipping_address = shipping_address
    self.__status = status.ACTIVE
    self.__credit_cards = []
    self.__bank_accounts = []

  def add_product(self, product):
    None

  def add_productReview(self, review):
    None

  def reset_password(self):
    None


from abc import ABC, abstractmethod

class Customer(ABC):
  def __init__(self, cart, order):
    self.__cart = cart
    self.__order = order

  def get_shopping_cart(self):
    return self.__cart

  def add_item_to_cart(self, item):
    None

  def remove_item_from_cart(self, item):
    None


class Guest(Customer):
  def register_account(self):
    None


class Member(Customer):
  def __init__(self, account):
    self.__account = account

  def place_order(self, order):
    None


# 第三部分
class ProductCategory:
  def __init__(self, name, description):
    self.__name = name
    self.__description = description


class ProductReview:
  def __init__(self, rating, review, reviewer):
    self.__rating = rating
    self.__review = review
    self.__reviewer = reviewer


class Product:
  def __init__(self, id, name, description, price, category, seller_account):
    self.__product_id = id
    self.__name = name
    self.__description = description
    self.__price = price
    self.__category = category
    self.__available_item_count = 0

    self.__seller = seller_account

  def get_available_count(self):
    return self.__available_item_count

  def update_price(self, new_price):
    None


# 第四部分
class Item:
  def __init__(self, id, quantity, price):
    self.__product_id = id
    self.__quantity = quantity
    self.__price = price

  def update_quantity(self, quantity):
    None


class ShoppingCart:
  def __init__(self):
    self.__items = []

  def add_item(self, item):
    None

  def remove_item(self, item):
    None

  def update_item_quantity(self, item, quantity):
    None

  def get_items(self):
    return self.__items

  def checkout(self):
    None


class OrderLog:
  def __init__(self, order_number, status=OrderStatus.PENDING):
    self.__order_number = order_number
    self.__creation_date = datetime.date.today()
    self.__status = status


class Order:
  def __init__(self, order_number, status=OrderStatus.PENDING):
    self.__order_number = 0
    self.__status = status
    self.__order_date = datetime.date.today()
    self.__order_log = []

  def send_for_shipment(self):
    None

  def make_payment(self, payment):
    None

  def add_order_log(self, order_log):
    None


# 第五部分
class ShipmentLog:
  def __init__(self, shipment_number, status=ShipmentStatus.PENDING):
    self.__shipment_number = shipment_number
    self.__status = status
    self.__creation_date = datetime.date.today()


class Shipment:
  def __init__(self, shipment_numbe, shipment_methodr):
    self.__shipment_number = shipment_number
    self.__shipment_date = datetime.date.today()
    self.__estimated_arrival = datetime.date.today()
    self.__shipment_method = shipment_method
    self.__shipmentLogs = []

  def add_shipment_log(self, shipment_log):
    None


# from abc import ABC, abstractmethod
class Notification(ABC):
  def __init__(self, id, content):
    self.__notification_id = id
    self.__created_on = datetime.date.today()
    self.__content = content

  def send_notification(self, account):
    None


# 第六部分
from abc import ABC, abstractmethod

class Search(ABC):
  def search_products_by_name(self, name):
    None

  def search_products_by_category(self, category):
    None


class Catalog(Search):
  def __init__(self):
    self.__product_names = {}
    self.__product_categories = {}

  def search_products_by_name(self, name):
    return self.product_names.get(name)

  def search_products_by_category(self, category):
    return self.product_categories.get(category)


