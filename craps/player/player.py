from typing import Tuple, List

from craps.player.bet_strategy import BetStrategy
from craps.player.dice_strategy import DiceStrategy
from craps.dice import Dice


class Player:

  def __init__(self, name: str, money: float, bet_strategy: BetStrategy, dice_strategy: DiceStrategy):
    self.name = name
    self.money: int = money
    self.bet_strategy: BetStrategy = bet_strategy
    self.dice_strategy: DiceStrategy = dice_strategy
    self.rolls: List[int] = []

  def bet(self):
    pass

  def select_dice(self, dice: Tuple[Dice]):
    return self.dice_strategy.select_dice(dice)

  def shoot_dice(self, active_dice: Tuple[Dice]):
    value: int = 0
    for die in active_dice:
      value = value + die.roll()
    print("  Value = %i" % value)
    self.rolls.append(value)
    return value

  def print_stats(self):
    num_rolls: int = len(self.rolls)
    if num_rolls > 0:
      print("Player (%s), rolled %i times and had the following distribution as a shooter." % (self.name, num_rolls))
      print("\t2: %.3f, 3: %.3f, 4: %.3f, 5: %.3f, 6: %.3f, 7: %.3f, 8: %.3f, 9: %.3f, 10: %.3f, 11: %.3f, 12: %.3f" % (
          (self.rolls.count(2)/num_rolls),
          (self.rolls.count(3)/num_rolls),
          (self.rolls.count(4)/num_rolls),
          (self.rolls.count(5)/num_rolls),
          (self.rolls.count(6)/num_rolls),
          (self.rolls.count(7)/num_rolls),
          (self.rolls.count(8)/num_rolls),
          (self.rolls.count(9)/num_rolls),
          (self.rolls.count(10)/num_rolls),
          (self.rolls.count(11)/num_rolls),
          (self.rolls.count(12)/num_rolls),
      ))
