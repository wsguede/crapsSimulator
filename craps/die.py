from typing import List


class Die:

  previous_rolls: List[int] = []

  def __init__(self: Die):
    pass

  def roll(self):
    from random import randrange
    value: int = randrange(6000) % 6+1
    self.previous_rolls.append(value)
    return value
