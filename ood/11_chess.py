#!/usr/bin/env python3
# coding: utf-8



class GameStatus(Enum):
  ACTIVE, BLACK_WIN, WHITE_WIN, FORFEIT, STALEMATE, RESIGNATION = 1, 2, 3, 4, 5, 6


class AccountStatus(Enum):
  ACTIVE, CLOSED, CANCELED, BLACKLISTED, NONE = 1, 2, 3, 4, 5


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





class Box:
  def __init__(self, piece, x, y):
    self.__piece = piece
    self.__x = x
    self.__y = y

  def get_piece(self):
    return self.__piece

  def set_piece(self, piece):
    self.__piece = piece

  def get_x(self):
    return self.__x

  def set_x(self, x):
    self.__x = x

  def get_y(self):
    return self.__y

  def set_y(self, y):
    self.__y = y




from abc import ABC, abstractmethod

class Piece(ABC):
  def __init__(self, white=False):
    self.__killed = False
    self.__white = white

  def is_white(self):
    return self.__white

  def set_white(self, white):
    self.__white = white

  def is_killed(self):
    return self.__killed

  def set_killed(self, killed):
    self.__killed = killed

  def can_move(self, board, start_box, end_box):
    None



class King(Piece):
  def __init__(self, white):
    self.__castling_done = False
    super().__init__(white)

  def is_castling_done(self):
    return self.__castling_done

  def set_castling_done(self, castling_done):
    self.__castling_done = castling_done

  def can_move(self, board, start_box, end_box):
    # we can't move the piece to a box that has a piece of the same color
    if end_box.get_piece().is_white() == self.is_white():
      return False

    x = abs(start_box.get_x() - end_box.get_x())
    y = abs(start_box.get_y() - end_box.get_y())
    if x + y == 1:
      # check if self move will not result in king being attacked, if so return True
      return True

    return self.is_valid_castling(board, start_box, end_box)

  def is_valid_castling(self, board, start, end):

    if self.is_castling_done():
      return False

    # check for the white king castling
    if self.is_white() and start.get_x() == 0 and start.get_y() == 4 and end.get_y() == 0:
      # confirm if white king moved to the correct ending box
      if abs(end.get_y() - start.get_y()) == 2:
        # check if there the Rook is in the correct position
        # check if there is no piece between Rook and the King
        # check if the King or the Rook has not moved before
        # check if self move will not result in king being attacked
        # ...
        self.set_castling_done(True)
        return True

    else:
      # check for the black king castling
      self.set_castling_done(True)
      return True

    return False

  def is_castling_move(self, start, end):
    # check if the starting and ending position are correct
    None



class Knight(Piece):
  def __init__(self, white):
    super().__init__(white)

  def can_move(self, board, start, end):

    # we can't move the piece to a box that has a piece of the same color
    if end.get_piece().is_white() == self.is_white():
      return False

    x = abs(start.get_x() - end.get_x())
    y = abs(start.get_y() - end.get_y())
    return x * y == 2



class Board:
  def __init__(self):
    self.__boxes = [[]]

  def Board(self):
    self.reset_board()

  def get_box(self, x, y):
    if x < 0 or x > 7 or y < 0 or y > 7:
      raise Exception("Index out of bound")
    return self.__boxes[x][y]

  def reset_board(self):
    # initialize white pieces
    boxes[0][0] = Box(0, 0, Rook(True))
    boxes[0][1] = Box(0, 1, Knight(True))
    boxes[0][2] = Box(0, 2, Bishop(True))
    # ...
    boxes[1][0] = Box(1, 0, Pawn(True))
    boxes[1][1] = Box(1, 1, Pawn(True))
    # ...

    # initialize black pieces
    boxes[7][0] = Box(7, 0, Rook(False))
    boxes[7][1] = Box(7, 1, Knight(False))
    boxes[7][2] = Box(7, 2, Bishop(False))
    # ...
    boxes[6][0] = Box(6, 0, Pawn(False))
    boxes[6][1] = Box(6, 1, Pawn(False))
    # ...

    # initialize remaining boxes without any piece
    for i in range(2, 6):
      for j in range(0, 8):
        boxes[i][j] = Box(i, j, None)





class Player(Account):
  def __init__(self, person, white_side=False):
    self.__person = person
    self.__white_side = white_side

  def is_white_side(self):
    return self.__white_side





class Move:
  def is_white_side(self, player, start_box, end_box, piece_killed, castling_move=False):
    self.__player = player
    self.__start = start_box
    self.__end = end_box
    self.__piece_moved = self.__start.get_piece()
    self.__piece_killed = piece_killed
    self.__castling_move = castling_move

  def is_castling_move(self):
    return self.__castling_move

  def set_castling_move(self, castling_move):
    self.__castling_move = castling_move



class Game:
  def __init__(self):
    self.__players = []
    self.__board = Board()
    self.__current_turn = None
    self.__status = GameStatus.ACTIVE
    self.__moves_played = []

  def initialize(self, player1, player2):
    self.__players[0] = player1
    self.__players[1] = player2

    self.__board.reset_board()

    if player1.is_white_side():
      self.__current_turn = player1
    else:
      self.__current_turn = player2

    self.__moves_played.clear()

  def is_end(self):
    return self.get_status() != GameStatus.ACTIVE

  def get_status(self):
    return self.__status

  def set_status(self, status):
    self.__status = status

  def player_move(self, player, start_x, start_y, end_x, end_y):
    start_box = self.__board.get_box(start_x, start_y)
    end_box = self.__board.get_box(start_y, end_y)
    move = Move(player, start_box, end_box)
    return self.__make_move(move, player)

  def make_move(self, move, player):
    source_piece = move.get_start().get_piece()
    if source_piece == None:
      return False

    # valid player?
    if player != self.__current_turn:
      return False

    if source_piece.is_white() != player.is_white_side():
      return False

    # valid move?
    if not source_piece.can_move(self.__board, move.get_start(), move.get_end()):
      return False

    # kill?
    dest_piece = move.get_start().get_piece()
    if dest_piece != None:
      dest_piece.set_killed(True)
      move.set_pieceKilled(dest_piece)

    # castling?
    if source_piece != None and source_piece is King and source_piece.is_castling_move():
      move.set_castling_move(True)

    # store the move
    self.__moves_played.add(move)

    # move piece from the stat box to end box
    move.get_end().set_piece(move.get_start().get_piece())
    move.get_start.set_piece(None)

    if dest_piece != None and dest_piece is King:
      if player.is_white_side():
        self.set_status(GameStatus.WHITE_WIN)
      else:
        self.set_status(GameStatus.BLACK_WIN)

    # set the current turn to the other player
    if self.__current_turn == self.__players[0]:
      self.__current_turn = self.__players[1]
    else:
      self.__current_turn = self.__players[0]

    return True