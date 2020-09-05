#!/usr/bin/env python3
# coding: utf-8



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


class MatchFormat(Enum):
  ODI, T20, TEST = 1, 2, 3


class MatchResult(Enum):
  LIVE, FINISHED, DRAWN, CANCELLED = 1, 2, 3, 4


class UmpireType(Enum):
  FIELD, RESERVED, TV = 1, 2, 3


class WicketType(Enum):
  BOLD, CAUGHT, STUMPED, RUN_OUT, LBW, RETIRED_HURT, HIT_WICKET, OBSTRUCTING = 1, 2, 3, 4, 5, 6, 7, 8


class BallType(Enum):
  NORMAL, WIDE, WICKET, NO_BALL = 1, 2, 3, 4


class RunType(Enum):
  NORMAL, FOUR, SIX, LEG_BYE, BYE, NO_BALL, OVERTHROW = 1, 2, 3, 4, 5, 6, 7






# For simplicity, we are not defining getter and setter functions. The reader can
# assume that all class attributes are private and accessed through their respective
# public getter methods and modified only through their public methods function.

class Player:
  def __init__(self, person):
    self.__person = person
    self.__contracts = []

  def add_contract(self, contract):
    None


class Admin:
  def __init__(self, person):
    self.__person = person

  def add_match(self, match):
    None

  def add_team(self, team):
    None

  def add_tournament(self, tournament):
    None


class Umpire:
  def __init__(self, person):
    self.__person = person

  def assign_match(self, match):
    None


class Referee:
  def __init__(self, person):
    self.__person = person

  def assign_match(self, match):
    None


class Commentator:
  def __init__(self, person):
    self.__person = person

  def assign_match(self, match):
    None




class Team:
  def __init__(self, name, coach):
    self.__name = name
    self.__players = []
    self.__news = []
    self.__coach = coach

  def add_tournament_squad(self, tournament_squad):
    None

  def add_player(self, player):
    None

  def add_news(self, news):
    None


class TournamentSquad:
  def __init__(self):
    self.__players = []
    self.__tournament_stats = []

  def add_player(self, player):
    None


class Playing11:
  def __init__(self):
    self.__players = []
    self.__twelfth_man = None

  def add_player(self, player):
    None





class Over:
  def __init__(self, number):
    self.__number = number
    self.__balls = []

  def add_ball(self, ball):
    None


class Ball:
  def __init__(self, balled_by, played_by, ball_type, wicket, runs, commentary):
    self.__balled_by = balled_by
    self.__played_by = played_by
    self.__type = ball_type

    self.__wicket = wicket
    self.__runs = runs
    self.__commentary = commentary


class Wicket:
  def __init__(self, wicket_type, player_out, caught_by, runout_by, stumped_by):
    self.__wicket_type = wicket_type
    self.__player_out = player_out
    self.__caught_by = caught_by
    self.__runout_by = runout_by
    self.__stumped_by = stumped_by


class Commentary:
  def __init__(self, text, commentator):
    self.__text = text
    self.__created_at = datetime.date.today()
    self.__created_by = commentator


class Inning:
  def __init__(self, number, start_time):
    self.__number = number
    self.__start_time = start_time
    self.__overs = []

  def add_over(self, over):
    None


# from abc import ABC, abstractmethod
class Match(ABC):
  def __init__(self, number, start_time, referee):
    self.__number = number
    self.__start_time = start_time
    self.__result = MatchResult.LIVE

    self.__teams = []
    self.__innings = []
    self.__umpires = []
    self.__referee = referee
    self.__commentators = []
    self.__match_stats = []

  def assign_stadium(self, stadium):
    None

  def assign_referee(self, referee):
    None


class ODI(Match):
# ...


class Test(Match):
# ...

