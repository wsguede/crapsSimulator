from craps.table import Table
from craps.player import Player, SequentialDiceStrategy, RandomDiceStrategy

bill = Player("Bill", 200.00, None, SequentialDiceStrategy())
abner = Player("Abner", 200.00, None, RandomDiceStrategy())
chris = Player("Chris", 200.00, None, SequentialDiceStrategy())
alex = Player("Alex", 200.00, None, RandomDiceStrategy())
peyton = Player("Peyton", 200.00, None, SequentialDiceStrategy())
blake = Player("Blake", 200.00, None, RandomDiceStrategy())

craps_table = Table()
craps_table.add_player(bill)
craps_table.add_player(abner)
craps_table.add_player(chris)
craps_table.add_player(alex)
craps_table.add_player(peyton)
craps_table.add_player(blake)

iteration = 0
while iteration < 1000:
  craps_table.play()
  iteration += 1

print("\n\n---------- Stats ----------")
craps_table.print_stats()
