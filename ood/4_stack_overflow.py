#!/usr/bin/env python3
# coding: utf-8


class QuestionStatus(Enum):
  OPEN, CLOSED, ON_HOLD, DELETED = 1, 2, 3, 4


class QuestionClosingRemark(Enum):
  DUPLICATE, OFF_TOPIC, TOO_BROAD, NOT_CONSTRUCTIVE, NOT_A_REAL_QUESTION, PRIMARILY_OPINION_BASED = 1, 2, 3, 4, 5, 6


class AccountStatus(Enum):
  ACTIVE, CLOSED, CANCELED, BLACKLISTED, BLOCKED = 1, 2, 3, 4, 5




# For simplicity, we are not defining getter and setter functions. The reader can
# assume that all class attributes are private and accessed through their respective
# public getter methods and modified only through their public methods function.


class Account:
  def __init__(self, id, password, name, address, email, phone, status=AccountStatus.Active):
    self.__id = id
    self.__password = password
    self.__name = name
    self.__address = address
    self.__email = email
    self.__phone = phone
    self.__status = status
    self.__reputation = 0

  def reset_password(self):
    None


class Member:
  def __init__(self, account):
    self.__account = account
    self.__badges = []

  def get_reputation(self):
    return self.__account.get_reputation()

  def get_email(self):
    return self.__account.get_email()

  def create_question(self, question):
    None

  def create_tag(self, tag):
    None


class Admin(Member):
  def block_member(self, member):
    None

  def unblock_member(self, member):
    None


class Moderator(Member):
  def close_question(self, question):
    None

  def undelete_question(self, question):
    None



class Badge:
  def __init__(self, name, description):
    self.__name = name
    self.__description = description


class Tag:
  def __init__(self, name, description):
    self.__name = name
    self.__description = description
    self.__daily_asked_frequency = 0
    self.__weekly_asked_frequency = 0

# import datetime


class Notification:
  def __init__(self, id, content):
    self.__notification_id = id
    self.__created_on = datetime.datetime.now()
    self.__content = content

  def send_notification(self):
    None





import datetime

class Photo:
  def __init__(self, id, path, member):
    self.__photo_id = id
    self.__photo_path = path
    self.__creation_date = datetime.datetime.now()
    self.__creating_member = member

  def delete(self):
    None

# import datetime


class Bounty:
  def __init__(self, reputation, expiry):
    self.__reputation = reputation
    self.__expiry = expiry

  def modify_reputation(self, reputation):
    None




from abc import ABC, abstractmethod

class Search(ABC):
  def search(self, query):
    None

import datetime

class Question(Search):
  def __init__(self, title, description, bounty, asking_member):
    self.__title = title
    self.__description = description
    self.__view_count = 0
    self.__vote_count = 0
    self.__creation_time = datetime.datetime.now()
    self.__update_time = datetime.datetime.now()
    self.__status = QuestionStatus.OPEN
    self.__closing_remark = QuestionClosingRemark.DUPLICATE

    self.__bounty = bounty
    self.__asking_member = asking_member
    self.__photos = []
    self.__comments = []
    self.__answers = []

  def close(self):
    None

  def undelete(self):
    None

  def add_comment(self, comment):
    None

  def add_bounty(self, bounty):
    None

  def search(self, query):
    # return all questions containing the string query in their title or description.
    None


class Comment:
  def __init__(self, text, member):
    self.__text = text
    self.__creation_time = datetime.datetime.now()
    self.__flag_count = 0
    self.__vote_count = 0
    self.__asking_member = member

  def increment_vote_count(self):
    None


class Answer:
  def __init__(self, text, member):
    self.__answer_text = text
    self.__accepted = False
    self.__vote_count = 0
    self.__flag_count = 0
    self.__creation_time = datetime.datetime.now()
    self.__creating_member = member
    self.__photos = []

  def increment_vote_count(self):
    None