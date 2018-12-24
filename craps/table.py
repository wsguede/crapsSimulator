from typing import List
from .die import Die
from .user import User

class Table:

  point: int = None
  positions: List[User] = []
  dice: List[Die] = []

  def __init__(self: Table):
    print("Welcome to the table")
    print("Place your bets!")
    self.dice.append(Die())
    self.dice.append(Die())
    self.dice.append(Die())
    self.dice.append(Die())
    self.dice.append(Die())

  def add_player(self: Table, user: User):
    self.positions.append(user)

  def make_bets(self: Table):
    for player in self.positions:
      player.bet(self)
