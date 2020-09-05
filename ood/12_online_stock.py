#!/usr/bin/env python3
# coding: utf-8


class ReturnStatus(Enum):
  SUCCESS, FAIL, INSUFFICIENT_FUNDS, INSUFFICIENT_QUANTITY, NO_STOCK_POSITION = 1, 2, 3, 4, 5, 6


class OrderStatus(Enum):
  OPEN, FILLED, PARTIALLY_FILLED, CANCELLED = 1, 2, 3, 4


class TimeEnforcementType(Enum):
  GOOD_TILL_CANCELLED, FILL_OR_KILL, IMMEDIATE_OR_CANCEL, ON_THE_OPEN, ON_THE_CLOSE = 1, 2, 3, 4, 5


class AccountStatus(Enum):
  ACTIVE, CLOSED, CANCELED, BLACKLISTED, NONE = 1, 2, 3, 5


class Location:
  def __init__(self, street, city, state, zip_code, country):
    self.__street_address = street
    self.__city = city
    self.__state = state
    self.__zip_code = zip_code
    self.__country = country


class Constants:
  def __init__(self):
    self.__MONEY_TRANSFER_LIMIT = 100000






class StockExchange:
  # singleton, used for restricting to create only one instance
  instance = None

  class __OnlyOne:
    def __init__(self):
      None

  def __init__(self):
    if not StockExchange.instance:
      StockExchange.instance = StockExchange.__OnlyOne()

  def place_order(self, order):
    return_status = self.get_instance().submit_order(Order)
    return return_status






from abc import ABC, abstractmethod
import datetime

class Order(ABC):
  def __init__(self, id):
    self.__order_id = id
    self.__is_buy_order = False
    self.__status = OrderStatus.OPEN
    self.__time_enforcement = TimeEnforcementType.ON_THE_OPEN
    self.__creation_time = datetime.datetime.now()

    self.__parts = {}

  def set_status(self, status):
    self.status = status

  def save_in_DB(self):
  # save in the database

  def add_order_parts(self, parts):
    for part in parts:
      self.parts[part.get_id()] = part


class LimitOrder(Order):
  def __init__(self):
    self.__price_limit = 0.0







from abc import ABC, abstractmethod

class Account(ABC):
  def __init__(self, id, password, name, address, email, phone, status=AccountStatus.NONE):
    self.__id = id
    self.__password = password
    self.__name = name
    self.__address = address
    self.__email = email
    self.__phone = phone
    self.__status = AccountStatus.NONE

  def reset_password(self):
    None

import datetime

class Member(Account):
  def __init__(self):
    self.__available_funds_for_trading = 0.0
    self.__date_of_membership = datetime.date.today()
    self.__stock_positions = {}
    self.__active_orders = {}

  def place_sell_limit_order(self, stock_id, quantity, limit_price, enforcement_type):
    # check if member has this stock position
    if stock_id not in __stock_positions:
      return ReturnStatus.NO_STOCK_POSITION

    stock_position = __stock_positions[stock_id]
    # check if the member has enough quantity available to sell
    if stock_position.get_quantity() < quantity:
      return ReturnStatus.INSUFFICIENT_QUANTITY

    order = LimitOrder(stock_id, quantity, limit_price, enforcement_type)
    order.is_buy_order = False
    order.save_in_DB()
    success = StockExchange.place_order(order)
    if success:
      order.set_status(OrderStatus.FAILED)
      order.save_in_DB()
    else:
      self.active_orders.add(order.get_order_id(), order)
    return success

  def place_buy_limit_order(self, stock_id, quantity, limit_price, enforcement_type):
    # check if the member has enough funds to buy this stock
    if self.__available_funds_for_trading < quantity * limit_price:
      return ReturnStatus.INSUFFICIENT_FUNDS

    order = LimitOrder(stock_id, quantity, limit_price, enforcement_type)
    order.is_buy_order = True
    order.save_in_DB()
    success = StockExchange.place_order(order)
    if not success:
      order.set_status(OrderStatus.FAILED)
      order.save_in_DB()
    else:
      self.active_orders.add(order.get_order_id(), order)
    return success

  # this function will be invoked whenever there is an update from
  # stock exchange against an order
  def callback_stock_exchange(self, order_id, order_parts, status):
    order = self.active_orders[order_id]
    order.add_order_parts(order_parts)
    order.set_status(status)
    order.update_in_DB()

    if status == OrderStatus.FILLED or status == OrderStatus.CANCELLEd:
      self.active_orders.remove(order_id)






