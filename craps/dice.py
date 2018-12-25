from random import randrange
from typing import List

class Dice:

  def __init__(self, number: int):
    self.number = number
    self.previous_rolls = []

  def roll(self, save: bool = True, show: bool = True):
    value: int = (randrange(6000) % 6) + 1
    if save:
      self.previous_rolls.append(value)
    if show:
      print('[%i]' % value, end='', flush=True)
    return value

  def print_stats(self):
    num_rolls: int = len(self.previous_rolls)
    if num_rolls > 0:
      print("Dice #%i, out of %i rolls the chance of getting each number." % (self.number, num_rolls))
      print("\t1: %.3f, 2: %.3f, 3: %.3f, 4: %.3f, 5: %.3f, 6: %.3f" % (
          (self.previous_rolls.count(1)/num_rolls),
          (self.previous_rolls.count(2)/num_rolls),
          (self.previous_rolls.count(3)/num_rolls),
          (self.previous_rolls.count(4)/num_rolls),
          (self.previous_rolls.count(5)/num_rolls),
          (self.previous_rolls.count(6)/num_rolls)
        ))


# ⚀,⚁,⚂,⚃,⚄,⚅
