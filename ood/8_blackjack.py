#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()



class SUIT(Enum):
  HEART, SPADE, CLUB, DIAMOND = 1, 2, 3, 4



class Card:
  def __init__(self, suit, face_value):
    self.__suit = suit
    self.__face_value = face_value

  def get_suit(self):
    return self.__suit

  def get_face_value(self):
    return self.__face_value






class BlackjackCard(Card):
  def __init__(self, suit, face_value):
    super().__init__(suit, face_value)
    self.__game_value = face_value
    if self.__game_value > 10:
      self.__game_value = 10

  def get_game_value(self):
    return self.__game_value




class Deck:
  def __init__(self):
    self.__cards = []
    self.__creation_date = datetime.date.today()
    for value in range(1, 14):
      for suit in SUIT:
        self.__cards.add(BlackjackCard(suit, value))

  def get_cards(self):
    self.__cards


class Shoe:
  def __init__(self, number_of_decks):
    self.__cards = []
    self.__number_of_decks = number_of_decks
    self.create_shoe()
    self.shuffle()

  def create_shoe(self):
    for decks in range(0, self.__number_of_decks):
      self.__cards.add(Deck().get_cards())

  import random

  def shuffle(self):
    card_count = self.__cards.size()
    for i in range(0, card_count):
      j = random.randrange(0, card_count - i - 1, 1)
      self.__cards[i], self.__cards[j] = self.__cards[j], self.__cards[i]

  # Get the next card from the shoe
  def deal_card(self):
    if self.__cards.size() == 0:
      create_shoe()
    return self.__cards.remove(0)





class Hand:
  def __init__(self, blackjack_card1, blackjack_card2):
    self.__cards = [blackjack_card1, blackjack_card1]

  def get_scores(self):
    totals = [0]

    for card in self.__cards:
      new_totals = []
      for score in totals:
        new_totals.add(card.face_value() + score)
        if card.face_value() == 1:
          new_totals.add(11 + score)

      totals = new_totals

    return totals

  def add_card(self, card):
    self.__cards.add(card)

  # get highest score which is less than or equal to 21

  def resolve_score(self):
    scores = self.get_scores()
    best_score = 0
    for score in scores:
      if score <= 21 and score > best_score:
        best_score = score

    return best_score





from abc import ABC, abstractmethod

class BasePlayer(ABC):
  def __init__(self, id, password, balance, status, person):
    self.__id = id
    self.__password = password
    self.__balance = balance
    self.__status = status
    self.__person = person
    self.__hands = []

  def reset_password(self):
    None

  def get_hands(self):
    return self.__hands

  def add_hand(self, hand):
    return self.__hands.add(hand)

  def remove_hand(self, hand):
    self.__hands.remove(hand)


class Player(BasePlayer):
  def __init__(self, id, password, balance, status, person):
    super.__init__(id, password, balance, status, person)
    self.__bet = 0
    self.__total_cash = 0


class Dealer(BasePlayer):
  def __init__(self, id, password, balance, status, person):
    super.__init__(id, password, balance, status, person)






class Game:
  def __init__(self, player, dealer):
    self.__player = player
    self.__dealer = dealer
    self.__MAX_NUM_OF_DECKS = 3
    self.__shoe = Shoe(self.__MAX_NUM_OF_DECKS)

  def play_action(self, action, hand):
    switcher = {
      "hit": self.hit(hand),
      "split": self.split(hand),
      "stand pat": None,  # do nothing
      "stand": self.stand()
    }
    switcher.get(action, 'Invalid move')

  def hit(self, hand):
    self.__hand.add_card(self.__shoe.deal_card())

  def stand(self):
    dealer_score = self.__dealer.get_total_score()
    player_score = self.__player.get_total_score()
    hands = self.__player.get_hands()
    for hand in hands:
      best_score = hand.resolve_score()
      if player_score == 21:
        # blackjack, pay 3: 2 of the bet
        None
      elif player_score > dealer_score:
        # pay player equal to the bet
        None
      elif player_score < dealer_score:
        # collect the bet from the player
        None
      else:  # tie
        # bet goes back to player
        None

  def split(self, hand):
    cards = hand.get_cards()
    self.__player.add_hand(Hand(cards[0], self.__shoe.deal_card()))
    self.__player.add_hand(Hand(cards[1], self.__shoe.deal_card()))
    self.__player.remove_hand(hand)

  def start(self):
    self.__player.place_bet(get_bet_from_UI())

    player_hand = Hand(self.__shoe.deal_card(),
                       self.__shoe.deal_card())
    self.__player.add_to_hand(player_hand)

    dealer_hand = Hand(self.__shoe.deal_card(),
                       self.__shoe.deal_card())
    self.__dealer.add_to_hand(dealer_hand)

    while True:
      hands = self.__player.get_hands()
      for hand in hands:
        action = get_user_action(hand)
        self.play_action(action, hand)
        if action.equals("stand"):
          break


def main():
  player = Player()
  dealer = Dealer()
  game = Game(player, dealer)
  game.start()