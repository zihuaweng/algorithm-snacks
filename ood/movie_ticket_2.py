#!/usr/bin/env python3
# coding: utf-8

"""
1. Requiremnt:
  - Book movie ticket
  - Cancel movie ticket
  - Select seat
  - Select cinema
  - Pay the ticket

2. User case (classes)
  - Admin
    Admin add / delete movie to the cinema
  - Person (customer, Casher)
    Guest: search / view movie
    Account: search / view movie, book, pay ticket, select seats
    Casher: book cancel order
  - 

3. Activities:
- book movice:
  - Search movie  (cls: Movie)
    - Not found: search again / exit
    - Found: 
      - Login
        - No account: register account (guest -> account)   cls: Account, Guest, 
        - login:
          - select date, select time, select seat   cls: Order, Seat, Ticket, Receipt, Cinema, Cahser
          - pay the ticket
          - get ther receipt

- cancel ticket:
  - login
    - find the order
        - not found: search again / exit
        - found:
            - verify if order is in valid timeframe
                - expire: search again / exit
                - not expire: 
                    - cancel it
                    - get recipt
                    - cancel other ticket

"""

class Genre(Enum):
    TYPE_ONE, TYPE_TWO, TYPE_THREE = 1,2,3

class OrderStatus(Enum):
    NOT_PAID, PENDING, COMPLETED, CANCEL = 1,2,3,4 


class Movie:
    def __init__(self, name: str, genre: Genre, start_date: str, price: float):
        pass


class Cinema:
    def __int__(self, name: str, address: Address):
        self.movies = []
        pass

    def add_movie(self, movie: Movie):
        self.movies.append(movie)


class Order:
    def __init(self, order_id:str, movie: Movie, price: float, cerate_date: str, status: OrderStatus):
        pass

    def cancel(self, order_id):
        self.status = OrderStatus.CANCEL


class Account:
    def __init__(self, account: str, passward: str):
        self.__account = account
        self.__passward = passward

    def reset_pwd(self, pwd):
        self.__passward = pwd


class Address:
    def __init__(self, country: str, street: str):
        self.__country = country
        self.__street = street


class Person:
    def __init__(self, name:str, date_of_birth:str, account: Account, address: Address):
        pass

    def rest_passward(self, pwd):
        self.account.reset_pwd(pwd)

class Customer(Person):
    def __init__(self, name:str, date_of_birth:str, account: Account, address: Address):
        super().__init__()
        pass

class Admin(Person):
    def __init__(self, name:str, date_of_birth:str, account: Account, address: Address, cinema: Cinema):
        super().__init__()
        pass

    def add_movie(self, movie: Movie):
        self.cinema.add_movie(movie)


class Casher(Person):
    def __init__(self, name:str, date_of_birth:str, account: Account, address: Address, cinema: Cinema):
        super().__init__()
        pass

    def book_movie():
        


