#!/usr/bin/env python3
# coding: utf-8


class BookingStatus(Enum):
  REQUESTED, PENDING, CONFIRMED, CHECKED_IN, CANCELED, ABANDONED = 1, 2, 3, 4, 5, 6


class SeatType(Enum):
  REGULAR, PREMIUM, ACCESSIBLE, SHIPPED, EMERGENCY_EXIT, OTHER = 1, 2, 3, 4, 5, 6


class AccountStatus(Enum):
  ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, UNKNOWN = 1, 2, 3, 4, 5, 6


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
  def __init__(self, id, password, status=AccountStatus.Active):
    self.__id = id
    self.__password = password
    self.__status = status

  def reset_password(self):
    None


# from abc import ABC, abstractmethod
class Person(ABC):
  def __init__(self, name, address, email, phone, account):
    self.__name = name
    self.__address = address
    self.__email = email
    self.__phone = phone
    self.__account = account


class Customer(Person):
  def make_booking(self, booking):
    None

  def get_bookings(self):
    None


class Admin(Person):
  def add_movie(self, movie):
    None

  def add_show(self, show):
    None

  def block_user(self, customer):
    None


class FrontDeskOfficer(Person):
  def create_booking(self, booking):
    None


class Guest:
  def register_account(self):
    None






class Show:
  def __init__(self, id, played_at, movie, start_time, end_time):
    self.__show_id = id
    self.__created_on = datetime.date.today()
    self.__start_time = start_time
    self.__end_time = end_time
    self.__played_at = played_at
    self.__movie = movie


class Movie:
  def __init__(self, title, description, duration_in_mins, language, release_date, country, genre, added_by):
    self.__title = title
    self.__description = description
    self.__duration_in_mins = duration_in_mins
    self.__language = language
    self.__release_date = release_date
    self.__country = country
    self.__genre = genre
    self.__movie_added_by = added_by

    self.__shows = []

  def get_shows(self):
    None







class Booking:
  def __init__(self, booking_number, number_of_seats, status, show, show_seats, payment):
    self.__booking_number = booking_number
    self.__number_of_seats = number_of_seats
    self.__created_on = datetime.date.today()
    self.__status = status
    self.__show = show
    self.__seats = show_seats
    self.__payment = payment

  def make_payment(self, payment):
    None

  def cancel(self):
    None

  def assign_seats(self, seats):
    None


class ShowSeat(CinemaHallSeat):
  def __init__(self, id, is_reserved, price):
    self.__show_seat_id = id
    self.__is_reserved = is_reserved
    self.__price = price


class Payment:
  def __init__(self, amount, transaction_id, payment_status):
    self.__amount = amount
    self.__created_on = datetime.date.today()
    self.__transaction_id = transaction_id
    self.__status = payment_status







class City:
  def __init__(self, name, state, zip_code):
    self.__name = name
    self.__state = state
    self.__zip_code = zip_code


class Cinema:
  def __init__(self, name, total_cinema_halls, address, halls):
    self.__name = name
    self.__total_cinema_halls = total_cinema_halls
    self.__location = address

    self.__halls = halls


class CinemaHall:
  def __init__(self, name, total_seats, seats, shows):
    self.__name = name
    self.__total_seats = total_seats

    self.__seats = seats
    self.__shows = shows






from abc import ABC, abstractmethod

class Search(ABC):
  def search_by_title(self, title):
    None

  def search_by_language(self, language):
    None

  def search_by_genre(self, genre):
    None

  def search_by_release_date(self, rel_date):
    None

  def search_by_city(self, city_name):
    None


class Catalog(Search):
  def __init__(self):
    self.__movie_titles = {}
    self.__movie_languages = {}
    self.__movie_genres = {}
    self.__movie_release_dates = {}
    self.__movie_cities = {}

    def search_by_title(self, title):
      return self.__movie_titles.get(title)

    def search_by_language(self, language):
      return self.__movie_languages.get(language)

    # ...

    def search_by_city(self, city_name):
      return self.__movie_cities.get(city_name)







"""
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
 
BEGIN TRANSACTION;
 
    -- Suppose we intend to reserve three seats (IDs: 54, 55, 56) for ShowID=99 
    Select * From ShowSeat where ShowID=99 && ShowSeatID in (54, 55, 56) && isReserved=0 
 
    -- if the number of rows returned by the above statement is NOT three, we can return failure to the user.
    update ShowSeat table...
    update Booking table ...
 
COMMIT TRANSACTION;
"""







import java.sql.DriverManager;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.sql.ResultSet;

public class Customer extends Person {

  public boolean makeBooking(Booking booking) {
    List<ShowSeat> seats = booking.getSeats();
    Integer seatIds[] = new Integer[seats.size()];
    int index = 0;
    for(ShowSeat seat : seats) {
      seatIds[index++] = seat.getShowSeatId();
    }

    Connection dbConnection = null;
    try {
      dbConnection = getDBConnection();
      dbConnection.setAutoCommit(false);
      // ‘Serializable’ is the highest isolation level and guarantees safety from
      // Dirty, Nonrepeatable, and Phantoms reads
      dbConnection.setTransactionIsolation(Connection.TRANSACTION_SERIALIZABLE);

      Statement st = dbConnection.createStatement();
      String selectSQL = "Select * From ShowSeat where ShowID=? && ShowSeatID in (?) && isReserved=0";
      PreparedStatement preparedStatement = dbConnection.prepareStatement(selectSQL);
      preparedStatement.setInt(1, booking.getShow().getShowId());
      Array array = dbConnection.createArrayOf("INTEGER", seatIds);
      preparedStatement.setArray(2, array);

      ResultSet rs = preparedStatement.executeQuery();
      // With TRANSACTION_SERIALIZABLE all the read rows will have the write lock, so we can
      // safely assume that no one else is modifying them.
      if (rs.next()) {
        rs.last(); // move to the last row, to calculate the row count
        int rowCount = rs.getRow();
        // check if we have expected number of rows, if not, this means another process is
        // trying to process at least one of the same row, if that is the case we
        // should not process this booking.
        if(rowCount == seats.size()) {
          // update ShowSeat table...
          // update Booking table ...
          dbConnection.commit();
          return true;
        }
      }
    } catch (SQLException e) {
      dbConnection.rollback();
      System.out.println(e.getMessage());
    }
    return false;
  }
}