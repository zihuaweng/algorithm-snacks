#!/usr/bin/env python3
# coding: utf-8



class ConnectionInvitationStatus(Enum):
  PENDING, ACCEPTED, REJECTED, CANCELED = 1, 2, 3, 4


class AccountStatus(Enum):
  ACTIVE, CLOSED, CANCELED, BLACKLISTED, DISABLED = 1, 2, 3, 4, 5


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


class Member(Person):
  def __init__(self, id, date_of_membership, name):
    self.__member_id = id
    self.__date_of_membership = date_of_membership
    self.__name = name

    self.__profile = Profile()
    self.__member_follows = []
    self.__member_connections = []
    self.__page_follows = []
    self.__member_suggestions = []
    self.__connection_invitations = []
    self.__group_follows = []

  def send_message(self, message):
    None

  def create_post(self, post):
    None

  def send_connection_invitation(self, invitation):
    None

  def search_member_suggestions(self):
    None


class Admin(Person):
  def block_user(self, customer):
    None

  def unblock_user(self, customer):
    None

  def enable_page(self, page):
    None

  def disable_page(self, page):
    None


class ConnectionInvitation:
  def __init__(self, member_invited, name, status=ConnectionInvitationStatus.PENDING):
    self.__member_invited = member_invited
    self.__status = status
    self.__date_created = datetime.date.today()
    self.__date_updated = datetime.date.today()

  def accept_connection(self):
    None

  def reject_connection(self):
    None




class Profile:
  def __init__(self, profile_picture, cover_photo, gender):
    self.__profile_picture = profile_picture
    self.__cover_photo = cover_photo
    self.__gender = gender

    self.__work_experiences = []
    self.__educations = []
    self.__places = []
    self.__stats = []

  def add_work_experience(self, work):
    None

  def add_education(self, education):
    None

  def add_place(self, place):
    None


class Work:
  def __init__(self, title, company, location, date_from, date_to, description):
    self.__title = title
    self.__company = company
    self.__location = location
    self.__from = date_from
    self.__to = date_to
    self.__description = description





class Page:
  def __init__(self, id, name, description, type, total_members):
    self.__page_id = id
    self.__name = name
    self.__description = description
    self.__type = type
    self.__total_members = total_members
    self.__recommendation = []

  def get_recommendation(self):
    return self.__recommendation


class Recommendation:
  def __init__(self, id, rating, description):
    self.__recommendation_id = id
    self.__rating = rating
    self.__description = description
    self.__created_at = datetime.date.today()






class Group:
  def __init__(self, id, name, description, total_members):
    self.__group_id = id
    self.__name = name
    self.__description = description
    self.__total_members = total_members
    self.__members = []

  def add_member(self, member):
    None

  def update_description(self, description):
    None


class Post:
  def __init__(self, id, text, total_likes, total_shares, owner):
    self.__post_id = id
    self.__text = text
    self.__total_likes = total_likes
    self.__total_shares = total_shares
    self.__owner = owner


class Message:
  def __init__(self, id, sent_to, body, media):
    self.__message_id = id
    self.__sent_to = sent_to
    self.__message_body = body
    self.__media = media

  def add_member(self, member):
    None


class Comment:
  def __init__(self, id, text, total_likes, owner):
    self.__comment_id = id
    self.__text = text
    self.__total_likes = total_likes
    self.__owner = owner






from abc import ABC, abstractmethod

class Search(ABC):
  def search_member(self, name):
    None

  def search_group(self, name):
    None

  def search_page(self, name):
    None

  def search_post(self, word):
    None


class SearchIndex(Search):
  def __init__(self):
    self.__member_names = {}
    self.__group_names = {}
    self.__page_titles = {}
    self.__posts = {}

  def add_member(self, member):
    if member.get_name() in self.__member_names:
      self.__member_names.get(member.get_name()).add(member)
    else:
      self.__member_names[member.get_name()] = member

  def add_group(self, group):
    None

  def add_page(self, page):
    None

  def add_post(self, post):
    None

  def search_member(self, name):
    return self.__member_names.get(name)

  def search_group(self, name):
    return self.__group_names.get(name)

  def search_page(self, name):
    return self.__page_titles.get(name)

  def search_post(self, word):
    return self.__posts.get(word)

