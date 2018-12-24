from .bet_strategy import BetStrategy
from .table import Table


class User:
  money: float = 0.00
  strategy: BetStrategy = None

  def __init__(self: User, money: float, strategy: BetStrategy):
    self.money = money
    self.strategy = strategy

  def bet(self: User, table: Table):
    pass