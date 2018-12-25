from typing import Tuple
from craps.dice import Dice

class DiceStrategy:

  @staticmethod
  def select_dice(dice: Tuple[Dice]):
    raise NotImplementedError
