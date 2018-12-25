from random import randrange
from typing import Tuple, List
from craps.dice import Dice
from craps.player import Player

class Table:

  def __init__(self):
    print("Welcome to the table")
    print("Place your bets!")
    self.players: List[Player] = []
    self.shooter: int = None
    dice_base = randrange(1000, 10000, 5)
    self.dice: Tuple[Dice] = (Dice(dice_base),
                 Dice(dice_base+1),
                 Dice(dice_base+2),
                 Dice(dice_base+3),
                 Dice(dice_base+4))
    self.active_dice: Tuple[int, int] = None
    self.point: int = None

  def add_player(self, player: Player):
    self.players.append(player)

  def play(self):
    if self.shooter is None:
      self._new_shooter()
    # TODO if shooter is None: end the game
    value = self.players[self.shooter].shoot_dice(self.active_dice)
    self.resolve_bets(value)

  def _new_shooter(self):
    num_players = len(self.players)
    if num_players == 0:
      self.shooter = None
    elif self.shooter is None:
      self.shooter = 0
    else:
      self.shooter = (self.shooter + 1) % num_players

    if self.shooter is not None:
      self.active_dice = self.players[self.shooter].select_dice(self.dice)

  def resolve_bets(self, dice_outcome: int):
    if self.point is None:
      if dice_outcome == 7 or dice_outcome == 11:
        # odds = 1:1
        # win
        print("winner winner chicken dinner")
      elif dice_outcome == 2 or dice_outcome == 3 or dice_outcome == 12:
        # lose
        print("lose - craps")
      else:
        self.point = dice_outcome
    else:
      # point is set
      if dice_outcome == 7:
        # lose
        print("seven out - new shooter!!")
        self.point = None
        self._new_shooter()
      elif dice_outcome == self.point:
        # odds
        #   pass: 1:1
        #   pass_odds
        #     4/10: 2:1
        #      5/9: 3:2
        #      6/8: 6:5
        # win
        print("point matched! WIN")
        self.point = None
      else:
        # place bets (multi roll)
        #   odds:
        #     4/10: 9:5
        #      5/9: 7:5
        #      6/8: 7:6
        # field bet (per roll)
        #   odds:
        #     3/4/9/10/11: 1:1
        #      2: 2:1
        #     12: 3:1
        # check for side bets
        print(".")

  def print_stats(self):
    for die in self.dice:
      die.print_stats()
    print()
    for player in self.players:
      player.print_stats()
