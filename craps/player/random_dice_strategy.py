from random import randrange
from typing import Tuple
from craps.dice import Dice
from craps.player.dice_strategy import DiceStrategy


class RandomDiceStrategy(DiceStrategy):

  @staticmethod
  def select_dice(dice: Tuple[Dice]):
    num_dice: int = len(dice)
    index1: int = randrange(num_dice*1000) % num_dice
    index2: int = randrange(num_dice*1000) % num_dice
    while index2 == index1:
      index2: int = randrange(num_dice*1000) % num_dice
    return (dice[index1], dice[index2])
