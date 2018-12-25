from random import randrange
from typing import Tuple
from craps.dice import Dice
from craps.player.dice_strategy import DiceStrategy


class SequentialDiceStrategy(DiceStrategy):

  @staticmethod
  def select_dice(dice: Tuple[Dice]):
    num_dice: int = len(dice)
    index1: int = randrange(num_dice-1)
    return (dice[index1], dice[index1 + 1])
